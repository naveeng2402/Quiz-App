import sys, os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QShortcut, QStackedWidget

from conf import set_prelim_constants, set_style_sheet, set_widgets, dummy
from screen_functions import *


if __name__ == '__main__':
    set_prelim_constants()
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')    
    set_style_sheet(app, os.path.join("ui", "style.qss"))

    stack = QStackedWidget()
    
    set_widgets(app, stack)

    # ByPassing Esc button
    esc = QShortcut(QtGui.QKeySequence('Esc'), stack)
    esc.activated.connect(dummy)

    quiz_list_scr()
    
    # STACK.setWindowIcon()
    stack.show()
    
    sys.exit(app.exec_())

    