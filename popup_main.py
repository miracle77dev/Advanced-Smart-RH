from PyQt5 import QtCore, QtGui, QtWidgets
from popup import Ui_Form
import cv2,os,sys
import shutil
from Functions import employer

class Popup(QtWidgets.QWidget):
    def __init__(self):
        super(Popup, self).__init__()
        self.ui = Ui_Form()
        self.Empl = employer.Employer()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.StartCamBtn.clicked.connect(self.StartCamera)
        self.ui.AddEmployerBtn.clicked.connect(self.AddEmployer)
        self.ui.msg.setStyleSheet("color:rgb(255, 255, 255)")
        self.Path = ''
        self.Photo = 0

    def StartCamera(self):
        Cap = cv2.VideoCapture(0)
        while True:
            Ret, Image = Cap.read()
            cv2.imshow("SAVE NEW EMPLOYEE", Image)
            key = cv2.waitKey(1)
            if key == 99:
                cv2.imwrite("sanflan.png", Image)
                self.Photo = 1
                try:
                    if self.ui.lineEditNom.text() != '' and self.ui.lineEditMatricule.text() != '' :
                        self.Path = f"./know/{self.ui.lineEditNom.text()} - {self.ui.lineEditMatricule.text()}.png"
                except:
                    ...
                self.ui.ImgFrame.setStyleSheet("border-image:url(./sanflan.png);")

            if key == 27:
                cv2.destroyAllWindows()
                break

    def AddEmployer(self):
        if self.ui.lineEditNom.text() == '' or self.ui.lineEditMatricule.text() == '' or self.ui.comboBoxPost.currentIndex() == 0 or self.ui.comboBoxType.currentIndex() == 0 :
            self.ui.msg.setText("Remplir les champs...")
            self.ui.msg.setStyleSheet("color: rgb(255, 28, 8)")
        elif self.Path == '':
            if self.ui.lineEditNom.text() != '' and self.ui.lineEditMatricule.text() != '':
                self.Path = f"./know/{self.ui.lineEditNom.text()} - {self.ui.lineEditMatricule.text()}.png"
            else:
                self.ui.msg.setText("Ajouter la photo ...")
                self.ui.msg.setStyleSheet("color: rgb(255, 28, 8)")
        else:
            if self.Photo == 1:
                if self.Path != '':
                    self.Path = f"./know/{self.ui.lineEditNom.text()} - {self.ui.lineEditMatricule.text()}.png"
                    shutil.copyfile("./sanflan.png", self.Path)
                    Data = (self.ui.lineEditMatricule.text(),self.ui.comboBoxType.currentText(),self.ui.lineEditNom.text(),self.ui.lineEditPrenom.text(),self.ui.comboBoxPost.currentText())
                    if self.Empl.AddEmployer(Data) == 0:
                        self.ui.msg.setText("Bienvenue !")
                        self.ui.msg.setStyleSheet("color:rgb(0, 145, 0)")
                        # Vider les champs
                        self.ui.lineEditNom.setText("")
                        self.ui.lineEditPrenom.setText("")
                        self.ui.lineEditMatricule.setText("")
                else:
                    self.ui.msg.setText("Ajouter la photo ...")
                    self.ui.msg.setStyleSheet("color: rgb(255, 28, 8)")
            else:
                self.ui.msg.setText("Ajouter la photo ...")
                self.ui.msg.setStyleSheet("color: rgb(255, 28, 8)")






if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    Win = Popup()
    Win.show()
    sys.exit(App.exec())