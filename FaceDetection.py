import cv2,os
import mediapipe as mp
import face_recognition
import numpy as np
from Functions.pointage import Pointage
from Functions.employer import Employer
from datetime import date,datetime
#Face mesh
Pointage = Pointage()
Employer = Employer()
"""Il faut toujours créer la liste ClassName = [] avant l'execution de la fonction FindEncodingImage"""

ClassName = []
def FindEncodingImage():
    Images = []
    global ClassName
    for cl in os.listdir("know"):
        curImg = cv2.imread(f"know/{cl}")
        Images.append(curImg)
        ClassName.append(os.path.splitext(cl)[0])
    curImg = cv2.imread(f"know/{cl}")
    Images.append(curImg)
    ClassName.append(os.path.splitext(cl)[0])
    EncodingImage = []
    for img in Images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        Encode = face_recognition.face_encodings(img)[0]
        EncodingImage.append(Encode)
    return EncodingImage

###################

FaceMesh = mp.solutions.face_mesh.FaceMesh()
EncodeListKnow = FindEncodingImage()

Cap = cv2.VideoCapture(0)
def StartCamera():

    while True:
        Ret, Image = Cap.read()
        # try:
        Height, Width, _ = Image.shape
        RgbImage = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        FaceCurFrame = face_recognition.face_locations(Image)
        encodeCurFrame = face_recognition.face_encodings(Image, FaceCurFrame)
        #
        for EncodeFace, FaceLoc in zip(encodeCurFrame, FaceCurFrame):
            Matches = face_recognition.compare_faces(EncodeListKnow, EncodeFace)
            FaceDis = face_recognition.face_distance(EncodeListKnow, EncodeFace)
            MatchesIndex = np.argmin(FaceDis)
            if Matches[MatchesIndex] and min(FaceDis) < 0.375:
                Name = ClassName[MatchesIndex].upper()
                Metric = min(FaceDis)
                Nom = Name.split("-")[0]
                Matricul = str(Name.split("-")[1])
                Data = (Nom,Matricul,date.today(),datetime.now().strftime("%H:%M:%S"))
                if Employer.GetEmployerCategorieByMatricule(Matricul) == "E":
                    if Pointage.GetHeureDeConnexionByMatricule(Matricul,"E") == 2:
                        if Pointage.PointageJournalier1(Data) == 0:
                            Pointage.Pointage(Matricul)
                            Pointage.AlertSystem()
                    elif Pointage.GetHeureDeConnexionByMatricule(Matricul,"E") == 0 and Pointage.VerifyP2(Matricul) ==0:
                        if Pointage.PointageJournalie2(Matricul) == 0:
                            if Pointage.Synchronisation(Matricul,"E") == 0:
                                Pointage.AlertSystem()

                elif Employer.GetEmployerCategorieByMatricule(Matricul) == "O":
                    if Pointage.GetHeureDeConnexionByMatricule(Matricul,"O") == 2:
                        if Pointage.PointageHeure1(Data) == 0:
                            Pointage.Pointage(Matricul)
                            Pointage.AlertSystem()
                    elif Pointage.GetHeureDeConnexionByMatricule(Matricul,"O") == 0 and Pointage.VerifyH2(Matricul) == 0:
                        if Pointage.PointageHeure2(Matricul) == 0:
                            if Pointage.Synchronisation(Matricul, "O") == 0:
                                Pointage.AlertSystem()
        # except:
        #     ...

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
        cv2.imshow("Pointage Intelligent", Image)
        key = cv2.waitKey(1)
        # if we press
        if key == 27:
            cv2.destroyAllWindows()
            break


