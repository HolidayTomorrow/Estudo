from info import Info
from utils import isNumOrDot, isEmpty, isValidNumber
from settings import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN, MEDIUM_FONT_SIZE
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QLineEdit, QPushButton, QGridLayout


class Display(QLineEdit):
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
    def __init__(self, display: Display, info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grid = [
            ['C', '↩', 'x\u02b8', '\u00F7'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._makeGrid()
        
        
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
        
    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._grid):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    font = button.font()
                    font.setBold(True)
                    font.setItalic(True)
                    button.setFont(font)
                self.addWidget(button, rowNumber, colNumber)
                buttonSlot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplay, button)
                button.clicked.connect(buttonSlot)
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def slot(_):
            func(*args, **kwargs)
        return slot
    
    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)
    
