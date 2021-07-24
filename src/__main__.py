import sys, os
from PyQt5.QtWidgets import QApplication, QStackedWidget

from conf import set_prelim_constants, set_style_sheet, set_widgets
from screen_functions import *


if __name__ == '__main__':
    set_prelim_constants()
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')    
    set_style_sheet(app, os.path.join("ui", "style.qss"))

    stack = QStackedWidget()
    
    set_widgets(app, stack)

    quiz_list_scr()
    
    # STACK.setWindowIcon()
    stack.show()
    
    sys.exit(app.exec_())

    