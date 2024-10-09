import sys
from settings import setupTheme
from info import Info
from settings import WINDOW_ICON_PATH
from display import Display, Button
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout
)


class Calculator(QMainWindow):
    ...
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle('Calculadora')
        
        
        self.centralwidget_ = QWidget()
        self.setCentralWidget(self.centralwidget_)
        
        self.layout_ = QGridLayout()
        
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
    
    
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)
    
    
    display = Display()
    window.addWidgetToVLayout(display)
    
    button = Button('Botão')
    window.centralwidget_.setLayout(window.layout_)
    window.addWidgetToVLayout(button)

    
    # button = Button("Tecla")
    # window.addWidgetToVLayout(button)
    
    window.adjustFixedSize()
    
    window.show()
    
    app.exec()