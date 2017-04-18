import cv2

from sample import show_or_save


CAM_PORT = 0
camera = cv2.VideoCapture(CAM_PORT)


def take_photo():
    for i in range(10):
        camera.read()
    return camera.read()


def run() -> None:
    r, img = take_photo()
    if r:
        show_or_save(img, name='webcam', file='webcam.jpg')


if __name__ == '__main__':
    run()
