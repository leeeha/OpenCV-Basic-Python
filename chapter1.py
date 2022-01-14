import cv2
import numpy as np

# 이미지는 단지 픽셀로 이루어진 배열, 행렬이다.

img = cv2.imread("Resources/lena.jpg")
print(img.shape) # 높이, 너비, BGR 채널 번호

imgResize = cv2.resize(img, (200, 200))
print(imgResize.shape)

imgCropped = img[0:100, 100:200] # 높이, 너비 [시작점: 끝점]
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Crop", imgCropped)

cv2.waitKey(0)
