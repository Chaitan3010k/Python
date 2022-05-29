import cv2
from cv2 import waitKey
image=cv2.imread("poster.jpg")
rocket=image[120:360,400:500]
image[0:240,500:600]=rocket
text1="My Name Is Chaitanya"
cv2.putText(image,  
           text1,
           (20, 220),  
           fontFace=cv2.FONT_ITALIC,
           fontScale=1,  
           color=(0,0,1)
           )
cv2.imshow("output",image)
cv2.waitKey(0)