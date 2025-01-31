import sys
import time
import cv2
import numpy as np
import dlib
from imutils import face_utils
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

# Append system path for external libraries
sys.path.append('/usr/lib/python3/dist-packages')

# Initialize face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Setup GPIO pins
buzzPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)

def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2
    elif 0.21 <= ratio <= 0.25:
        return 1
    else:
        return 0

def call_lcd(value):
    GPIO.setmode(GPIO.BCM)
    lcd = LCD.Adafruit_CharLCD(12, 7, 8, 25, 24, 23, 0, 16, 2)
    lcd.clear()
    messages = {
        1: "SLEEPING!!",
        2: "Drowsy!!",
        3: "Active",
        5: "Turning on..",
        6: "Welcome",
    }
    lcd.message(messages.get(value, "Face not detected!!"))
    if value in [5, 6]:
        time.sleep(3)

# Start capturing video
cap = cv2.VideoCapture(0)

try:
    call_lcd(6)
    call_lcd(5)
    sleep, drowsy, active = 0, 0, 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        face_frame = frame.copy()

        for face in faces:
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            left_blink = blinked(*landmarks[36:42])
            right_blink = blinked(*landmarks[42:48])

            if left_blink == 0 or right_blink == 0:
                sleep += 1
                drowsy = 0
                active = 0
                if sleep > 6:
                    call_lcd(1)
                    status = "SLEEPING !!!"
                    GPIO.output(buzzPin, 1)
                    color = (0, 0, 255)
            elif left_blink == 1 or right_blink == 1:
                sleep = 0
                active = 0
                drowsy += 1
                if drowsy > 6:
                    call_lcd(2)
                    status = "DROWSY !"
                    GPIO.output(buzzPin, 1)
                    color = (0, 0, 255)
            else:
                drowsy = 0
                sleep = 0
                active += 1
                if active > 6:
                    call_lcd(3)
                    GPIO.output(buzzPin, 0)
                    status = "Active :)"
                    color = (0, 255, 0)

            cv2.putText(face_frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
            for (x, y) in landmarks:
                cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

        cv2.imshow("Frame", frame)
        cv2.imshow("Result of detector", face_frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

except KeyboardInterrupt:
    print("Exiting program")
finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
