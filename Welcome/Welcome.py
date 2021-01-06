"""
This file is resposible for the first screen of the application

Features:
    The welcome screen is the first screen the user faces when the app starts
    The topic is displayed by reading the Json\data.json file
    The host name(s) is also done by reading the same file
    The window automatically adjusts itself for the number of host names specified

Note: You can know more about editing the json file in the readme.md or readme.txt

"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Welcome():
    
    def __init__(self,  Hosts, Topic_name):
        '''
        This class is responsible for the Welcome Screen
        
        Variables:
            Hosts     : list:: consisting Host Names
            Topic_name: str :: Name of the topic
        '''        
        # self.Dialog = super(QtWidgets.QDialog, self).__init__()
        
        self.Dialog = QtWidgets.QDialog()
        self.Hosts = Hosts
        self.Topic_name = Topic_name
        
        self.setup()
        self.Dialog.show()
    
    def setup(self):
        '''
        This makes up the parent widgets and sets plot to programatically generate rest of the widgets
        '''

        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(662, 471)
        
        
        self.gridLayout = QtWidgets.QGridLayout(self.Dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        
        self.frame = QtWidgets.QFrame(self.Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        
        self.Welcome = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Welcome.sizePolicy().hasHeightForWidth())
        self.Welcome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Welcome.setFont(font)
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setText("Welcome you all to the QUIZ on")
        self.Welcome.setObjectName("Welcome")
        self.gridLayout_2.addWidget(self.Welcome, 0, 0, 1, len(self.Hosts))
        
        
        self.Topic = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Topic.sizePolicy().hasHeightForWidth())
        self.Topic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.Topic.setFont(font)
        self.Topic.setAlignment(QtCore.Qt.AlignCenter)
        self.Topic.setText(self.Topic_name)
        self.Topic.setObjectName("Topic")
        self.gridLayout_2.addWidget(self.Topic, 1, 0, 1, len(self.Hosts))
        
        
        self.HostedBy = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HostedBy.sizePolicy().hasHeightForWidth())
        self.HostedBy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.HostedBy.setFont(font)
        self.HostedBy.setAlignment(QtCore.Qt.AlignCenter)
        self.HostedBy.setText("Hosted By :")
        self.HostedBy.setObjectName("HostedBy")
        self.gridLayout_2.addWidget(self.HostedBy, 2, 0, 1, len(self.Hosts))
        
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        

        # Generating the labels for Host's name
        for i in range(len(self.Hosts)):
            exec(f'''self.Host_{i+1} = QtWidgets.QLabel(self.frame)''')            
            eval(f'''self.Host_{i+1}.setFont(font)''')
            eval(f'''self.Host_{i+1}.setAlignment(QtCore.Qt.AlignCenter)''')
            eval(f'''self.Host_{i+1}.setText('{self.Hosts[i]}')''')
            eval(f'''self.Host_{i+1}.setObjectName('Host_{i+1}')''')
            eval(f'''self.Host_{i+1}.setStyleSheet("""border: 3px solid black;
                                                      background-color: rgba(255, 255, 255,30); """)''')
            eval(f'''self.gridLayout_2.addWidget(self.Host_{i+1}, 3, {i}, 1, 1)''')
        
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        font.setPointSize(20)

        self.Done_Button = QtWidgets.QPushButton(self.frame)
        self.Done_Button.setFont(font)
        self.Done_Button.setMinimumHeight(75)
        self.Done_Button.setText('Start Quiz')
        self.gridLayout_2.addWidget(self.Done_Button, 4, 0, 1, len(self.Hosts))
        
        
        self.Done_Button.setStyleSheet('''
                                       margin-top : 20px
                                       ''')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    ui = Welcome(['Nagi Pragalathan', 'Heamenth'], 'Engineering Graphics')
    # ui.setupUi()
    # Dialog.show()
    sys.exit(app.exec_())
