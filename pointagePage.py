from PyQt5 import QtCore, QtGui, QtWidgets
from pointage import Ui_Form
import sys
class PointagePage(QtWidgets.QWidget):
    def __init__(self):
        super(PointagePage, self).__init__()
        self.DataPara = []
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)


    def setDatePara(self,DatePara):
        self.DataPara = DatePara


    def getDatePara(self):
        return self.DataPara



if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    Win = PointagePage()
    Win.show()
    sys.exit(App.exec())