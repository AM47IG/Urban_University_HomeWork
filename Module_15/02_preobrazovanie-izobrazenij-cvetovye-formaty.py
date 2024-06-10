import cv2
import numpy as np


img = cv2.imread('img.png')
img2 = cv2.imread('img.png')
img = img[0:480, 0:730]
new_img = np.zeros(img.shape, np.uint8)

img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 10, 20)
kernel = np.ones((2, 2), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for i in range(83):
    cv2.drawContours(new_img, con, i, (225, 20, 210))
for i in range(83, 165):
    cv2.drawContours(new_img, con, i, (20, 76, 225))
for i in range(165, 252):
    cv2.drawContours(new_img, con, i, (20, 225, 25))

cv2.imshow('Res', new_img)
cv2.waitKey(0)
