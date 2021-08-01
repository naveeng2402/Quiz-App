from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFrame, QLabel, QSizePolicy, QVBoxLayout, QWidget

import conf
from widget_generation import *
from UI.teams import Ui_teams


class Teams:
    def __init__(self, data:dict) -> None:
        self.dig = QDialog()
        self.ui = Ui_teams()
        self.ui.setupUi(self.dig)
        
        self.team_names:List[str] = data['Team_Names']
        self.no_of_players = int(data['Players_NO'])

        dynamic_ui(self.ui, self.team_names, self.no_of_players)
        
        
        
def dynamic_ui(self:Ui_teams, team_names:List[str], no_of_players:int)->None:        
        teams_count = len(team_names)
        
        for i in range(teams_count):
            tab = QWidget()
            tab.setObjectName(team_names[i])
            
            tab_layout = QVBoxLayout(tab)
            
            label = QLabel(tab)
            label.setText(team_names[i])
            label.setAlignment(Qt.AlignCenter)
            label.setAccessibleName("teams_labels")
            tab_layout.addWidget(label)
            
            sizePolicy = set_size_policy(conf.size_Preferred, conf.size_Expanding)
            
            frame = QFrame(tab)
            frame.setSizePolicy(sizePolicy)
            frame.setFrameShape(QFrame.Shape.NoFrame)
            frame.setFrameShadow(QFrame.Shadow.Plain)
            
            frame_layout = QVBoxLayout(frame)
            
            for j in range(no_of_players):
                sizePolicy = set_size_policy(conf.size_Expanding, conf.size_Preferred)
                line_edit = line_edit_gen(frame, frame_layout, accessible_name='teams_input', sizePolicy=sizePolicy)
                self.line_edits.append(line_edit)
                
            tab_layout.addWidget(frame)
            
            self.tabWidget.addTab(tab, team_names[i])
            
            
            
            