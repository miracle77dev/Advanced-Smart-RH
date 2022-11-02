import os
import cv2
import face_recognition



Path = "know/RONALDINHO - 45556.png"
Path2 = "know/MANI - 41.png"

image = face_recognition.load_image_file(Path2)
face_locations = face_recognition.face_locations(image)



print(face_locations)