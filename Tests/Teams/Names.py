from PyQt5 import QtCore, QtWidgets, QtGui

def names_frame_gen(self, no = 0, source = None, layout = None, Team = "None"):
    # QtWidgets.QFrame.StyledPanel
    _Team = '_'.join(Team.split()) # Team Name Without Spaces but Underscores
    
    exec(f'''self.names_frame = QtWidgets.QFrame({source})''')
    eval(f'''self.names_frame.setFrameShape(QtWidgets.QFrame.NoFrame)''')
    eval(f'''self.names_frame.setFrameShadow(QtWidgets.QFrame.Raised)''')
    eval(f'''self.names_frame.setObjectName("names_frame")''')
    eval(f'''{layout}.addWidget(self.names_frame)''')
    
    
    exec(f'''self.gridLayout = QtWidgets.QGridLayout(self.names_frame)''')
    eval(f'''self.gridLayout.setObjectName("gridLayout")''')
    
    
    
    exec(f'''self.names_frame_2 = QtWidgets.QFrame(self.names_frame)''')
    eval(f'''self.names_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)''')
    eval(f'''self.names_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)''')
    eval(f'''self.names_frame_2.setObjectName("names_frame_2")''')
    eval(f'''self.gridLayout.addWidget(self.names_frame_2, 1,1)''')        
    
    
    exec('''sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)''')
    
    exec(f'''self.names_verticalLayout = QtWidgets.QVBoxLayout(self.names_frame_2)''')
    eval(f'''self.names_verticalLayout.setContentsMargins(0,0,0,0)''')
    eval(f'''self.names_verticalLayout.setObjectName("names_verticalLayout")''')
    
    
    exec(f'''self.names_label_{_Team} = QtWidgets.QLabel(self.names_frame_2)''')
    eval(f'''self.names_label_{_Team}.setAlignment(QtCore.Qt.AlignCenter)''')
    eval(f'''self.names_label_{_Team}.setObjectName("names_label_{_Team}")''')
    exec(f'''self.names_label_{_Team}.setSizePolicy(sizepolicy)''')
    eval(f'''self.names_label_{_Team}.setText('{Team}')''')
    exec(f'''Font = QtGui.QFont()''')
    eval(f'''Font.setPointSize(20)''')
    eval(f'''self.names_label_{_Team}.setFont(Font)''')
    eval(f'''self.names_verticalLayout.addWidget(self.names_label_{_Team})''')
    
    
    # exec(f'''self.names_spacerItem_top = QtWidgets.QSpacerItem(20,40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)''')
    # eval(f'''self.gridLayout.addItem(self.names_spacerItem_top, 0, 1, 1, 1)''')
    
    
    # exec(f'''self.names_spacerItem_bottom = QtWidgets.QSpacerItem(20,40, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)''')
    # eval(f'''self.gridLayout.addItem(self.names_spacerItem_bottom, 2, 1, 1, 1)''')
    
    
    exec(f'''self.names_spacerItem_left = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)''')
    eval(f'''self.gridLayout.addItem(self.names_spacerItem_left, 1, 0, 1, 1)''')
    
    exec(f'''self.names_spacerItem_right = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)''')
    eval(f'''self.gridLayout.addItem(self.names_spacerItem_right, 1, 2, 1, 1)''')
    
    
    for i in range(1,no+1):
        exec(f'''self.names_lineEdit_{_Team}_{i} = QtWidgets.QLineEdit(self.names_frame_2)''')
        eval(f'''self.names_lineEdit_{_Team}_{i}.setAlignment(QtCore.Qt.AlignCenter)''')
        eval(f'''self.names_lineEdit_{_Team}_{i}.setObjectName("names_lineEdit_{_Team}_{i}")''')
        exec('''sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)''')
        eval('''sizePolicy.setHorizontalStretch(0)''')
        eval('''sizePolicy.setVerticalStretch(0)''')
        eval(f'''sizePolicy.setHeightForWidth(self.names_lineEdit_{_Team}_{i}.sizePolicy().hasHeightForWidth())''')
        eval(f'''self.names_lineEdit_{_Team}_{i}.setSizePolicy(sizePolicy)''')
        eval(f'''Font.setPointSize(15)''')
        eval(f'''self.names_lineEdit_{_Team}_{i}.setFont(Font)''')
        eval(f'''self.names_verticalLayout.addWidget(self.names_lineEdit_{_Team}_{i})''')
        
    # print([i.objectName() for i in self.names_frame_2.children()])

def tabs_gen(self, team_no = 0, player_no = 7, source = None, layout=None, Teams = ['Team A', 'Team B']):
    
    _Teams = ['_'.join(i.split()) for i in Teams]

    exec(f'''self.tabWidget = QtWidgets.QTabWidget({source})''')
    eval('''self.tabWidget.setObjectName("tabWidget")''')
    eval(f'''{layout}.addWidget(self.tabWidget)''')
    
    for i in range(1,team_no+1):
        
        exec(f'''self.tab_{i} = QtWidgets.QWidget()''')
        eval(f'''self.tab_{i}.setObjectName("tab_{i}")''')
        
        exec(f'''self.tab_{i}_grid = QtWidgets.QGridLayout(self.tab_{i})''')
        eval(f'''self.tab_{i}_grid.setObjectName("tab_{i}_grid")''')

        eval(f'''names_frame_gen(self, player_no, 'self.tab_{i}', 'self.tab_{i}_grid', '{Teams[i-1]}')''')
            
        eval(f'''self.tabWidget.addTab(self.tab_{i}, '{Teams[i-1]}')''')
