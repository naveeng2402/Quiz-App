from PyQt5 import QtCore, QtGui, QtWidgets
from Names import tabs_gen


class Ui_Dialog():
    
    def __init__(self, Dialog, Teams, Teams_no, Player_no):
        self.Dialog     = Dialog
        self.Player_no  = Player_no
        self.Teams      = Teams
        self.Teams_no   = Teams_no
        
        
        self.setup()
    
    def setup(self):
        
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(689, 518)
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

        tabs_gen(self, team_no = self.Teams_no, player_no = self.Player_no,  Teams= self.Teams, source ='self.Tab_frame', layout = 'self.Tab_grid')

        self.Done_Button.clicked.connect(self.Done_Action)
        
    def Done_Action(self):
        
        teams_info = {}
        
        for i in range(self.Teams_no):
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog, ['Team A', 'Team B', 'Team C'], 3, 6)
    Dialog.show()
    sys.exit(app.exec_())