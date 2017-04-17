import cv2
import numpy as np
from matplotlib import pyplot as plt

from nms import non_max_suppression_fast


overlapThresh = 0.1
threshold = 0.5


def multiple_template_matching(origin, tmp, matched):
    img_rgb = cv2.imread(origin)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(tmp, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    boxes = []
    for pt in zip(*loc[::-1]):
        boxes.append([*pt, pt[0] + w, pt[1] + h])
    pick = non_max_suppression_fast(np.array(boxes), overlapThresh)

    for (startX, startY, endX, endY) in pick:
        cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 255, 0), 2)

    cv2.imwrite(matched, img_rgb)


if __name__ == '__main__':
    inputName = 'example.jpg'
    outputName = 'matched.jpg'
    templateName = 'template.png'
    multiple_template_matching(inputName, templateName, outputName)
