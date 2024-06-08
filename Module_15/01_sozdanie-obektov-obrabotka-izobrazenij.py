import numpy as np
import cv2


image = np.zeros((450, 450, 3), dtype='uint8')
cntr = image.shape[0] // 2

for i in range(0, 450):
    image[0:450, i:i+1] = i // 2, i // 2, i // 2

for i in (50, 90):
    cv2.circle(image, (cntr, cntr), i, (0, 170, 0), thickness=5)

for i in range(0, 450):
    image[0:225, i:i+1] = i // 2, i // 2, i // 2

for i in (-90, -50, 50, 90):
    cv2.line(image, (cntr + i, cntr), (cntr + i, cntr - 100), (170, 0, 0), thickness=5)

for i in (((135, 125), (175, 125)), ((275, 125), (315, 125))):
    cv2.line(image, *i, (0, 0, 170), thickness=5)

cv2.circle(image, (cntr, cntr), 200, (255, 255, 255), thickness=5)


cv2.imshow('URBAN', image)
cv2.waitKey(0)
