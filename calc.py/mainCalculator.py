from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QMessageBox
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
        
        
    def makeMsgBox(self):
        return QMessageBox(self)