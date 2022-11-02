from PyQt5 import QtCore, QtGui, QtWidgets
from pointeur import Ui_MainWindow
import cv2,os
#####################
import mediapipe as mp
import face_recognition
import numpy as np
from datetime import datetime
#####################
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ClassName = []

        #
        self.Ui.OkBtn.clicked.connect(self.ClosePointFrame)

    def ClosePointFrame(self):
        try:
            self.Cap.release()
            cv2.destroyAllWindows()
            self.close()
        except AttributeError:
            pass

    def FindEncodingImage(self):
        Images = []
        for cl in os.listdir("know"):
            curImg = cv2.imread(f"know/{cl}")
            Images.append(curImg)
            self.ClassName.append(os.path.splitext(cl)[0])
        curImg = cv2.imread(f"know/{cl}")
        Images.append(curImg)
        self.ClassName.append(os.path.splitext(cl)[0])
        EncodingImage = []
        for img in Images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            Encode = face_recognition.face_encodings(img)[0]
            EncodingImage.append(Encode)
        return EncodingImage

    def StartCamera(self):
        FaceMesh = mp.solutions.face_mesh.FaceMesh()
        EncodeListKnow = self.FindEncodingImage()

        self.Cap = cv2.VideoCapture(0)
        e= 0
        while True:
            Ret, Image = self.Cap.read()
            self.DisplayImage(Image)
            Height, Width, _ = Image.shape
            RgbImage = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)

            FaceCurFrame = face_recognition.face_locations(Image)
            encodeCurFrame = face_recognition.face_encodings(Image, FaceCurFrame)

            for EncodeFace, FaceLoc in zip(encodeCurFrame, FaceCurFrame):
                Matches = face_recognition.compare_faces(EncodeListKnow, EncodeFace)
                FaceDis = face_recognition.face_distance(EncodeListKnow, EncodeFace)
                MatchesIndex = np.argmin(FaceDis)

                if Matches[MatchesIndex] and min(FaceDis) < 0.375:
                    now = datetime.now()
                    Time = now.strftime("%H:%M:%S")
                    Name = self.ClassName[MatchesIndex].upper()
                    Metric = min(FaceDis)
                    Nom = Name.split("-")[0]
                    Matricul = Name.split("-")[1]
                    self.Ui.labelHello.setText("HELLO M.")
                    self.Ui.labelMatricule.setText("MATRICULE")
                    self.Ui.labelMetric.setText("METRIC")
                    self.Ui.labelStart.setText("Start")
                    self.Ui.labelNom.setText(Nom)
                    self.Ui.labelValeurMatricule.setText(Matricul)
                    self.Ui.labelValeurMetric.setText(str(Metric))
                    self.Ui.labelValeurTemps.setText(Time)
                    self.Ui.OkBtn.setText("Parfait !")
                    e=0

                else:
                    e+=1
                    if e >= 10:
                        self.Ui.OkBtn.setText("Employer non réconnu par le système ")
                        self.Ui.labelHello.setText("XXXXX")
                        self.Ui.labelMatricule.setText("XXXXX")
                        self.Ui.labelMetric.setText("XXXXX")
                        self.Ui.labelStart.setText("XXXXX")
                        self.Ui.labelNom.setText("XXXXX")
                        self.Ui.labelValeurMatricule.setText("XXXXX")
                        self.Ui.labelValeurMetric.setText(str("XXXXX"))
                        self.Ui.labelValeurTemps.setText("XXXXX")
                    else:
                        self.Ui.OkBtn.setText("Identification en cours... ")
                        self.Ui.labelHello.setText("XXXXX")
                        self.Ui.labelMatricule.setText("XXXXX")
                        self.Ui.labelMetric.setText("XXXXX")
                        self.Ui.labelStart.setText("XXXXX")
                        self.Ui.labelNom.setText("XXXXX")
                        self.Ui.labelValeurMatricule.setText("XXXXX")
                        self.Ui.labelValeurMetric.setText(str("XXXXX"))
                        self.Ui.labelValeurTemps.setText("XXXXX")

            # Facial landmarks

            try:
                Result = FaceMesh.process(RgbImage)
                for FacialLandMarks in Result.multi_face_landmarks:
                    for i in range(0, 468):
                        pt1 = FacialLandMarks.landmark[i]
                        x = int(pt1.x * Width)
                        y = int(pt1.y * Height)

                        cv2.circle(Image, (x, y), 2, (100, 100, 0), -1)
            except:
                pass
            cv2.waitKey(1)
            cv2.destroyAllWindows()

    def DisplayImage(self,Img):

        if len(Img.shape) == 3:
            if Img.shape[2] == 4:
                QFormat = QtGui.QImage.Format_RGBA8888
            else:
                QFormat = QtGui.QImage.Format_RGB888
            Img = QtGui.QImage(Img,Img.shape[1],Img.shape[0],QFormat)
            Img = Img.rgbSwapped()
            self.Ui.CaptureLabel.setPixmap(QtGui.QPixmap.fromImage(Img))
            self.Ui.CaptureLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)



if __name__ == "__main__":
    import sys
    App = QtWidgets.QApplication([])
    Win = Main()
    Win.show()
    Win.StartCamera()
    sys.exit(App.exec_())