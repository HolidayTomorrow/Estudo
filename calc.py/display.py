from info import Info
import math
from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber
from settings import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN, MEDIUM_FONT_SIZE
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import QLineEdit, QPushButton, QGridLayout
from mainCalculator import Calculator
from PySide6.QtGui import QKeyEvent

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
        
    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE*1.5)
        self.setMaximumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        
        
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]
        
        if isEnter:
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
        
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()
        
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()











class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
        
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(50, 50)










class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, info: Info, window: Calculator, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grid = [
            ['C', '↩', 'x\u02b8', '\u00F7'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Resultado'
        self._left = None
        self._right = None
        self._op = None
        
        self.equation = self._equationInitialValue
        self._makeGrid()
        
        
        
        
    @property
    def equation(self):
        return self._equation
    
    
    
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
        
        
        
        
        
    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertButtonTextToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        
        for rowNumber, rowData in enumerate(self._grid):
            for colNumber, buttonText in enumerate(rowData):
                self.button = Button(buttonText)
                
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    self.button.setProperty('cssClass', 'specialButton')
                    font = self.button.font()
                    font.setBold(True)
                    font.setItalic(True)
                    self.button.setFont(font)
                    self._configSpecialButton(self.button)
                    
                self.addWidget(self.button, rowNumber, colNumber)
                buttonSlot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplay, buttonText)
                self._connectButtonClicked(self.button, buttonSlot)
                
                
                
                
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
        
        
    def _configSpecialButton(self, button):
        text = button.text()
        
        if text == 'C':
            self._connectButtonClicked(button, self._clear)
            
        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)
            
        if text == '↩':
            self._connectButtonClicked(button, self.display.backspace)
            
        if text in ['+', '-', 'x', 'x\u02b8', '\u00F7']:
            self._connectButtonClicked(button, self._makeButtonDisplaySlot(self._configLeftOp, text))
        
        if text == '=':
            self._connectButtonClicked(button, self._eq)
            
            
            
            
    @Slot()       
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def slot(_):
            func(*args, **kwargs)
        return slot
    
    
    
    
    
    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()
        
        if not isValidNumber(displayText):
            return
        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))
    
    
    
    
    
    @Slot()
    def _insertButtonTextToDisplay(self, text):
        newDisplayValue = self.display.text() + text
        
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(text)
        self.display.setFocus()
        
        
        
        
    @Slot()    
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()
        
        
        
        
        
    @Slot()    
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()
        self.display.setFocus()
    
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Insira um número!')
            return
        
        if self._left is None:
            self._left = convertToNumber(displayText)

        if text == 'x\u02b8':
            text = '^'
        self._op = text
        self.equation = f'{self._left} {self._op}'
    
    
    
    
    
    @Slot()
    def _eq(self):
        displayText = self.display.text()
        
        if not isValidNumber(displayText) or self._left is None:
            self._showError('Expressão incompleta!')
            return 
        
        self._right = convertToNumber(displayText)
        if self._op == 'x':
            self._op = '*'
        if self._op == '\u00F7':
            self._op = '/'
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'ERROR'
        
        try:
            if '^' in self.equation and isinstance(self._left, (float, int)):
                result = math.pow(self._left, self._right)
                result = convertToNumber(str(result))
            else:
                result = convertToNumber(str(eval(self.equation)))
        except ZeroDivisionError:
            self._showError('Divisão por zero!')
        except OverflowError:
            self._showError('O resultado não pode ser concluído.')
        
        self.display.clear()
        
        if result == 'ERROR':
            self._left = None
            self._clear()
        else:
            self.info.setText(f'{self.equation} = {result}')
            self.display.insert(str(result))
            self._left = result
            self._right = None
        self.display.setFocus()
        
            
            
            
            
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()
        
        
        
        
        
    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox
    
    
    
    
    
        
    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setWindowTitle('Aviso')
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()
        
        
    
    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
        

