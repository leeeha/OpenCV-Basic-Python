import cv2
import numpy as np

img = cv2.imread("Resources/pill.jpg")

width, height = 400, 250 # 변환 후 가로, 세로 길이
pts1 = np.float32([[1137, 1193], [2553, 2113], [377, 1777], [1793, 2993]]) # 네 모서리 점의 좌표
pts2 = np.float32([[0,0], [width,0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2) # 선형변환을 위한 행렬 얻기
imgOutput = cv2.warpPerspective(img, matrix, (width, height)) # 변환 행렬 적용

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)
