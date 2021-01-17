import json
import sys
# from screeninfo import get_monitors
from PyQt5 import QtCore, QtWidgets, QtGui

from Welcome.Welcome import Welcome
from Teams.Teams_main import TeamsMain
from App.App_main import AppMain
from GeneralRules.generalRules import GeneralRules

def summa(): pass # This is used to ByPass the Esc button action that causes trouble

def Welcome_screen():

    # This function takes care of the welcome screen
    
    _data = data['Welcome'] # Extracting the data
    
    welcome_scr = Welcome(_data['Hosts'], _data['Topic'])
    widget.addWidget(welcome_scr.Dialog)
    
    # moving to next screen
    def welcome_btn():
        teams_screen()

    # By passing Esc key
    welcome_scr.esc = QtWidgets.QShortcut('Esc', welcome_scr.Dialog)
    welcome_scr.esc.activated.connect(summa)
    
    # connecting the button to move to next screen
    welcome_scr.Done_Button.clicked.connect(welcome_btn)
    
    # Adding StyleSheet
    welcome_scr.Dialog.setStyleSheet('''
                                     border-image: url(BG/Trans.png)
                                     ''')


def teams_screen():
    
    _data = data['Teams'] # Extracting the data
    
    # Setting up the StyleSheet for the background
    widget.setStyleSheet('''
                         border-image: url(BG/BG_blur.jpg)
                         ''')
    
    teams_scr = TeamsMain(_data['Team_Names'], _data['Players_NO'])

    widget.addWidget(teams_scr.Dialog)
    widget.setCurrentWidget(teams_scr.Dialog)


    # ByPassing Esc button
    teams_scr.esc = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), teams_scr.Dialog)
    teams_scr.esc.activated.connect(summa)
    

    def Done_Action():
        '''
        This function takes all the entered names of the participants and make it into a dictionary and appends it to the json data(does not alter the actual file but the imported data is altered)
        '''
        
        teams_scr.teams_info = {}
        
        for team in range(len(teams_scr.Teams)):
            
            for player in range(teams_scr.Player_no):
                
                # The path for the list is found using i.objectname as the list element, then it was changed to i.text()
                exec(f'''teams_scr.teams_info[teams_scr.Teams[team]] = [i.text() for i in teams_scr.tab_{team+1}.children()[1].children()[1].children()[2:]]''')
                
        # print(teams_scr.teams_info)
        
        data['Teams']['Teams_info'] = teams_scr.teams_info
        
        # moving to next screen
        general_rules()
        
        # print(json.dumps(data))
        # print()
        # print(data)
        
    # connecting the button to alter the data got from Json\data.json
    teams_scr.Done_Button.clicked.connect(Done_Action)
    
    # Adding StyleSheet
    teams_scr.Dialog.setStyleSheet('''
                                   border-image: url(BG/Trans.png)
                                   ''')
    teams_scr.Tab_frame


def App():
    
    widget.setStyleSheet('''
                         border-image: url(BG/BG_blur.jpg)
                         ''')
    
    teams_info = data['Teams']['Teams_info']
    round      = data['Rounds']
    _qns       = qns
    
    app_scr = AppMain(teams_info, round, _qns, color)
    
    app_scr.esc = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), app_scr.Dialog)
    app_scr.esc.activated.connect(summa)
    
    widget.addWidget(app_scr.Dialog)
    widget.setCurrentWidget(app_scr.Dialog)
    
    app_scr.Dialog.setStyleSheet('''
                                 border-image: url(BG/Trans.png)
                                 ''')
    app_scr.stackedWidget.setStyleSheet('''background-color: rgb(230,230,230)''')
    

def general_rules():
    def action():
        App()

    _general_rules = GeneralRules()
    _general_rules.Button.clicked.connect(action)

    widget.addWidget(_general_rules)
    widget.setCurrentWidget(_general_rules)
    
    _general_rules.esc = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), _general_rules)
    _general_rules.esc.activated.connect(summa)



if __name__ == '__main__':
    
    
    # Reading the main data file
    with open('Json/data.json') as f:
        data = json.load(f)
        
    # Reading the questions file
    with open('Json/qns.json') as f:
        qns = json.load(f)
        
    color = data['color']
    # print(color)

    # screen = get_monitors()[0]
    # max_x, max_y = (screen.width, screen.height)
        
            
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle('Quiz')
    widget.resize(400, 300)
    # widget.setMaximumSize(max_x, max_y)
    widget.setStyleSheet('''
                         border-image: url(BG/BG.jpg)
                         ''')
    # teams_screen()
    Welcome_screen()
    # screen = Welcome(data['Hosts'], data['Topic']).Dialog
    # widget.addWidget(screen)
    widget.setWindowIcon(QtGui.QIcon('Others/icon.svg'))
    widget.show()
    sys.exit(app.exec_())