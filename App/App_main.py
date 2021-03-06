"""
This file is resposible for the main screen of the application

Features:
    The App screen is the main screen the user uses
    Using the data in the Json\data.json file, the script generates the scoring part, navigation part, interaction part and a table of scores
    The questions are generated using Json\qns.json file

Note: You can know more about editing the json file in the readme.md or readme.txt

"""

from PyQt5 import QtWidgets, QtCore, QtGui
from time import sleep
from App.App_gen import Scoring_gen, Modify_scroing, TeamTableGen, Scoring_Actions, Score_Table_gen, Navig_gen, Questions_gen, Navig_connect, Qn_Connect, scores, Timer_Connect

class AppMain():
    
    def __init__(self, Teams_info: dict = {'Team A': ['Naveen1','Naveen2', 'Naveen_A'], 'Team B': ['Naveen3', 'Naveen4', 'Naveen_B'], 'Team C': ['Naveen5', 'Naveen6', 'Naveen_C']}, rounds = {}, qns = {}, color = False):
        self.Dialog = QtWidgets.QDialog()
        self.color = color
        # Getting the values and making datastructures
        self.Team_Info      = Teams_info
        self.rounds_Info    = rounds
        
        self.Team_Names = sorted(list(self.Team_Info.keys()))
        self._Team_Names = ['_'.join(i.split()) for i in self.Team_Names]
        
        self.Round_Names = sorted(list(self.rounds_Info.keys()))
        self._Round_Names= ['_'.join(i.split()) for i in self.Round_Names]
        
        self.qns = qns
        
        self.score = {}
        for i in self._Team_Names: self.score[i] = 0
        self.s_Tick = 0
        self.s_Plus = 0
        self.s_Minus= 0
        self.TimerControl = False
        
        # print(self.Team_Names)
        # print(self._Team_Names)
        # print(self.Team_Info)
        # print(self.rounds_Info)
        # print(self.Round_Names)
        # print(self._Round_Names)
        # print(self.score)
        
        self.setup()
        self.Dialog.show()
        
    def setup(self):
        self.Dialog.setObjectName('Dialog')
        self.Dialog.resize(500,500)
        
        self.Dialog_grid = QtWidgets.QGridLayout(self.Dialog)
        self.Dialog_grid.setObjectName("Dialog_grid")
        
        self.Dig_frame = QtWidgets.QFrame(self.Dialog)
        self.Dig_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Dig_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Dig_frame.setObjectName("Dig_frame")    
        self.Dialog_grid.addWidget(self.Dig_frame)
        
        self.Dig_frame_grid = QtWidgets.QGridLayout(self.Dig_frame) 
        self.Dig_frame_grid.setObjectName("Dig_frame_grid")
        
        self.Root_Splitter = QtWidgets.QSplitter(self.Dig_frame)
        self.Root_Splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Root_Splitter.setObjectName("Root_Splitter")
        self.Dig_frame_grid.addWidget(self.Root_Splitter)
        
        
        self.teamTable = QtWidgets.QTableWidget(self.Root_Splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamTable.sizePolicy().hasHeightForWidth())
        self.teamTable.setSizePolicy(sizePolicy)
    
        self.teamTable.setMinimumSize(QtCore.QSize(0, 0))
        self.teamTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teamTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teamTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.teamTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.teamTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.teamTable.setAlternatingRowColors(False)
        self.teamTable.setSortingEnabled(True)
        self.teamTable.setObjectName("teamTable")
        self.teamTable.horizontalHeader().setStretchLastSection(True)
        self.teamTable.verticalHeader().setStretchLastSection(True)
        
        TeamTableGen(self, _teams = self._Team_Names, teams = self.Team_Names, teams_info=self.Team_Info)
                
        self.Main_splitter = QtWidgets.QSplitter(self.Root_Splitter)
        self.Main_splitter.setOrientation(QtCore.Qt.Vertical)
        self.Main_splitter.setObjectName("Main_splitter")  

        self.Scoring = QtWidgets.QScrollArea(self.Main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Scoring.sizePolicy().hasHeightForWidth())
        self.Scoring.setSizePolicy(sizePolicy)
        self.Scoring.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Scoring.setWidgetResizable(True)
        self.Scoring.setObjectName("Scoring")
        
        self.Scoring_Contents = QtWidgets.QWidget()
        self.Scoring_Contents.setGeometry(QtCore.QRect(-239, 0, 867, 60))
        self.Scoring_Contents.setObjectName("Scroing_Contents")
        self.Scoring.setWidget(self.Scoring_Contents)
        
        self.Scoring_Layout = QtWidgets.QHBoxLayout(self.Scoring_Contents)
        self.Scoring_Layout.setSpacing(25)
        self.Scoring_Layout.setObjectName("Scoring_Layout")     
        
        # self.S_trigger()      
      
        Scoring_gen(self,teams = self.Team_Names, _teams=self._Team_Names, source='self.Scoring_Contents', layout= 'self.Scoring_Layout')
 
        if self.s_Minus < 0: 
            Modify_scroing(self, self._Team_Names, 'a')
        else: 
            try :Modify_scroing(self,self._Team_Names, 'r')
            except : pass
            
        # self.Tab_frame = QtWidgets.QFrame(self.Main_splitter)
        # self.Tab_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.Tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.Tab_frame.setObjectName("Tab_frame")
        
        # self.Tab_frame_Layout = QtWidgets.QVBoxLayout(self.Tab_frame)
        # self.Tab_frame_Layout.setContentsMargins(0, 0, 0, 0)
        # self.Tab_frame_Layout.setObjectName("Tab_frame_Layout")
            
        self.tableWidget = QtWidgets.QTableWidget(self.Main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
    
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

                
        Score_Table_gen(self, _teams = self._Team_Names, teams = self.Team_Names, teams_info=self.Team_Info)
        
        # self.end_button = QtWidgets.QPushButton("END QUIZ",self.Tab_frame)
        # self.Tab_frame_Layout.addWidget(self.end_button)
        self.end = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.SHIFT+QtCore.Qt.Key_Escape), self.Dialog)
        
        Scoring_Actions(self)
        # self.Main_splitter.setSizes([1,0])
        

        self.App_frame = QtWidgets.QFrame()
        self.App_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.App_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.App_frame.setObjectName("App_frame")
        self.Main_splitter.insertWidget(1, self.App_frame)
        
        self.App_frame_Layout = QtWidgets.QHBoxLayout(self.App_frame)
        self.App_frame_Layout.setContentsMargins(0, 0, 0, 0)
        self.App_frame_Layout.setObjectName("App_frame_Layout")

        self.App_splitter = QtWidgets.QSplitter(self.App_frame)      
        self.App_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.App_splitter.setObjectName("App_splitter")
        self.App_frame_Layout.addWidget(self.App_splitter)
        
        
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.App_splitter)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        
        
        Questions_gen(self, self.qns, self.Round_Names, self._Round_Names, self.rounds_Info)
        
        
        self.Navigation = QtWidgets.QScrollArea(self.App_splitter)
        self.Navigation.setMinimumSize(QtCore.QSize(195, 0))
        self.Navigation.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Navigation.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Navigation.setWidgetResizable(True)
        self.Navigation.setObjectName("Navigation")
        self.Navigation_Contents = QtWidgets.QWidget()
        self.Navigation_Contents.setGeometry(QtCore.QRect(0, 0, 187, 473))
        self.Navigation_Contents.setObjectName("Navigation_Contents")
        self.Navigation.setWidget(self.Navigation_Contents)
        
        self.Navigation_Layout = QtWidgets.QGridLayout(self.Navigation_Contents)
        self.Navigation_Layout.setObjectName("Navigation_Layout")
        
        Navig_gen(self, self.rounds_Info, self.Round_Names, self._Round_Names)
        
        Timer_Connect(self, self.Round_Names, self._Round_Names, self.rounds_Info, self.qns)
      
        Navig_connect(self, self._Round_Names)
        
        Qn_Connect(self,self.Round_Names, self._Round_Names, self.rounds_Info, self.qns)
        
        scores(self, self.rounds_Info)
        
        
        
        # for i in self.stackedWidget.children(): print(i.objectName())
        
            
    # def S_trigger(self):
    #     self.s = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self.Dialog)
    #     self.s.activated.connect(self.action)
    # def action(self):

    #     # #  Action for Scoring
    #     # self.s_Minus = -10
    #     if self.s_Minus < 0: Modify_scroing(self, self._Team_Names, 'a')
    #     else: 
    #         try : Modify_scroing(self, self._Team_Names, 'r')
    #         except : pass
    #     # # Action for display score
    #     # for i in self.score.keys(): self.score[i] = self.score.get(i) + self.s_Minus
    #     # print(self.score)
    #     # Modify_Disp_Score(self, score= self.score)
    #     pass









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # rounds = ['Round 1', 'Round 2']
    rounds= {
            "Round 1":
                {
                    "nos"   : 1,
                    # "tag"   : "HTML",
                    "rules" : '<p style="text-align: center;">\n<span style="color: #ff0000; background-color: #ffff00;">Rules for Round 1</span>\n</p>',
                    "tick"  : 10,
                    "plus"  : 5,
                    "minus" : 0,
                    "time"  : 3
                },

            "Round 2":
                {
                    "nos"   : 1,
                    # "tag"   : "HTML",
                    "rules" : "Rules for Round 2",
                    "tick"  : 50,
                    "plus"  : 25,
                    "minus" : -10,
                    "time"  : 45
                }
            }

    qns   = \
            {
            "Round_1_Q1" : 
                {
                    # "tag"     : "HTML",
                    "content" : "<h1>Q1\n</span>\n</h1>",
                    "options" : ["a1", "b1", "c1"],
                    "answer"  : "c1",
                    "explain" : "<p><img style='display: block; margin-left: auto; margin-right: auto;' src='Kratos_Axe_Square.jpg' alt='axe width='100' height='100' /></p>"
                },
            "Round_2_Q1" : 
                {
                    # "tag"     : "HTML",
                    "content" : "<h1>Q2\n</span>\n</h1>",
                    "options" : ["a2", "b2", "c2"],
                    "answer"  : "b2",
                    "explain" : "Q2 Explaination"
                }
           }
            
            
    
    
    ui = AppMain(rounds= rounds, qns= qns)
    sys.exit(app.exec_())