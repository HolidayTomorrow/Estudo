from pathlib import Path
import qdarkstyle




PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'





qss = f"""
        QPushButton[cssClass="specialButton"] {{
            color: #fff;
            background: {PRIMARY_COLOR};
        }}
        QPushButton[cssClass="specialButton"]:hover {{
            color: #fff;
            background: {DARKER_PRIMARY_COLOR};
        }}
        QPushButton[cssClass="specialButton"]:pressed {{
            color: #fff;
            background: {DARKEST_PRIMARY_COLOR};
        }}
"""
def setupTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    app.setStyleSheet(app.styleSheet() + qss)




ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'


# Sizing

BIG_FONT_SIZE = 38
MEDIUM_FONT_SIZE = 22
SMALL_FONT_SIZE = 16
TEXT_MARGIN = 13
MINIMUM_WIDTH = 500