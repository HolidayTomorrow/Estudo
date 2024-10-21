import sys
from settings import setupTheme
from info import Info
from mainCalculator import Calculator
from settings import WINDOW_ICON_PATH
from display import Display, ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
    
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

buttonsGrid = ButtonsGrid(display, info, window)
window.layout_.addLayout(buttonsGrid)
buttonsGrid._makeGrid()


window.adjustFixedSize()

window.show()

app.exec()