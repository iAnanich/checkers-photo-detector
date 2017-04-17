import cv2


def run():
    img = cv2.imread('sample-1.jpg',0)
    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == 1048691:  # wait for 's' key to save and exit
        cv2.imwrite('sample-2.png',img)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
