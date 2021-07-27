from PyQt5.QtWidgets import QDialog

import conf, screen_functions
from UI import Ui_quiz_selected

class QuizSelected:
    def __init__(self) -> None:
        self.dig = QDialog()
        self.ui = Ui_quiz_selected()
        self.ui.setupUi(self.dig)
        
        self.ui.back.clicked.connect(lambda:self.back())
        self.ui.start_quiz.clicked.connect(lambda: self.start_quiz())
        
    def back(self):
        conf.STACK.setCurrentWidget(conf.SCREENS_WIDGETS['quiz_list_scr'])
        
    def start_quiz(self):
        screen_functions.welcome_scr(conf.CONFIG['Welcome'])
        conf.STACK.setCurrentWidget(conf.SCREENS_WIDGETS['welcome_scr'])
        