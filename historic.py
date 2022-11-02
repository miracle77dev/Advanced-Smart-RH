import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from historique import Ui_Form
import sys
from popup_main import Popup
from pointagePage import PointagePage
from Functions import pointage


class Historic(QtWidgets.QWidget):
    def __init__(self):
        super(Historic, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.DateCustomize = Popup()
        self.Pointage = pointage.Pointage()
        self.PointageFen = PointagePage()
        self.Interval = []
        self.T = "" #Cette variable renvoi l'initial du type: E ou O, cela peut aider à choisir la table ou faire la requête SQL
        self.CourrantMonth()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.PersonnaliseBtn.clicked.connect(self.OpenWindow)
        self.ui.HistoriqueEmbaucheBtn.clicked.connect(lambda: self.CourrantMonth("E"))
        self.ui.HistoriqueOuvriersBtn.clicked.connect(lambda: self.CourrantMonth("O"))
        self.DateCustomize.ui.AppliquerBtn.clicked.connect(lambda: self.CourrantMonth("P"))
        self.ui.GenererPointageBtn.clicked.connect(self.GenererPointage)

    def CourrantMonth(self,Type="E"):
        """ E: pour embauche
            O: pour ouvrier
            P: pour personnaliser
        """

        if Type == "E":
            self.T = "E"
            self.Interval.clear()
            self.ui.TableauHistorique.clear()
            Ligne = 0
            for i in self.Pointage.getPointageMoisCourantEmbauche():
                QtWidgets.QTreeWidgetItem(self.ui.TableauHistorique)
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(0, str(i[0]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(1, str(i[1]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(2, str(i[2]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(3, str(i[3]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(4, str(i[4]))
                self.Interval.append(i[4])
                Ligne += 1

        elif Type == "O":
            self.T = "O"
            self.Interval.clear()
            self.ui.TableauHistorique.clear()
            Ligne = 0
            for i in self.Pointage.getPointageMoisCourantOuvrier():
                QtWidgets.QTreeWidgetItem(self.ui.TableauHistorique)
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(0, str(i[0]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(1, str(i[1]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(2, str(i[2]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(3, str(i[3]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(4, str(i[4]))
                self.Interval.append(i[4])
                Ligne += 1
        elif Type == "P":
            self.T = self.DateCustomize.ui.ChoseTypeBox.currentText()[0]
            self.Interval.clear()
            Data = (self.DateCustomize.ui.dateEdit.date().toPyDate(),self.DateCustomize.ui.dateEdit_2.date().toPyDate())
            self.ui.TableauHistorique.clear()
            Ligne = 0
            for i in self.Pointage.getPointagePersonnalise(self.DateCustomize.ui.ChoseTypeBox.currentText(),Data):
                QtWidgets.QTreeWidgetItem(self.ui.TableauHistorique)
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(0, str(i[0]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(1, str(i[1]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(2, str(i[2]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(3, str(i[3]))
                self.ui.TableauHistorique.topLevelItem(Ligne).setText(4, str(i[4]))
                self.Interval.append(i[4])
                Ligne += 1
            self.DateCustomize.close()

    def GenererPointage(self):
        try:
            if self.Interval[0] != [] and self.Interval[-1] != []:
                if self.T == "E":
                    Data =  self.Pointage.GeneratePointage("P_Journalier",(self.Interval[-1],self.Interval[0]))
                    self.PointageFen.ui.TableauPointageE.clear()
                    self.Ligne = 0
                    D1 = "-".join(self.Interval[-1].split("-")[::-1])
                    D2 = "-".join(self.Interval[0].split("-")[::-1])
                    self.PointageFen.ui.StackedWidgetHistorique.setCurrentIndex(0)
                    for i in Data:
                        QtWidgets.QTreeWidgetItem(self.PointageFen.ui.TableauPointageE)
                        self.PointageFen.ui.TableauPointageE.topLevelItem(self.Ligne).setText(0, str(i[0]))
                        self.PointageFen.ui.TableauPointageE.topLevelItem(self.Ligne).setText(1, str(i[1]))
                        self.PointageFen.ui.TableauPointageE.topLevelItem(self.Ligne).setText(2, str(i[2]))
                        self.PointageFen.ui.TableauPointageE.topLevelItem(self.Ligne).setText(3, str(i[3]))
                        self.PointageFen.ui.TableauPointageE.topLevelItem(self.Ligne).setText(4, str(i[4]))
                        self.PointageFen.ui.TableauPointageE.topLevelItem(self.Ligne).setText(5, f"Du {D1} au {D2}")
                        self.Ligne += 1
                    self.PointageFen.show()
                elif self.T == "O":
                    self.Ligne = 0
                    self.PointageFen.ui.StackedWidgetHistorique.setCurrentIndex(1)
                    Data = self.Pointage.GeneratePointage("P_Heure", (self.Interval[-1],self.Interval[0]))
                    D1 = "-".join(self.Interval[-1].split("-")[::-1])
                    D2 = "-".join(self.Interval[0].split("-")[::-1])
                    self.PointageFen.ui.TableauPointageO.clear()
                    for i in Data:
                        QtWidgets.QTreeWidgetItem(self.PointageFen.ui.TableauPointageO)
                        self.PointageFen.ui.TableauPointageO.topLevelItem(self.Ligne).setText(0, str(i[0]))
                        self.PointageFen.ui.TableauPointageO.topLevelItem(self.Ligne).setText(1, str(i[1]))
                        self.PointageFen.ui.TableauPointageO.topLevelItem(self.Ligne).setText(2, str(i[2]))
                        self.PointageFen.ui.TableauPointageO.topLevelItem(self.Ligne).setText(3, str(i[3]))
                        self.PointageFen.ui.TableauPointageO.topLevelItem(self.Ligne).setText(4, str(i[4]))
                        self.PointageFen.ui.TableauPointageO.topLevelItem(self.Ligne).setText(5, f"Du {D1} au {D2}")
                        self.Ligne += 1
                    self.PointageFen.show()
            else:
                ...
        except:
            ...

    def OpenWindow(self):
        self.DateCustomize.ui.NotifsBoxPanel.setCurrentIndex(1)
        self.DateCustomize.show()


if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    Win = Historic()
    Win.show()
    sys.exit(App.exec())
