# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/SYSTEM/Programming/Python Projects/Quiz/ui/teams.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teams(object):
    def __init__(self) -> None:
        self.tabs:List[QtWidgets.QWidget] = []
        self.line_edits:List[QtWidgets.QLineEdit] = []
        
    def setupUi(self, teams):
        teams.setObjectName("teams")
        teams.resize(500, 391)
        self.verticalLayout = QtWidgets.QVBoxLayout(teams)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(teams)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.done_btn = QtWidgets.QPushButton(teams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_btn.sizePolicy().hasHeightForWidth())
        self.done_btn.setSizePolicy(sizePolicy)
        self.done_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.done_btn.setObjectName("done_btn")
        self.verticalLayout.addWidget(self.done_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(teams)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(teams)

    def retranslateUi(self, teams):
        _translate = QtCore.QCoreApplication.translate
        teams.setWindowTitle(_translate("teams", "Dialog"))
        self.done_btn.setText(_translate("teams", "Done"))