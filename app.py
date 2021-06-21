import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Store a single frame as bg
_, background = cap.read()

background = cv2.flip(background, 1)

time.sleep(2)

_, background = cap.read()

background = cv2.flip(background, 1)

# Define all the kernals size
open_kernal = np.ones((5,5), np.uint8)

close_kernal = np.ones((7,7), np.uint8)

dilation_kernal = np.ones((10,10), np.uint8)

# Func for remove noise from mask
def filter_mask(mask):

    close_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernal)

    open_mask = cv2.morphologyEx(close_mask, cv2.MORPH_OPEN, open_kernal)

    dilation = cv2.dilate(open_mask, dilation_kernal, iterations=1)

    return dilation

while cap.isOpened():
    _, frame = cap.read()

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # RED ([50,119,0],[179,255,255])
    lower = np.array([50,119,0])
    upper = np.array([179,255,255])

    mask = cv2.inRange(hsv, lower, upper) # defind area color 

    mask = filter_mask(mask)

    magic = cv2.bitwise_and(background, background, mask=mask)

    inverse_mask = cv2.bitwise_not(mask)

    current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    combined = cv2.add(magic, current_background)

    cv2.imshow("RESULT", combined)

    if cv2.waitKey(1) == ord('q'):
        break