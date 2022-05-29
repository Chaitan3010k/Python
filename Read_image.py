import cv2
from cv2 import imread
from cv2 import waitKey
image=cv2.imread("butterfly.jpg")
cv2.imshow("displayimg",image)
#print(image)
grayImage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscaleImg",grayImage)
print(grayImage)
waitKey(00000)
