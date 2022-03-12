# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:50:41 2021

@author: suhedaras
"""

import cv2
import dlib
from scipy.spatial import distance

# Euclidean distance ((x1-x2)^2 -(y1-y2)^2)^1/2


def calculate_EAR(eye):

    a = distance.euclidean(eye[1], eye[5])
    b = distance.euclidean(eye[2], eye[4])
    c = distance.euclidean(eye[0], eye[3])
    ear = (a+b)/(2.0 * c)
    return ear


def calculate_MOR(mouth_landmarks):
    d = distance.euclidean(mouth_landmarks[1], mouth_landmarks[7])
    e = distance.euclidean(mouth_landmarks[2], mouth_landmarks[6])
    f = distance.euclidean(mouth_landmarks[3], mouth_landmarks[5])
    g = distance.euclidean(mouth_landmarks[0], mouth_landmarks[4])
    mor = (d + e + f) / (2.0 * g)
    return mor


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    frame_check = 20
    flag = 0

    face_detector = dlib.get_frontal_face_detector()
    face_landmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    while True:

        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector(gray)

        for face in faces:

            face_landmark_gray: None = face_landmark(gray, face)
            leftEye = []
            rightEye = []
            mouth = []

            for n in range(36, 42):
                x = face_landmark_gray.part(n).x
                y = face_landmark_gray.part(n).y
                leftEye.append((x, y))
                next_point = n + 1
                if n == 41:
                    next_point = 36
                x2 = face_landmark_gray.part(next_point).x
                y2 = face_landmark_gray.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

            for n in range(42, 48):
                x = face_landmark_gray.part(n).x
                y = face_landmark_gray.part(n).y
                rightEye.append((x, y))
                next_point = n + 1
                if n == 47:
                    next_point = 42
                x2 = face_landmark_gray.part(next_point).x
                y2 = face_landmark_gray.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

            for n in range(60, 68):
                x = face_landmark_gray.part(n).x
                y = face_landmark_gray.part(n).y
                mouth.append((x, y))
                next_point = n + 1
                if n == 67:
                    next_point = 60
                x2 = face_landmark_gray.part(next_point).x
                y2 = face_landmark_gray.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 0, 255), 1)

            left_ear = calculate_EAR(leftEye)
            right_ear = calculate_EAR(rightEye)

            EAR = (left_ear + right_ear) / 2
            EAR = round(EAR, 2)

            MOR = calculate_MOR(mouth)
            MOR = round(MOR, 2)

            cv2.putText(frame, "EAR: {}".format(EAR), (510, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, "MOR: {}".format(MOR), (510, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            if MOR > 0.70:
                cv2.putText(frame, "You are yawning. Are you drowsy?", (5, 75),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            if EAR < 0.22:
                flag += 1
                if flag > frame_check:
                    cv2.putText(frame, "DROWSINESS ALERT", (25, 125),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                if flag == frame_check:
                    pass
            else:
                flag = 0

        cv2.imshow("Drowsy Detector", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


