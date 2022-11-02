from PyQt5 import QtCore, QtWidgets
from asrh import Ui_MainWindow
from popup_main import Popup
from PyQt5.QtCore import QRect, QPropertyAnimation,QEasingCurve,QUrl
import sys
from FaceDetection import StartCamera
from Functions import pointage,employer
from historic import Historic

class Asrh(QtWidgets.QMainWindow):
    def __init__(self):
        super(Asrh, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DialogBox = Popup()
        self.Historic = Historic()
        self.Pointage = pointage.Pointage()
        self.TotalEmployer = employer.Employer()
        self.ui.labelTotalPersonnal.setText(str(self.TotalEmployer.GetNumberOfEmployer()))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #Contrôle fenêtre
        self.ui.HomeFrame.mouseMoveEvent = self.DeplaceFenetre
        self.ui.HomeFrame.mouseDoubleClickEvent = self.MaxAndMinWindow
        self.ui.labelRediusIcon.mousePressEvent = self.RediusWindow
        self.ui.labelQuitIcon.mousePressEvent = self.CloseWindow
        self.ui.labelMenuIcon.mousePressEvent = self.animMenuPanel
        self.ui.HomeLabel.mousePressEvent = self.animMenuPanel2
        self.ui.labelShowHideMenu.mousePressEvent = self.AnimMenuCache
        self.ui.labelNotifIcon.clicked.connect(lambda :self.InfoBox("Info"))
        self.ui.PointageBtn.clicked.connect(self.PointageCam)
        self.ui.UpdateBtn.clicked.connect(self.ShowRessource)
        self.ui.HistoriqueBtn.clicked.connect(lambda: self.Historic.show())
        self.ui.AddEmployerBtn.clicked.connect(self.StartCam)
        self.ui.HomeLabel.hide()
        self.ui.MenuCache.hide()
        self.Ligne = 0
        self.CacheMenuFrame = 0
        self.ShowRessource()
        self.ui.labelTotalPresent.setText(str(self.Ligne))
    #Deplacer la fenêtre
    def DeplaceFenetre(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.ClickPosition)
            self.ClickPosition = event.globalPos()
            event.accept()

    def StartCam(self):
        self.DialogBox.ui.NotifsBoxPanel.setCurrentIndex(2)
        self.DialogBox.show()

    def PointageCam(self):
        StartCamera()


    def mousePressEvent(self, event):
        self.ClickPosition = event.globalPos()

    def RediusWindow(self,event):
        self.showMinimized()

    def CloseWindow (self,event):
        self.close()

    def MaxAndMinWindow(self, event):
        if self.isMaximized() == True:
            self.showNormal()
        else:
            self.showMaximized()
            self.ui.MenuCache.setMinimumWidth(int(self.ui.PointageDashbord.width()))

    def animMenuPanel(self,event):
        self.frame = QPropertyAnimation(self.ui.frame, b"minimumWidth")
        self.frame.setEasingCurve(QEasingCurve.Linear)
        self.frame.setDuration(180)  # 550
        self.frame.setStartValue(220)
        self.frame.setEndValue(0)
        self.frame.start()
        self.ui.HomeLabel.show()
        self.ui.labelMenuIcon.hide()

    def animMenuPanel2(self,event):
        self.frame = QPropertyAnimation(self.ui.frame, b"minimumWidth")
        self.frame.setEasingCurve(QEasingCurve.Linear)
        self.frame.setDuration(210)  # 750
        self.frame.setStartValue(0)
        self.frame.setEndValue(220)
        self.frame.start()
        self.ui.labelMenuIcon.show()
        self.ui.HomeLabel.hide()

    def InfoBox(self, type):
        if type == "Danger":
            self.DialogBox.ui.NotifsBoxPanel.setCurrentIndex(3)
            self.DialogBox.show()
            self.AnimNotif()
        elif type == "Succes":
            self.DialogBox.ui.NotifsBoxPanel.setCurrentIndex(1)
            self.DialogBox.show()
            self.AnimNotif()
        elif type == "Info":
            self.DialogBox.ui.NotifsBoxPanel.setCurrentIndex(0)
            self.DialogBox.show()
            self.AnimNotif()
        elif type == "Erreur":
            self.DialogBox.ui.NotifsBoxPanel.setCurrentIndex(2)
            self.DialogBox.show()
            self.AnimNotif()

    def AnimNotif(self):
        self.anim = QPropertyAnimation(self.DialogBox, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.setDuration(750)
        self.anim.setStartValue(QRect(540, 0, 26, 16))
        if self.isMaximized() == True:
            self.anim.setEndValue(QRect(540, 90, 950, 537))
        else:
            self.anim.setEndValue(QRect(540, 150, 950, 537))
        self.anim.start()

    def AnimMenuCache(self,event):
        if  self.CacheMenuFrame == 0:
            self.CacheMenuFrame = 1
            self.ui.MenuCache.setMaximumWidth(int(self.ui.PointageDashbord.width()))
            self.ui.MenuCache.show()
            self.anim = QPropertyAnimation(self.ui.MenuCache, b"geometry")
            self.anim.setEasingCurve(QEasingCurve.Linear)
            self.anim.setDuration(250)
            self.anim.setStartValue(QRect(9, -15, int(self.ui.PointageDashbord.width()), 0))
            self.anim.setEndValue(QRect(9, 9, int(self.ui.PointageDashbord.width()), 50))
            self.anim.start()
        else:
            self.CacheMenuFrame = 0
            self.ui.MenuCache.hide()

    def ShowRessource(self):
        self.ui.TableAujourdhui.clear()
        self.Ligne = 0
        for i in self.Pointage.getPointage():
            QtWidgets.QTreeWidgetItem(self.ui.TableAujourdhui)
            self.ui.TableAujourdhui.topLevelItem(self.Ligne).setText(0, str(i[0]))
            self.ui.TableAujourdhui.topLevelItem(self.Ligne).setText(1, str(i[1]))
            self.ui.TableAujourdhui.topLevelItem(self.Ligne).setText(2, str(i[2]))
            self.ui.TableAujourdhui.topLevelItem(self.Ligne).setText(3, str(i[3]))
            self.ui.TableAujourdhui.topLevelItem(self.Ligne).setText(4, str(i[4]))
            self.Ligne += 1
        #Actualiser la valeur de la liste de presence
        self.ui.labelTotalPersonnal.setText(str(self.TotalEmployer.GetNumberOfEmployer()))
        self.ui.labelTotalPresent.setText(str(self.Ligne))
        self.ui.labelTotalAbsent.setText(str(int(self.TotalEmployer.GetNumberOfEmployer())-int(self.Ligne)))
        self.ui.PresentVal.setText(str(self.Ligne))
        self.ui.AbsentVal.setText(str(int(self.TotalEmployer.GetNumberOfEmployer())-int(self.Ligne)))



if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    Win = Asrh()
    Win.show()
    sys.exit(App.exec())