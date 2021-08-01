from typing import List
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel

import conf
from UI import Ui_welcome
import screen_functions  

class Welcome:
    def __init__(self, data:dict) -> None:
        self.dig = QDialog()
        self.ui = Ui_welcome()
        self.ui.setupUi(self.dig)
        
        self.topic = data['Topic']
        self.hosts = data['Hosts']
        
        dynamic_ui(self.ui, self.topic, self.hosts)

        self.ui.start_quiz.clicked.connect(lambda: self.start())
        
    def start(self):
        screen_functions.teams_scr(conf.CONFIG['Teams'])
        conf.STACK.setCurrentWidget(conf.SCREENS_WIDGETS['teams_scr'])


def dynamic_ui(self: Ui_welcome, topic_name: str, hosts: List[str]):
    
    hosts_lbl:List[QLabel] = []
    self.hosts_lbl = hosts_lbl
    
    lbls = [i for i in self.frame.children() if type(i) == QLabel] # Getting the labels
    
    for index in range(len(lbls)):
        self.gridLayout_2.addWidget(lbls[index], index, 0, 1, len(hosts))
        # Adding existing widget automatically removes it from the grid
                
    for i in range(len(hosts)):
        self.hosts_lbl.append(QLabel(hosts[i], self.frame))
        self.hosts_lbl[i].setAccessibleName('hosts')
        self.hosts_lbl[i].setAlignment(QtCore.Qt.AlignCenter)
        self.hosts_lbl[i].setObjectName(f'host_{i+1}')
        self.gridLayout_2.addWidget(self.hosts_lbl[i], 3, i, 1, 1, QtCore.Qt.AlignCenter)
        
    
    self.topic.setText(topic_name)