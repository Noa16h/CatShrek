import os;
import time;
import cv2;




video = cv2.VideoCapture(0)

check,frame = video.read()

cv2.imshow("Capturing", frame)

cv2.waitKey('o')

video.release()