import numpy as np
import cv2

black=np.zeros([600,600])
#print(black)
black[200:400, 200:400]=255
print(black)

cv2.imshow("black",black)
cv2.waitKey(0)