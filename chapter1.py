import cv2
import numpy as np

print("Package Imported")

img = cv2.imread("Resources/lena.jpg")
kernel = np.ones((5, 5), np.uint8) # 행렬의 크기, 8비트 integer (0~255)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200) # canny edge detector (이미지의 윤곽선 감지)

# dilation(팽창), canny 이미지의 윤곽선을 두껍게
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# erosion(부식, 침식), dialation 이미지의 윤곽선을 얇게
imgErosion = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erosion Image", imgErosion)

cv2.waitKey(0)
