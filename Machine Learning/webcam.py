import cv2
import numpy as np

def webcam():
    webcam = cv2.VideoCapture(0)

    while True:

        try:
            check, frame = webcam.read()
            cv2.waitKey(1)
            cv2.imshow('Video', frame)

            if not check:
                continue
            
            image = cv2.resize(frame, (224, 224))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = np.array(image, dtype = np.float32)

            yield image
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            break
        