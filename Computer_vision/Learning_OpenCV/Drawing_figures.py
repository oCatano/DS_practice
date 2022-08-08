import cv2
import numpy as np

photo = np.zeros((400, 400, 3), dtype=np.uint8)

# Add colors
# Not RGB -> BGR!!!
# Hight x weight not WxH
# photo[100:150, 200:280] = 242, 172, 84

# src, start_point, end_point, color, thickness (format of points: x,y)
# thickness= cv2.FILLED - Full colored rectangle
cv2.rectangle(photo, (100, 0), (250, 100), (242, 172, 84), thickness=4)

cv2.circle(photo, (2*photo.shape[1]//3, 2*photo.shape[0]//3),
           radius=photo.shape[0]//3, color=(242, 172, 84), thickness=4)

# photo.shape - (height, weight)
cv2.line(photo, (0, photo.shape[1]//2), (photo.shape[0]//2,photo.shape[1]//2), thickness=3, color=(242, 172, 84))

cv2.imshow('Generate_photo', photo)
cv2.waitKey(0)
