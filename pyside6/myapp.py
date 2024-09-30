import sys
import os
from random import choice
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QCheckBox,
    QMainWindow
)

basedir = os.path.dirname(__file__)
print("Current working folder:", os.getcwd())
print("Paths are relative to:", basedir)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("My App")
#         widget = QCheckBox("This is a checkbox")
#         widget.setCheckState(Qt.Checked)
        
        
#         widget.stateChanged.connect(self.show_state)
        
#         self.setCentralWidget(widget)
#     def show_state(self, s):
#         print(s == Qt.Checked)
#         print(s)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(basedir, "otje2.jpg")))
        widget.setScaledContents(True)
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # self.setFixedSize(QSize(500, 400))
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)
# 
# 
# window_titles = [
#     "My App",
#     "My App",
#     "Still My App",
#     "Still My App",
#     "What on earth",
#     "What on earth",
#     "This is surprising",
#     "This is surprising",
#     "Something went wrong",
# ]
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.n_times_clicked = 0
        
#         self.setWindowTitle("My App")
        
#         self.label = QLabel()
        
#         self.input = QLineEdit()
#         self.input.textChanged.connect(self.label.setText)
        
#         layout = QVBoxLayout()
#         layout.addWidget(self.input)
#         layout.addWidget(self.label)
        
#         container = QWidget()
#         container.setLayout(layout)
        
        
        
        
#         self.setCentralWidget(container)
        
    #     self.button = QPushButton("Press Me!")
    #     self.button.clicked.connect(self.the_button_was_clicked)
        
    #     self.windowTitleChanged.connect(self.the_window_title_changed)
        
    #     self.setCentralWidget(self.button)
        
    # def the_button_was_clicked(self):
    #     print("Clicked.")
    #     new_window_title = choice(window_titles)
    #     print(f"Setting title: {new_window_title}")
    #     self.setWindowTitle(new_window_title)
        
    # def the_window_title_changed(self, window_title):
    #     print(f"Window title changed: {window_title}")
        
    #     if window_title == "Something went wrong":
    #         self.button.setDisabled(True)
    #     self.button_is_checked = True
    #     self.setWindowTitle("A new window title")
    #     self.button = QPushButton("Press Me!")
    #     self.button.released.connect(self.the_button_was_clicked)
        
    #     self.setFixedSize(QSize(400, 300))
    #     # self.setMinimumSize(QSize(400, 300))
    #     # self.setMaximumSize(QSize(1920, 1080))
    #     self.setCentralWidget(self.button)
    
    # def the_button_was_clicked(self):
    #     self.button.setText("You already clicke me.")
    #     self.button.setEnabled(False)
        
    #     self.setWindowTitle("My Oneshot App")
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()