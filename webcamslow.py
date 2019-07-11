import os;
import time;
import cv2;
import numpy as np;

class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self,size_max):
        self.max = size_max
        self.idx = 0
        self.data = []

    def append(self,x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0

    def insert(self,x):
        self.data[self.cur] = x
        self.cur = (self.cur+1) % self.max

    def getNext(self):
        item = self.data[self.idx]
        self.idx = (self.idx+1) % self.max
        return item

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data



video = cv2.VideoCapture(0)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 255

params.filterByColor = True
params.blobColor = 255


# Filter by Area.
params.filterByArea = True
params.minArea = 100
params.maxArea = 1500

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)


#buffer = RingBuffer(10)

#for i in range(10):
#    _,frameA = video.read()
#    buffer.append(frameA)
_,lastFrame = video.read()

while True:
    check,frame = video.read() 


    im = frame
    #h,w = frame.shape
    #im = frame.astype(np.int32)
    target = None
    #second = buffer.getNext()
    second = lastFrame
    lastFrame = frame
    #print(type(second))
    diff = cv2.absdiff(second,im)
    
    #buffer.insert(frame)
    grayImage = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    (thresh, imask) = cv2.threshold(grayImage, 40, 255, cv2.THRESH_BINARY)
    im = diff
    
    th = 1
    #imask = mask>th
    im = imask
    

    keypoints = detector.detect(im)
    if len(keypoints)!= 0:
       print("detected")

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("Capturing", im_with_keypoints )

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()