import time

import cv2
import numpy as np


cap = cv2.VideoCapture('sample.mp4')
# cap = cv2.VideoCapture(0)
eyes = cv2.CascadeClassifier('eyes.xml')
mask = np.zeros(cap.read()[1].shape[:2], dtype=np.uint8)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    find_eyes = eyes.detectMultiScale(gray, scaleFactor=3.5, minNeighbors=10)
    gray = cv2.GaussianBlur(gray, (1, 91), 0, sigmaY=91)
    if len(find_eyes) > 1:
        mask[:] = 0
        cur = []
        for x, y, w, h in find_eyes:
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), thickness=3)
            cur.append((x, y))
            cur.append((x + w, y + h))
        eyes_xy = ((min(cur)[0] - 50, min(cur, key=lambda el: el[1])[1]),
                   (max(cur)[0] + 50, max(cur, key=lambda el: el[1])[1]))
        cv2.rectangle(mask, *eyes_xy, (255, ), thickness=-1)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    gray = cv2.bitwise_and(gray, gray, mask=mask)
    img = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))
    result = cv2.bitwise_or(img, gray)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Gray', gray)
    # cv2.imshow('IMG', img)
    cv2.imshow('Result', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
