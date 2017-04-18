import cv2


def show_or_save(image, name: str='image', file: str='latest.jpg'):
    cv2.imshow(name, image)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == 1048691:  # wait for 's' key to save and exit
        cv2.imwrite(file, image)
        cv2.destroyAllWindows()


def run():
    img = cv2.imread('sample-1.jpg')
    show_or_save(img, file='sample-2.jpg')


if __name__ == '__main__':
    run()
