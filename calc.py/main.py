import sys
from settings import setupTheme
from info import Info
from settings import WINDOW_ICON_PATH
from display import Display, ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout
)


class Calculator(QMainWindow):
    ...
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle('Calculadora')
        
        
        self.centralwidget_ = QWidget()
        self.layout_ = QVBoxLayout()
        self.centralwidget_.setLayout(self.layout_)
        self.setCentralWidget(self.centralwidget_)
        
        
        self.statusBar_ = self.statusBar()
        self.statusBar_.showMessage('Esta é uma aplicação em nível de desenvolvimento.')
        
        
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def addWidgetToVLayout(self, widget: QWidget):
        self.layout_.addWidget(widget)
        
    
if __name__=='__main__':
    
    app = QApplication(sys.argv)
    setupTheme(app)
    
    window = Calculator()
    
    
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    
    info = Info('Resultado')
    window.addWidgetToVLayout(info)
    
    
    display = Display()
    window.addWidgetToVLayout(display)
    
    buttonsGrid = ButtonsGrid(display, info)
    window.layout_.addLayout(buttonsGrid)
    buttonsGrid._makeGrid()
    
    
    window.adjustFixedSize()
    
    window.show()
    
    app.exec()