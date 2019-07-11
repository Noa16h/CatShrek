import os;
import time;
import cv2;
import numpy as np;




video = cv2.VideoCapture(0)


while True:
    
    check,frame = video.read() 

    #h,w = frame.shape
    #im = frame.astype(np.int32)
    im = frame

    print(type(im))
    print(type(frame))
    detector = cv2.SimpleBlobDetector_create()
    print(detector)
    keypoints = detector.detect(im)

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("Capturing", im_with_keypoints )

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()