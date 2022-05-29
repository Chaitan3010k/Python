import cv2
vid = cv2.VideoCapture("video.mp4")
if(vid.isOpened()==False):
    print("Unable To Load A Video.....")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) 
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS)) 
print(fps)

while(True):
    rate,frame=vid.read()
    cv2.imshow("webcam",frame)
    
    if cv2.waitKey(25)==32:
        break
    
vid.release()
cv2.destroyAllWindows()