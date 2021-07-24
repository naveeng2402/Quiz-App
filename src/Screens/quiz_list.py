from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidgetItem

import conf, screen_functions
from UI import Ui_quiz_list

class QuizList():
    def __init__(self) -> None:
        self.dig = QDialog()
        self.ui = Ui_quiz_list()
        self.ui.setupUi(self.dig)
        
        for quiz in conf.QUIZ_LIST:
            item = QListWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(quiz)
            self.ui.quiz_lst_box.addItem(item)
        self.ui.quiz_lst_box.itemDoubleClicked.connect(lambda: self.quiz_selected())
    
    def quiz_selected(self):
        conf.set_quiz_constants(self.ui.quiz_lst_box.currentItem().text())
        screen_functions.quiz_selected_scr()
        conf.STACK.setCurrentWidget(conf.SCREENS_WIDGETS['quiz_selected_scr'])