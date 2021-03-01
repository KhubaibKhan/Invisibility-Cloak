import numpy as np
import cv2

import time

def empty(x):
    pass


time.sleep(1)
cap = cv2.VideoCapture(0)

background = 0
for i in range(30):
    ret, background = cap.read()



background = np.flip(background, axis=1)
while 1:
    ret, img = cap.read(0)
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min, h_max, s_min, s_max, val_min, val_max = 0, 179, 0, 28, 85, 255
    lower = np.array([h_min, s_min, val_min])
    upper = np.array([h_max, s_max, val_max])
    mask1 = cv2.inRange(hsv, lower, upper)


    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility cloak: ", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()





