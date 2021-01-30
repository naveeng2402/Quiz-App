from PyQt5 import QtWidgets, QtCore, QtGui
from playsound import playsound
from threading import Thread
from random import randint
from time import sleep

def Scoring_gen(self, teams, _teams, source, layout):
    
    for i in range(len(teams)):
        
        exec(f'''self.{_teams[i]}_Scoring = QtWidgets.QFrame({source})''')
        eval(f'''self.{_teams[i]}_Scoring.setFrameShape(QtWidgets.QFrame.NoFrame)''')
        eval(f'''self.{_teams[i]}_Scoring.setFrameShadow(QtWidgets.QFrame.Raised)''')
        eval(f'''self.{_teams[i]}_Scoring.setObjectName("{_teams[i]}_Scoring")''')
        # print(self.color)
        if self.color is True:
            eval(f'''self.{_teams[i]}_Scoring.setStyleSheet("background-color:hsv({randint(0,350)}, 255, 255);color:rgb(255,255,255)")''')
        
        exec(f'''self.{_teams[i]}_Scoring_Layout = QtWidgets.QGridLayout(self.{_teams[i]}_Scoring)''')
        eval(f'''self.{_teams[i]}_Scoring_Layout.setContentsMargins(0, 0, 0, 0)''')
        eval(f'''self.{_teams[i]}_Scoring_Layout.setHorizontalSpacing(5)''')
        eval(f'''self.{_teams[i]}_Scoring_Layout.setVerticalSpacing(0)''')
        eval(f'''self.{_teams[i]}_Scoring_Layout.setObjectName("{_teams[i]}_Scoring_Layout")''')
        
        exec(f'''self.{_teams[i]}_Tick = QtWidgets.QPushButton(self.{_teams[i]}_Scoring)''')
        exec('''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)''')
        eval('''sizePolicy.setHorizontalStretch(0)''')
        eval('''sizePolicy.setVerticalStretch(0)''')
        eval(f'''sizePolicy.setHeightForWidth(self.{_teams[i]}_Tick.sizePolicy().hasHeightForWidth())''')
        eval(f'''self.{_teams[i]}_Tick.setSizePolicy(sizePolicy)''')
        eval(f'''self.{_teams[i]}_Tick.setText('')''')
        exec('''icon = QtGui.QIcon()''')
        eval('''icon.addFile('Images/Tick.svg')''')
        eval(f'''self.{_teams[i]}_Tick.setIcon(icon)''')
        eval(f'''self.{_teams[i]}_Tick.setIconSize(QtCore.QSize(20,20))''')
        eval(f'''self.{_teams[i]}_Tick.setObjectName("{_teams[i]}_Tick")''')
        eval(f'''self.{_teams[i]}_Scoring_Layout.addWidget(self.{_teams[i]}_Tick, 1, 0, 1, 1)''')
        
        exec(f'''self.{_teams[i]}_Plus = QtWidgets.QPushButton(self.{_teams[i]}_Scoring)''')
        exec(f'''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)''')
        eval('''sizePolicy.setHorizontalStretch(0)''')
        eval(f'''sizePolicy.setVerticalStretch(0)''')
        eval(f'''sizePolicy.setHeightForWidth(self.{_teams[i]}_Plus.sizePolicy().hasHeightForWidth())''')
        eval(f'''self.{_teams[i]}_Plus.setSizePolicy(sizePolicy)''')
        eval(f'''self.{_teams[i]}_Plus.setText('')''')
        exec('''icon = QtGui.QIcon()''')
        eval('''icon.addFile('Images/Plus.svg')''')
        eval(f'''self.{_teams[i]}_Plus.setIcon(icon)''')
        eval(f'''self.{_teams[i]}_Plus.setIconSize(QtCore.QSize(20,20))''')
        eval(f'''self.{_teams[i]}_Plus.setObjectName("{_teams[i]}_Plus")''')
        eval(f'''self.{_teams[i]}_Scoring_Layout.addWidget(self.{_teams[i]}_Plus, 1, 1, 1, 1)''')
        
        font = QtGui.QFont()
        font.setBold(True)
        exec(f'''self.{_teams[i]}_Label = QtWidgets.QLabel(self.{_teams[i]}_Scoring)''')
        eval(f'''self.{_teams[i]}_Label.setAlignment(QtCore.Qt.AlignCenter)''')
        eval(f'''self.{_teams[i]}_Label.setFont(font)''')
        eval(f'''self.{_teams[i]}_Label.setText('{teams[i]}')''')
        eval(f'''self.{_teams[i]}_Label.setObjectName("{_teams[i]}_Label")''')
    
        eval(f'''self.{_teams[i]}_Scoring_Layout.addWidget(self.{_teams[i]}_Label, 0, 0, 1, 2)''')
        
        eval(f'''{layout}.addWidget(self.{_teams[i]}_Scoring)''')
    

def Modify_scroing(self, _teams, flag): # flag 'a' is for adding and 'r' for removing
    
    if flag == 'a':
        for i in range(len(_teams)):
            exec(f'''self.{_teams[i]}_Cross = QtWidgets.QPushButton(self.{_teams[i]}_Scoring)''')
            exec(f'''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)''')
            eval('''sizePolicy.setHorizontalStretch(0)''')
            eval(f'''sizePolicy.setVerticalStretch(0)''')
            eval(f'''sizePolicy.setHeightForWidth(self.{_teams[i]}_Cross.sizePolicy().hasHeightForWidth())''')
            eval(f'''self.{_teams[i]}_Cross.setSizePolicy(sizePolicy)''')
            eval(f'''self.{_teams[i]}_Cross.setText('')''')
            exec('''icon = QtGui.QIcon()''')
            eval('''icon.addFile('Images/Cross.svg')''')
            eval(f'''self.{_teams[i]}_Cross.setIcon(icon)''')
            eval(f'''self.{_teams[i]}_Cross.setIconSize(QtCore.QSize(20,20))''')
            eval(f'''self.{_teams[i]}_Cross.setObjectName("{_teams[i]}_Cross")''')
            eval(f'''self.{_teams[i]}_Scoring_Layout.addWidget(self.{_teams[i]}_Cross, 1, 2, 1, 1)''')

            eval(f'''self.{_teams[i]}_Scoring_Layout.addWidget(self.{_teams[i]}_Label, 0, 0, 1, 3)''')
    
        Cross_connect(self)
    
    if flag == 'r':
        for i in range(len(_teams)):
            eval(f'''self.{_teams[i]}_Cross.deleteLater()''')
            eval(f'''self.{_teams[i]}_Scoring_Layout.addWidget(self.{_teams[i]}_Label, 0, 0, 1, 2)''')


def Scoring_Actions(self):   
    self.s_Tick +=0
    
    ticks = []
    pluss = []
    
    for i in self.Scoring_Contents.children()[1:]:
        # print(i.objectName())
        for j in i.children()[1:]:
            # print(j.objectName())
            if 'Tick' in j.objectName(): ticks.append(j)
            if 'Plus' in j.objectName(): pluss.append(j)
    # print([i.objectName() for i in ticks])
    
    for i in range(len(ticks)):
        
        ticks[i].clicked.connect(lambda _, i=i: Tick_Clicked(self, ticks[i].objectName()[:-5], self.score, self.s_Tick))
        pluss[i].clicked.connect(lambda _, i=i: Plus_Clicked(self, pluss[i].objectName()[:-5], self.score, self.s_Plus))
 

def Tick_Clicked(self, _team : str, score, tick):

    # print(score)
    score[_team] += tick 
    Modify_Disp_Score(self, score)
    # print(f'{_team} Tick_Clicked''')
    
def Plus_Clicked(self, _team, score, plus):
    score[_team] += plus
    Modify_Disp_Score(self, score)
    # print(f'{_team} Plus_Clicked')
                
def Cross_Clicked(self,_team,score,minus):
    score[_team] += minus
    Modify_Disp_Score(self, score)
    # print(f'''{_team} Cross_Clicked''')


def Cross_connect(self):
    crosss = []
    for i in self.Scoring_Contents.children()[1:]:
        for j in i.children()[1:]: 
            if 'Cross' in j.objectName(): crosss.append(j)
    
    for i in range(len(crosss)):
        crosss[i].clicked.connect(lambda _, i=i: Cross_Clicked(self, crosss[i].objectName()[:-6], self.score, self.s_Minus))




def Table_gen(self, _teams, teams, teams_info):
    
    def headers():
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(teams))
        
        for i in range(2):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem().setTextAlignment(QtCore.Qt.AlignCenter))
        self.tableWidget.setHorizontalHeaderLabels(['Teams', 'Members', 'Score'])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(2, 10)

        for i in range(len(_teams)):
            self.tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem().setTextAlignment(QtCore.Qt.AlignCenter))
            self.tableWidget.setRowHeight(i,100)
        self.tableWidget.setVerticalHeaderLabels(['' for i in range(len(_teams))])
     
    def teams_fill():
        for i in range(len(teams)):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(teams[i])
            self.tableWidget.setItem(i, 0, item)
        
    def memebers():
        
        for i in range(len(teams)):
        
            membs = ', '.join(teams_info[teams[i]])
        
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(membs)
            self.tableWidget.setItem(i, 1, item)
        
    def score():
        for i in range(len(teams)):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText('0')
            exec(f'''self.{_teams[i]}_score_disp = item''')
            self.tableWidget.setItem(i, 2, item)
    
    headers()
    teams_fill()
    memebers()
    score()
    
def Modify_Disp_Score(self, score):
    
    for i in self._Team_Names:
        eval(f'''self.{i}_score_disp.setText('{score[i]}')''')



def Navig_gen(self, rounds_info, rounds, _rounds):
    
    row = -1
    for i in range(len(rounds)):
        
        row += 1
        exec(f'''self.{_rounds[i]} = QtWidgets.QPushButton(self.Navigation_Contents)''')
        eval(f'''self.{_rounds[i]}.setMinimumHeight(30)''')
        # eval(f'''self.{_rounds[i]}.setmi''')
        eval(f'''self.{_rounds[i]}.setText('{rounds[i]}')''')
        eval(f'''self.{_rounds[i]}.setObjectName("{_rounds[i]}")''')
        eval(f'''self.{_rounds[i]}.setStyleSheet(\'\'\'border: 2px dashed black\'\'\')''')
        eval(f'''self.Navigation_Layout.addWidget(self.{_rounds[i]}, {row}, 0, 1, 3)''')
        for j in range(rounds_info[rounds[i]]['nos']):
            if j%3 == 0: row += 1
            exec(f'''self.{_rounds[i]}_Q{j+1} = QtWidgets.QPushButton(self.Navigation_Contents)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}.setText('Q {j+1}')''')
            eval(f'''self.{_rounds[i]}_Q{j+1}.setMinimumSize(50, 50)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}.setObjectName("{_rounds[i]}_Q{j+1}")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}.setStyleSheet(\'\'\'QPushButton::!hover
                                                                    {{
                                                                    border-radius:25px;
                                                                    border : 2px solid black;
                                                                    }}

                                                                    QPushButton::hover
                                                                    {{
                                                                    border-radius:25px;
                                                                    border : 4px solid black;
                                                                    }}

                                                                    QPushButton::pressed
                                                                    {{	
                                                                    border-radius:20px;
                                                                    border : 4px solid black;
                                                                    background-color: rgb(100, 100, 100);
                                                                    color: rgb(255, 255, 255);
                                                                    }}\'\'\')''')
            
            eval(f'''self.Navigation_Layout.addWidget(self.{_rounds[i]}_Q{j+1}, {row}, {j%3}, 1, 1)''')
        # Generating Space Between Rounds
        row += 1
        exec(f'''self.{_rounds[i]}_spacer = QtWidgets.QLabel(self.Navigation_Contents)''')
        eval(f'''self.{_rounds[i]}_spacer.setMinimumHeight(20)''')
        eval(f'''self.{_rounds[i]}_spacer.setObjectName('{_rounds[i]}_spacer')''')
        eval(f'''self.Navigation_Layout.addWidget(self.{_rounds[i]}_spacer, {row}, 0, 1, 3) ''')
        
        
        

def Questions_gen(self, qns, rounds, _rounds, rounds_info):
    
    for i in range(len(_rounds)):
        
        exec(f'''self.{_rounds[i]}_Info = QtWidgets.QWidget()''')
        eval(f'''self.{_rounds[i]}_Info.setObjectName("{_rounds[i]}_Info")''')
        eval(f'''self.stackedWidget.addWidget(self.{_rounds[i]}_Info)''')
        
        exec(f'''self.{_rounds[i]}_Info_Layout = QtWidgets.QVBoxLayout(self.{_rounds[i]}_Info)''')
        eval(f'''self.{_rounds[i]}_Info_Layout.setObjectName('{_rounds[i]}_Info_Layout')''')
        
        exec(f'''self.{_rounds[i]}_Info_Label = QtWidgets.QLabel('Round {i+1}', self.{_rounds[i]}_Info)''')
        eval(f'''self.{_rounds[i]}_Info_Label.setAlignment(QtCore.Qt.AlignCenter)''')
        eval(f'''self.{_rounds[i]}_Info_Label.setObjectName('{_rounds[i]}_Info_Label')''')
        eval(f'''self.{_rounds[i]}_Info_Layout.addWidget(self.{_rounds[i]}_Info_Label)''')
        
        exec(f'''self.{_rounds[i]}_Rules = QtWidgets.QTextBrowser(self.{_rounds[i]}_Info)''')
        eval(f'''self.{_rounds[i]}_Rules.setObjectName("{_rounds[i]}_Rules")''')
        eval(f'''self.{_rounds[i]}_Rules.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)''')
        eval(f'''self.{_rounds[i]}_Rules.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)''')
        eval(f'''self.{_rounds[i]}_Rules.setText(rounds_info['{rounds[i]}']['rules'])''')
        eval(f'''self.{_rounds[i]}_Info_Layout.addWidget(self.{_rounds[i]}_Rules)''')
        
        exec(f'''self.{_rounds[i]}_Info_Button = QtWidgets.QPushButton('Start Round {i+1}', self.{_rounds[i]}_Info)''')
        eval(f'''self.{_rounds[i]}_Info_Button.setObjectName("{_rounds[i]}_Info_Button")''')
        eval(f'''self.{_rounds[i]}_Info_Layout.addWidget(self.{_rounds[i]}_Info_Button)''')
        
               
        for j in range(rounds_info[rounds[i]]['nos']):
            
            options = qns[_rounds[i]+'_Q'+str(j+1)]['options']
            qn      = qns[_rounds[i]+'_Q'+str(j+1)]['content']
            # tag     = qns[_rounds[i]+'_Q'+str(j+1)]['tag']
            ans     = qns[_rounds[i]+'_Q'+str(j+1)]['answer']
            exp     = qns[_rounds[i]+'_Q'+str(j+1)]['explain']
            # print(f'Aswers {ans}')
            
            # print(options, qn, tag, ans)

            exec(f'''self.{_rounds[i]}_Q{j+1}_Widget = QtWidgets.QWidget()''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Widget.setContentsMargins(0,0,0,0)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Widget.setObjectName('{_rounds[i]}_Q{j+1}_Widget')''')
            eval(f'''self.stackedWidget.addWidget(self.{_rounds[i]}_Q{j+1}_Widget)''')
            

            exec(f'''self.{_rounds[i]}_Q{j+1}_Widget_Layout = QtWidgets.QGridLayout(self.{_rounds[i]}_Q{j+1}_Widget)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Widget_Layout.setObjectName('{_rounds[i]}_Q{j+1}_Widget_Layout')''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_Splitter = QtWidgets.QSplitter(self.{_rounds[i]}_Q{j+1}_Widget)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Splitter.setOrientation(QtCore.Qt.Vertical)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Splitter.setObjectName("{_rounds[i]}_Q{j+1}_Splitter")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Widget_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_Splitter)''')


            exec(f'''self.{_rounds[i]}_Q{j+1}_Question = QtWidgets.QFrame(self.{_rounds[i]}_Q{j+1}_Splitter)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question.setFrameShape(QtWidgets.QFrame.NoFrame)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question.setContentsMargins(0,0,0,0)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question.setFrameShadow(QtWidgets.QFrame.Raised)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question.setObjectName("{_rounds[i]}_Q{j+1}_Question")''')
            
            exec(f'''self.{_rounds[i]}_Q{j+1}_Question_Layout = QtWidgets.QGridLayout(self.{_rounds[i]}_Q{j+1}_Question)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question_Layout.setObjectName("{_rounds[i]}_Q{j+1}_Question_Layout")''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_Timer = QtWidgets.QLabel(self.{_rounds[i]}_Q{j+1}_Question)''')
            exec(f'''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)''')
            eval(f'''sizePolicy.setHorizontalStretch(0)''')
            eval(f'''sizePolicy.setVerticalStretch(0)''')
            eval(f'''sizePolicy.setHeightForWidth(self.{_rounds[i]}_Q{j+1}_Timer.sizePolicy().hasHeightForWidth())''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Timer.setSizePolicy(sizePolicy)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Timer.setMinimumSize(QtCore.QSize(60, 30))''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Timer.setStyleSheet(\'\'\'border : 2px solid black;                                                                            
                                                                    border-radius : 15px\'\'\')''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Timer.setAlignment(QtCore.Qt.AlignCenter)''')
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(20)
            eval(f'''self.{_rounds[i]}_Q{j+1}_Timer.setFont(font)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Timer.setObjectName("{_rounds[i]}_Q{j+1}_Timer")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_Timer, 0, 1, 1, 1)''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_Spacer_Left = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question_Layout.addItem(self.{_rounds[i]}_Q{j+1}_Spacer_Left, 0, 0, 1, 1)''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_Spacer_Right = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Question_Layout.addItem(self.{_rounds[i]}_Q{j+1}_Spacer_Right, 0, 2, 1, 1)''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox = QtWidgets.QTextBrowser(self.{_rounds[i]}_Q{j+1}_Question)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox.setObjectName("{_rounds[i]}_Q{j+1}_QuestionBox")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox.setContentsMargins(0,0,0,0)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox.setAlignment(QtCore.Qt.AlignCenter)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox.setText(qn)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_QuestionBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)''')

            eval(f'''self.{_rounds[i]}_Q{j+1}_Question_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_QuestionBox, 1, 0, 1, 3)''')


            exec(f'''self.{_rounds[i]}_Q{j+1}_Option = QtWidgets.QFrame(self.{_rounds[i]}_Q{j+1}_Splitter)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Option.setFrameShape(QtWidgets.QFrame.NoFrame)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Option.setFrameShadow(QtWidgets.QFrame.Raised)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Option.setObjectName("{_rounds[i]}_Q{j+1}_Option")''')
            
            exec(f'''self.{_rounds[i]}_Q{j+1}_Option_Layout = QtWidgets.QGridLayout(self.{_rounds[i]}_Q{j+1}_Option)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Option_Layout.setObjectName("{_rounds[i]}_Q{j+1}_Option_Layout")''')

            # The options check buttons has lower case o in its name and else has upper case O in their names

            for k in range(len(options)):
                exec(f'''self.{_rounds[i]}_Q{j+1}_option_{k+1} = QtWidgets.QRadioButton(self.{_rounds[i]}_Q{j+1}_Option)''')
                exec(f'''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)''')
                eval(f'''self.{_rounds[i]}_Q{j+1}_option_{k+1}.setSizePolicy(sizePolicy)''')
                eval(f'''self.{_rounds[i]}_Q{j+1}_option_{k+1}.setCheckable(True)''')
                eval(f'''self.{_rounds[i]}_Q{j+1}_option_{k+1}.setText('{options[k]}')''')
                eval(f'''self.{_rounds[i]}_Q{j+1}_option_{k+1}.setStyleSheet(\'\'\'
                                                                            QRadioButton::checked
                                                                            {{
                                                                            background-color: blue;
                                                                            color: white
                                                                            }}
                                                                            \'\'\')''')
                eval(f'''self.{_rounds[i]}_Q{j+1}_option_{k+1}.setObjectName("{_rounds[i]}_Q{j+1}_option_{k+1}")''')
                eval(f'''self.{_rounds[i]}_Q{j+1}_Option_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_option_{k+1}, {k}, 0, 1, 2)''')

                # Timer Button
            exec(f'''self.{_rounds[i]}_Q{j+1}_Start_Timer = QtWidgets.QPushButton(self.{_rounds[i]}_Q{j+1}_Option)''')
            exec(f'''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)''')
            eval('''sizePolicy.setHorizontalStretch(0)''')
            eval(f'''sizePolicy.setVerticalStretch(0)''')
            eval(f'''sizePolicy.setHeightForWidth(self.{_rounds[i]}_Q{j+1}_Start_Timer.sizePolicy().hasHeightForWidth())''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Start_Timer.setSizePolicy(sizePolicy)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Start_Timer.setText('Start Timer')''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Start_Timer.setObjectName("{_rounds[i]}_Q{j+1}_Start_Timer")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Option_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_Start_Timer, {len(options)}, 0, 1, 1)''')
            
            
            exec(f'''self.{_rounds[i]}_Q{j+1}_Check_Answer = QtWidgets.QPushButton(self.{_rounds[i]}_Q{j+1}_Option)''')
            exec(f'''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)''')
            eval('''sizePolicy.setHorizontalStretch(0)''')
            eval(f'''sizePolicy.setVerticalStretch(0)''')
            eval(f'''sizePolicy.setHeightForWidth(self.{_rounds[i]}_Q{j+1}_Check_Answer.sizePolicy().hasHeightForWidth())''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Check_Answer.setSizePolicy(sizePolicy)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Check_Answer.setText('Check Answer')''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Check_Answer.setObjectName("{_rounds[i]}_Q{j+1}_Check_Answer")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Option_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_Check_Answer, {len(options)}, 1, 1, 1)''')                

            exec(f'''self.{_rounds[i]}_Q{j+1}_Explaination = QtWidgets.QFrame(self.{_rounds[i]}_Q{j+1}_Splitter)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination.setFrameShape(QtWidgets.QFrame.StyledPanel)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination.setContentsMargins(0,0,0,0)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination.setFrameShadow(QtWidgets.QFrame.Raised)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination.setObjectName("{_rounds[i]}_Q{j+1}_Explaination")''')
            
            exec(f'''self.{_rounds[i]}_Q{j+1}_Explaination_Layout = QtWidgets.QGridLayout(self.{_rounds[i]}_Q{j+1}_Explaination)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination_Layout.setObjectName("{_rounds[i]}_Q{j+1}_Explaination_Layout")''')                
            
            exec(f'''self.{_rounds[i]}_Q{j+1}_ExplainLabel = QtWidgets.QLabel(self.{_rounds[i]}_Q{j+1}_Explaination)''')
            exec(f'''font = QtGui.QFont()''')
            eval(f'''font.setPointSize(15)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_ExplainLabel.setFont(font)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_ExplainLabel.setAlignment(QtCore.Qt.AlignCenter)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_ExplainLabel.setText('Explaination')''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_ExplainLabel.setObjectName("{_rounds[i]}_Q{j+1}_ExplainLabel")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_ExplainLabel)''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_ExplainContent = QtWidgets.QTextBrowser(self.{_rounds[i]}_Q{j+1}_Explaination)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_ExplainContent.setText(exp)''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_ExplainContent.setObjectName("{_rounds[i]}_Q{j+1}_ExplainContent")''')
            eval(f'''self.{_rounds[i]}_Q{j+1}_Explaination_Layout.addWidget(self.{_rounds[i]}_Q{j+1}_ExplainContent)''')

            exec(f'''self.{_rounds[i]}_Q{j+1}_Splitter.setSizes([5, 4,0])''')
    

def Navig_connect(self, _rounds):

    infos = []
    tmp   = []
    qns   = []

    for i in self.Navigation_Contents.children():
        for j in self.stackedWidget.children():
            # print(i.objectName(), j.objectName())
            if i.objectName() in j.objectName() and 'Info' in j.objectName():
                infos.append((i,j))
            elif '_Q' in i.objectName() and i.objectName() in j.objectName() and 'Widget' in j.objectName():
                tmp.append((i, j))
                        
        for i in tmp:
            if i not in qns: qns.append(i)
                
    # print([(i[0].objectName(), i[1].objectName()) for i in qns])
    

    def connect(widget):
        self.stackedWidget.setCurrentWidget(widget)
    
    for k in infos:
        k[0].clicked.connect(lambda _, widget = k[1]: connect(widget))
        
    for k in qns:
        k[0].clicked.connect(lambda _, widget = k[1]: connect(widget))
    
    
    
def Qn_Connect(self, rounds, _rounds, rounds_info, qns):
                
    wids = [j for j in self.stackedWidget.children() if 'Widget' in j.objectName()]
    check_btn = []
    ans = {}
    for i in range(len(rounds)):
        for j in range(rounds_info[rounds[i]]['nos']):
            ans[_rounds[i]+'_Q'+str(j+1)] = qns[_rounds[i]+'_Q'+str(j+1)]['answer']


    for i in wids:
        for j in i.children()[1].children():
            if '_Option' in j.objectName():
                for k in j.children():
                    if '_Check_Answer' in k.objectName(): 
                        check_btn.append((j,k, ans['_'.join(j.objectName().split('_')[:-1])]))
                        
                        
    # print(ans)
    # print([(i[0].objectName(), i[1].objectName(),  i[2]) for i in check_btn])
    # for i in check_btn:
        # for j in i[0].children(): print(j.objectName())     
    def check(frame, ans):
        btns = [i for i in frame.children() if '_option_' in i.objectName()]
        # print('Inside Check')
        for i in btns:
            if i.isChecked() is True and i.text() == ans:
                # print('Correct') 
                i.setStyleSheet('''
                                QPushButton::checked
                                {
                                background-color: green;
                                color: white
                                }
                                ''')
                icon = QtGui.QIcon('Images/Tick.svg')
                i.setIcon(icon)
                i.setIconSize(QtCore.QSize(32,32))
                # i.setText(i.text()+('\t(Correct)'))
                self.TimerControl = False
                playsound('Audio/Correct.mp3')
                # btns.remove(i)
                break
                
            elif i.isChecked() is True and i.text() != ans:
                # print('Wrong') 
                i.setStyleSheet('''
                                QPushButton::checked
                                {
                                background-color: red;
                                color: white
                                }
                                ''')
                icon = QtGui.QIcon('Images/Cross.svg')
                i.setIcon(icon)
                i.setIconSize(QtCore.QSize(32,32))
                # i.setText(i.text()+('\t(Wrong)'))
                self.TimerControl = False
                playsound('Audio/Wrong.mp3')
                # btns.remove(i)
                break
        
        # print([i.objectName() for i in btns])        
        # print(frame.objectName(), ans)
        
    for i in check_btn: i[1].clicked.connect(lambda _, widget = i[0], ans = i[2]: check(widget, ans))
    
    
def scores(self, round_info):
    
    def action(round):
        self.s_Tick = round_info[' '.join(round.split('_'))]['tick']
        self.s_Plus = round_info[' '.join(round.split('_'))]['plus']
        self.s_Minus= round_info[' '.join(round.split('_'))]['minus']
        
        
        if self.s_Minus < 0: Modify_scroing(self, self._Team_Names, 'a')
        else: 
            try : Modify_scroing(self, self._Team_Names, 'r')
            except : pass
        
        print(f'\t\tUpdatedScores\nTick : {self.s_Tick}\nPlus : {self.s_Plus}\nMinus : {self.s_Minus}')
    
    wids = [i for i in self.stackedWidget.children() if 'Info' in i.objectName()]
    btns = []
    
    for i in wids:
        for j in i.children():
            if '_Button' in j.objectName(): btns.append((j,'_'.join(j.objectName().split('_')[:-2])))
    
    
    # print([[j.objectName() for j in i.children()] for i in wids])
    # print([(i[0].objectName(),i[1]) for i in btns])
    
    for i in btns: i[0].clicked.connect(lambda _, round = i[1]: action(round))
        
    
def Timer_Connect(self, rounds, _rounds, rounds_info, qns):
    
    def clock(label, time):
        while self.TimerControl is True:
            sec = time
            ans = True
            while sec != 0:
                if self.TimerControl is not True: break 
                sec -=1
                label.setText(str(sec))
                sleep(0.9)
            
            if sec == 0 :
                ans = False 
                label.setText('Time Up')
                playsound('Audio/TimeUp.mp3')
                self.TimerControl = False
        if ans == True:
            label.setText('ANSWERED')
            self.TimerControl = False
            
    
    
    def clock_control(label, time):
        self.TimerControl = True
        self._clock_thread = Thread(target= clock, args=(label, int(time)))
        self._clock_thread.setDaemon(True)
        self._clock_thread.start()        
        if self.TimerControl is False: self._clock_thread.join()
        
    wids = [j for j in self.stackedWidget.children() if 'Widget' in j.objectName()]
    timer_btn = []
    timer_lbl = {}
    
    # self.TimerControl = False
    
    for i in wids:
        # print(i.objectName())
        for j in i.children()[1].children():
            if '_Question' in j.objectName():
                for k in j.children():
                    if '_Timer' in k.objectName():
                        timer_lbl['_'.join(k.objectName().split('_')[:-1])] = k
    # print(timer_lbl)
            
    for i in wids:
        for j in i.children()[1].children():
            if '_Option' in j.objectName():
                for k in j.children():
                    if '_Start_Timer' in k.objectName(): 
                        timer_btn.append((k, timer_lbl['_'.join(j.objectName().split('_')[:-1])], str(rounds_info[' '.join(j.objectName().split('_')[:-2])]['time'])))
                            
    # print([(i[0].objectName(),i[1].objectName(), i[2]) for i in timer_btn])
    
    
    for i in timer_btn: i[0].clicked.connect(lambda _, label = i[1], time = i[2]: clock_control(label, time))
    
    
    
    