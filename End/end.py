from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.uic import loadUi
import sys

class End(QtWidgets.QDialog):

    def __init__(self, winners):
        super(QtWidgets.QDialog, self).__init__()
        loadUi("End/end.ui", self)
        msg = f"""
                <p style="text-align: center; font-size: 30px;"><em><strong>CONGRATS!!!</strong></em></p>
                <p style="text-align: center; font-size: 50px;"><em><strong>{winners}</strong></em></p>
                <p style="text-align: center; font-size: 30px;"><em><strong>You Have Won the Quiz</strong></em></p>
                <p style="text-align: center; font-size: 20px;">by your exceptional performance</p>
              """
        self.label.setText(msg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.resize(400,300)

    widget.addWidget(End("Naveen, Naveen, Naveen, Naveen"))
    widget.show()
    sys.exit(app.exec_())