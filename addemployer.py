import cv2,os,sys

Cap = cv2.VideoCapture(0)
def StartCamera():


    while True:
        Ret, Image = Cap.read()
        Height, Width, _ = Image.shape
        RgbImage = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        FaceCurFrame = face_recognition.face_locations(Image)
        encodeCurFrame = face_recognition.face_encodings(Image, FaceCurFrame)

        cv2.imshow("Pointage Intelligent", Image)
        key = cv2.waitKey(1)
        # if we press esc
        if key == 27:
            cv2.destroyAllWindows()
            break
StartCamera()