import cv2


cap = cv2.VideoCapture('sample.mp4')
eyes = cv2.CascadeClassifier('eyes.xml')

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = eyes.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), thickness=3)

    cv2.imshow('Result', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
