import json, os
from PyQt5.QtWidgets import QApplication, QSizePolicy, QStackedWidget, QWidget


QUIZ_LIST:list
CONFIG:dict
QNS:dict

STACK:QStackedWidget
APP:QApplication
SCREENS_WIDGETS:dict = {}

size_Expanding:QSizePolicy.Policy = QSizePolicy.Expanding
size_Preferred:QSizePolicy.Policy = QSizePolicy.Preferred


def get_json_data(path) -> dict:
    with open(path) as f:
        data = json.load(f)
    return data

def screens_widgets(name:str, scr:QWidget) -> None:
    global SCREENS_WIDGETS
    SCREENS_WIDGETS[name] = scr

def set_widgets(app:QApplication, stack:QStackedWidget) -> None:
    global APP, STACK
    APP = app
    STACK = stack
    
def set_prelim_constants()-> None:
    global QUIZ_LIST
    
    QUIZ_LIST = get_json_data(os.path.join('data', 'quiz_list.json'))['quiz-list']

def set_quiz_constants(quiz:str) -> None:
    global CONFIG, QNS
    
    # JSON Data
    CONFIG = get_json_data(os.path.join('data', quiz, 'config.json'))
    QNS = get_json_data(os.path.join('data', quiz, 'qns.json'))
    
def set_style_sheet(app:QApplication, ss_path:str)-> None:
    with open(ss_path) as f:
        ss = f.read()
    app.setStyleSheet(ss)
    
def dummy():
    pass