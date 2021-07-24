from PyQt5.QtWidgets import QDialog

import conf
from UI import Ui_quiz_selected

class QuizSelected:
    def __init__(self) -> None:
        self.dig = QDialog()
        self.ui = Ui_quiz_selected()
        self.ui.setupUi(self.dig)
        
        self.ui.back.clicked.connect(lambda:self.back())
        
    def back(self):
        conf.STACK.setCurrentWidget(conf.SCREENS_WIDGETS['quiz_list_scr'])