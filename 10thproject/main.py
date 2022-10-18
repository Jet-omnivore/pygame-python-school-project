import numpy as np
import sys
import cv2
import enum
import json

class KEY(enum.Enum):
    ESC = 27

WIDTH = 640
HEIGHT = 480

def readAndEvaluateConfigFile(path):
    with open(path) as config_file:
        data = json.loads(config_file.read()) 
        data = {int(k): v for k, v in data.items()}
    return data

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

names_data = readAndEvaluateConfigFile("config.json")
      

cap = cv2.VideoCapture("http://192.168.15.82:4747/video")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


while True:
    success, frame = cap.read()   

    if not success:
        print("Success variable error! Most probably camera not found!")
        break

    frame = cv2.flip(frame, -1)     # flip frame vertically!!!
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = faceCascade.detectMultiScale(
            gray_frame,
            scaleFactors=1.2,
            minNeighbours=5,
            minSize=(20, 20)
            )

    for x_pos, y_pos, width, height in detected_faces:
        # cv2.rectangle(image, start pos, end pos, color, thickness)
        cv2.rectangle(frame, (x_pos, y_pos), (x_pos + width, y_pos + height), (255, 0, 0), 2)
        face_id, confidence = face_recognizer.predict(gray_frame[y_pos : y_pos + height, x_pos : x_pos + width]) 

        name = "unknown"
        text_confidence = "  {0}%".format(round(100 - confidence))
        if confidence < 100:
            name = names_data[face_id]

        cv2.putText(
                    frame, 
                    str(name), 
                    (x_pos + 5, y_pos-5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (255,255,255), 
                    2)

        cv2.putText(
                    frame, 
                    str(text_confidence), 
                    (x_pos + 5,y_pos + height-5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (255,255,0), 
                    1)

    cv2.imshow('camera', frame)

    key = cv2.waitkey(30) & 0xff
    if key in [KEY.ESC]:
        break 

cap.release()
cv2.destroyAllWindows()
