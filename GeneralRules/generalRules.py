from PyQt5.QtGui import QKeySequence
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QShortcut, QTextBrowser, QStackedWidget, QApplication, QDialog
import json
import sys

class GeneralRules(QDialog):

    def __init__(self):
        super(QDialog, self).__init__()
        loadUi('GeneralRules/generalRules.ui', self)
    
        with open('Json/data.json') as f:
            content = json.load(f)['GeneralRules']

        self.Rules.setText(content)
        self.mainFrame.setStyleSheet('''border-image:url(BG/Trans.png)''')
        
        # self.shortcut = QShortcut(QKeySequence('Esc'))
        # self.shortcut.activated.connect(self.summa)
    
    def summa(): pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    widget.setWindowTitle('RULES')
    widget.addWidget(GeneralRules())
    widget.show()
    sys.exit(app.exec_())

