from PyQt5.QtWidgets import QStackedWidget
from Screens.quiz_selected import QuizSelected
from Screens.teams import Teams
from Screens.welcome import Welcome

import conf
from Screens import *

def quiz_list_scr():
    scr = QuizList()
    scr.dig.show()
    
    conf.STACK.addWidget(scr.dig)
    conf.screens_widgets("quiz_list_scr", scr.dig)
    
def quiz_selected_scr():
    scr = QuizSelected()
    scr.dig.show()
    
    conf.STACK.addWidget(scr.dig)
    conf.screens_widgets("quiz_selected_scr", scr.dig)
    
def welcome_scr(data:dict):
    scr = Welcome(data)
    scr.dig.show()
    
    conf.STACK.addWidget(scr.dig)
    conf.screens_widgets('welcome_scr', scr.dig)
    
def teams_scr(data:dict):
    scr = Teams(data)
    scr.dig.show()
    
    conf.STACK.addWidget(scr.dig)
    conf.screens_widgets('teams_scr', scr.dig)
    