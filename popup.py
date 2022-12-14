# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 220)
        Form.setMinimumSize(QtCore.QSize(530, 220))
        Form.setMaximumSize(QtCore.QSize(530, 220))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Ressource/Images/ASRH_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NotifsBoxPanel = QtWidgets.QStackedWidget(Form)
        self.NotifsBoxPanel.setStyleSheet("QStackedWidget{\n"
"background-color: rgb(255, 0, 0);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    color:#fff;\n"
"    border-radius:7px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(96, 166, 252, 255), stop:1 rgba(105, 131, 243, 255));\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(104, 176, 255, 255), stop:1 rgba(115, 141, 253, 255));\n"
"}")
        self.NotifsBoxPanel.setObjectName("NotifsBoxPanel")
        self.Info = QtWidgets.QWidget()
        self.Info.setObjectName("Info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Info)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.Info)
        self.frame.setStyleSheet("QFrame#frame{\n"
"    border-radius:15px;\n"
"    background-color: rgb(240, 242, 245); \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 50, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.522, y2:1, stop:0 rgba(96, 166, 252, 255), stop:1 rgba(105, 131, 243, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.labelIcon = QtWidgets.QLabel(self.frame)
        self.labelIcon.setGeometry(QtCore.QRect(0, 10, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelIcon.setFont(font)
        self.labelIcon.setStyleSheet("image: url(:/Autre/Images/AutreIcon/alert-circle.svg);")
        self.labelIcon.setText("")
        self.labelIcon.setObjectName("labelIcon")
        self.textBrowserInfo = QtWidgets.QTextBrowser(self.frame)
        self.textBrowserInfo.setGeometry(QtCore.QRect(5, 100, 521, 51))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowserInfo.setFont(font)
        self.textBrowserInfo.setStyleSheet("color: rgb(31, 31, 31);\n"
"border:none;\n"
"background-color: rgb(240, 242, 245);")
        self.textBrowserInfo.setObjectName("textBrowserInfo")
        self.ComprisBtn = QtWidgets.QPushButton(self.frame)
        self.ComprisBtn.setGeometry(QtCore.QRect(178, 160, 181, 36))
        self.ComprisBtn.setMinimumSize(QtCore.QSize(0, 36))
        self.ComprisBtn.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ComprisBtn.setFont(font)
        self.ComprisBtn.setStyleSheet("")
        self.ComprisBtn.setObjectName("ComprisBtn")
        self.verticalLayout_2.addWidget(self.frame)
        self.NotifsBoxPanel.addWidget(self.Info)
        self.Succes = QtWidgets.QWidget()
        self.Succes.setStyleSheet("QWidget#Succes{\n"
"background-color: rgb(240, 242, 245);\n"
"}")
        self.Succes.setObjectName("Succes")
        self.AppliquerBtn = QtWidgets.QPushButton(self.Succes)
        self.AppliquerBtn.setGeometry(QtCore.QRect(170, 150, 181, 33))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.AppliquerBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/BlancIcone/Images/BlancIcon/check-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AppliquerBtn.setIcon(icon1)
        self.AppliquerBtn.setObjectName("AppliquerBtn")
        self.frame_2 = QtWidgets.QFrame(self.Succes)
        self.frame_2.setGeometry(QtCore.QRect(60, 70, 411, 61))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"    border:1px solid;\n"
"    border-color: rgba(103, 139, 245,0.2);\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"padding:6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(96, 166, 252, 0.1), stop:1 rgba(105, 131, 243, 0.1));\n"
"border-radius:6px;\n"
"color: rgb(103, 139, 245);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setMinimumSize(QtCore.QSize(170, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(170, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.frameBlanc = QtWidgets.QFrame(self.Succes)
        self.frameBlanc.setGeometry(QtCore.QRect(0, 0, 531, 221))
        self.frameBlanc.setStyleSheet("")
        self.frameBlanc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBlanc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBlanc.setObjectName("frameBlanc")
        self.ChoseTypeBox = QtWidgets.QComboBox(self.frameBlanc)
        self.ChoseTypeBox.setGeometry(QtCore.QRect(60, 20, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ChoseTypeBox.setFont(font)
        self.ChoseTypeBox.setStyleSheet("QComboBox{\n"
"border:none;\n"
"padding:6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(96, 166, 252, 0.1), stop:1 rgba(105, 131, 243, 0.1));\n"
"border-radius:6px;\n"
"color: rgb(103, 139, 245);;}\n"
"")
        self.ChoseTypeBox.setObjectName("ChoseTypeBox")
        self.ChoseTypeBox.addItem("")
        self.ChoseTypeBox.addItem("")
        self.frameBlanc.raise_()
        self.AppliquerBtn.raise_()
        self.frame_2.raise_()
        self.NotifsBoxPanel.addWidget(self.Succes)
        self.CreateNew = QtWidgets.QWidget()
        self.CreateNew.setStyleSheet("QWidget#CreateNew{\n"
"background-color: rgb(239, 239, 239);\n"
"}\n"
"QLabel#ImgFrame,QFrame#frameInfo{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:4px;\n"
"border-color:#fff;\n"
"}")
        self.CreateNew.setObjectName("CreateNew")
        self.ImgFrame = QtWidgets.QLabel(self.CreateNew)
        self.ImgFrame.setGeometry(QtCore.QRect(10, 10, 221, 201))
        self.ImgFrame.setText("")
        self.ImgFrame.setObjectName("ImgFrame")
        self.frameInfo = QtWidgets.QFrame(self.CreateNew)
        self.frameInfo.setGeometry(QtCore.QRect(240, 9, 281, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frameInfo.setFont(font)
        self.frameInfo.setStyleSheet("QLineEdit{\n"
"border:1px solid;\n"
"border-top:none;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-color: rgb(239, 239, 239);\n"
"\n"
"}\n"
"\n"
"QComboBox{\n"
"border:1px solid;\n"
"border-top:none;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-color: rgb(239, 239, 239);\n"
"\n"
"}\n"
"QComboBox:pressed,\n"
"QComboBox:focus,\n"
"QComboBox:on{border-color: rgb(239, 239, 239);}")
        self.frameInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInfo.setObjectName("frameInfo")
        self.StartCamBtn = QtWidgets.QPushButton(self.frameInfo)
        self.StartCamBtn.setGeometry(QtCore.QRect(180, 160, 31, 33))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.StartCamBtn.setFont(font)
        self.StartCamBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/BlancIcone/Images/BlancIcon/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartCamBtn.setIcon(icon2)
        self.StartCamBtn.setObjectName("StartCamBtn")
        self.AddEmployerBtn = QtWidgets.QPushButton(self.frameInfo)
        self.AddEmployerBtn.setGeometry(QtCore.QRect(220, 160, 31, 33))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.AddEmployerBtn.setFont(font)
        self.AddEmployerBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/BlancIcone/Images/BlancIcon/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddEmployerBtn.setIcon(icon3)
        self.AddEmployerBtn.setObjectName("AddEmployerBtn")
        self.lineEditMatricule = QtWidgets.QLineEdit(self.frameInfo)
        self.lineEditMatricule.setGeometry(QtCore.QRect(20, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditMatricule.setFont(font)
        self.lineEditMatricule.setObjectName("lineEditMatricule")
        self.lineEditNom = QtWidgets.QLineEdit(self.frameInfo)
        self.lineEditNom.setGeometry(QtCore.QRect(20, 40, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditNom.setFont(font)
        self.lineEditNom.setObjectName("lineEditNom")
        self.lineEditPrenom = QtWidgets.QLineEdit(self.frameInfo)
        self.lineEditPrenom.setGeometry(QtCore.QRect(20, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditPrenom.setFont(font)
        self.lineEditPrenom.setText("")
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.comboBoxPost = QtWidgets.QComboBox(self.frameInfo)
        self.comboBoxPost.setGeometry(QtCore.QRect(20, 100, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxPost.setFont(font)
        self.comboBoxPost.setStyleSheet("color: rgb(100, 100, 100);")
        self.comboBoxPost.setObjectName("comboBoxPost")
        self.comboBoxPost.addItem("")
        self.comboBoxPost.addItem("")
        self.comboBoxPost.addItem("")
        self.comboBoxPost.addItem("")
        self.comboBoxPost.addItem("")
        self.comboBoxPost.addItem("")
        self.comboBoxPost.addItem("")
        self.comboBoxType = QtWidgets.QComboBox(self.frameInfo)
        self.comboBoxType.setGeometry(QtCore.QRect(20, 130, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxType.setFont(font)
        self.comboBoxType.setStyleSheet("color: rgb(100, 100, 100);")
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.msg = QtWidgets.QLabel(self.frameInfo)
        self.msg.setGeometry(QtCore.QRect(20, 169, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg.setFont(font)
        self.msg.setStyleSheet("color: rgb(0, 145, 0);")
        self.msg.setObjectName("msg")
        self.NotifsBoxPanel.addWidget(self.CreateNew)
        self.Danger = QtWidgets.QWidget()
        self.Danger.setObjectName("Danger")
        self.NotifsBoxPanel.addWidget(self.Danger)
        self.verticalLayout.addWidget(self.NotifsBoxPanel)

        self.retranslateUi(Form)
        self.NotifsBoxPanel.setCurrentIndex(2)
        self.ComprisBtn.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pop-Up"))
        self.label.setText(_translate("Form", "Notification !"))
        self.textBrowserInfo.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#222222;\">Votre bo??te de r??ception est vide pour le moment</span></p></body></html>"))
        self.ComprisBtn.setText(_translate("Form", "C\'est compris"))
        self.AppliquerBtn.setText(_translate("Form", "Appliquer"))
        self.label_2.setText(_translate("Form", "De"))
        self.label_3.setText(_translate("Form", "A"))
        self.ChoseTypeBox.setItemText(0, _translate("Form", "Employ??s"))
        self.ChoseTypeBox.setItemText(1, _translate("Form", "Ouvriers"))
        self.lineEditMatricule.setPlaceholderText(_translate("Form", "Matricule"))
        self.lineEditNom.setPlaceholderText(_translate("Form", "Nom"))
        self.lineEditPrenom.setPlaceholderText(_translate("Form", "Pr??noms"))
        self.comboBoxPost.setItemText(0, _translate("Form", "_Poste_"))
        self.comboBoxPost.setItemText(1, _translate("Form", "Session Bureau"))
        self.comboBoxPost.setItemText(2, _translate("Form", "Session Chauffeur"))
        self.comboBoxPost.setItemText(3, _translate("Form", "Session D??p??t"))
        self.comboBoxPost.setItemText(4, _translate("Form", "Session Entretien"))
        self.comboBoxPost.setItemText(5, _translate("Form", "Session Gardien"))
        self.comboBoxPost.setItemText(6, _translate("Form", "Session Mecanique"))
        self.comboBoxType.setItemText(0, _translate("Form", "_Type_"))
        self.comboBoxType.setItemText(1, _translate("Form", "E"))
        self.comboBoxType.setItemText(2, _translate("Form", "O"))
        self.msg.setText(_translate("Form", "Bienvenue !"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
