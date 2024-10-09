import settings
from settings import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN, MEDIUM_FONT_SIZE
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QVBoxLayout


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
        font.setItalic(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')
        
    