"""
This file is resposible for the second screen of the application

Features:
    The Teams screen is where the teams are declared
    The names of the teams and the number of members in the each teams is known by reading the Json\qns.json file
    The code programatically genreates all the necessary widgets to Enter the names of the members of each teams
    The code also adds the data to the imported json data (does not modifies the actual json file)
    The programatic generation of widgets is done using Teams\Teams_gen.py file

Note: You can know more about editing the json file in the readme.md or readme.txt

"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Teams.Teams_gen import tabs_gen


class TeamsMain():
    
    def __init__(self, Teams, Player_no):
        '''
        This class is responsible for the Teams Screen

        Variables:
            Teams    : list:: containing names of all teams
            Player_no: int :: number of players in each team
        
        '''

        self.Dialog     = QtWidgets.QDialog()
        self.Player_no  = Player_no
        self.Teams      = Teams 
        
        self.setup()
        self.Dialog.show()
    
    def setup(self):
        '''
        This makes up the parent widgets and sets plot to programatically generate rest of the widgets
        '''
        
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(1920,1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dialog.sizePolicy().hasHeightForWidth())
        self.Dialog.setSizePolicy(sizePolicy)


        self.Dialog_grid = QtWidgets.QGridLayout(self.Dialog)
        self.Dialog_grid.setContentsMargins(3,3,3,3)
        self.Dialog_grid.setVerticalSpacing(0)
        self.Dialog_grid.setObjectName('Dialog_grid')
        
        self.Tab_frame = QtWidgets.QFrame(self.Dialog)
        self.Tab_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Tab_frame.setContentsMargins(9,9,9,0)
        # self.Tab_frame.setStyleSheet('''background-color: rgba(255,255,255,30)''')
        self.Dialog_grid.addWidget(self.Tab_frame,0,1)     
        
        self.Tab_grid = QtWidgets.QGridLayout(self.Tab_frame)
        self.Tab_grid.setObjectName('Tab_grid') 
        
        self.Button_frame = QtWidgets.QFrame(self.Dialog)
        self.Button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Dialog_grid.addWidget(self.Button_frame,1,1)
        
        self.Button_grid = QtWidgets.QGridLayout(self.Button_frame)
        self.Button_grid.setContentsMargins(0,2,2,5)
        self.Button_grid.setObjectName('Button_grid')
        
        self.Done_Button = QtWidgets.QPushButton(self.Button_frame)
        self.Done_Button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))
        self.Done_Button.setMinimumHeight(50)
        self.Done_Button.setText('Done')
        Font = QtGui.QFont()
        Font.setPointSize(20)
        self.Done_Button.setFont(Font)
        self.Button_grid.addWidget(self.Done_Button,0,1)
        
        self.Button_spacer_left = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Expanding)
        self.Button_grid.addItem(self.Button_spacer_left, 0,0)

        self.Button_spacer_right = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Expanding)
        self.Button_grid.addItem(self.Button_spacer_right, 0,2)

        tabs_gen(self, player_no = self.Player_no,  Teams= self.Teams, source ='self.Tab_frame', layout = 'self.Tab_grid')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    ui = TeamsMain(['Team A', 'Team B', 'Team C'] , 6)
    # Dialog.show()
    sys.exit(app.exec_())