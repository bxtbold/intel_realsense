import cv2
import pyrealsense2
from realsense_depth import *

point = (400,300)
color = (200,0,0)
thickness = 5
radius = 5
font = cv2.FONT_HERSHEY_SIMPLEX

dc = DepthCamera()
while True:
    boolean, depth_frame, rgb_frame = dc.get_frame()
    if boolean == False: print("No image detected"); break
    
    cv2.circle(rgb_frame, point, radius, color, thickness)
    distance = depth_frame[point[1], point[0]]
    cv2.putText(rgb_frame, "{}mm".format(distance), (400, 380), font, 2, color, 2)
    cv2.imshow('depth frame', depth_frame)
    cv2.imshow('Point Distance', rgb_frame)
    CLOSE = cv2.waitKey(100)   
    
    if CLOSE == 27:
        break
    