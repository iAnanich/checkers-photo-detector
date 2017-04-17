import cv2

from template import multiple_template_matching


tmp = cv2.imread('template.jpg', 0)
for i in range(58):
    origin = cv2.imread('examples/rgb{}.jpg'.format(i))
    matched = multiple_template_matching(origin, tmp)
    cv2.imshow(str(i), matched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
