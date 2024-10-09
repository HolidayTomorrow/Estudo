import sys
from PySide6.QtCore import Slot, QSize
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget, QVBoxLayout, QToolBar)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primeira Janela")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.btn_ok = QPushButton("Ok")
        self.btn_ok.setStyleSheet('font-size: 12px;')
        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setStyleSheet('font-size: 12px;')
        
        self.layout_ = QGridLayout()
        self.central_widget.setLayout(self.layout_)
        self.layout_.addWidget(self.btn_ok, 5, 5, 1, 1)
        self.layout_.addWidget(self.btn_cancel, 5, 6, 1, 1)
        
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Esta é uma aplicação em nível de desenvolvimento.')

        self.menu = self.menuBar()
        self.menu_arquive = self.menu.addMenu('Arquivo')
        self.menu_new = self.menu_arquive.addAction('Novo Arquivo')

        self.menu_open = self.menu_arquive.addAction('Abrir')

        if self.menu_open.triggered.connect(self.slot_):
            self.menu_open = self.menu_arquive.addSeparator()
            
    def slot_(self):
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MyWindow()

    window.show()

    app.exec()
