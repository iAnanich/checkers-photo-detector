import cv2
import numpy as np
from matplotlib import pyplot as plt

from nms import non_max_suppression_fast


OVERLAP_THRESH = 0.1
THRESHOLD = 0.6


def multiple_template_matching(origin, tmp):
    img_gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= THRESHOLD)

    boxes = []
    for pt in zip(*loc[::-1]):
        boxes.append([*pt, pt[0] + w, pt[1] + h])
    pick = non_max_suppression_fast(np.array(boxes), OVERLAP_THRESH)

    for (startX, startY, endX, endY) in pick:
        cv2.rectangle(origin, (startX, startY), (endX, endY), (0, 255, 0), 2)

    return origin


if __name__ == '__main__':
    origin = cv2.imread('example.jpg')
    template = cv2.imread('template.jpg', 0)
    matched = multiple_template_matching(origin, template)
    cv2.imshow('image', matched)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == 1048691:  # wait for 's' key to save and exit
        cv2.imwrite('sample-2.png', matched)
        cv2.destroyAllWindows()
