import cv2
import numpy as np


def open_img():
    # Work with images
    img = cv2.imread('../img/communicate.png')

    cv2.imshow('Result', img)
    cv2.waitKey(0)


def open_video(path=0):
    # Open my videos
    # cap = cv2.VideoCapture('../videos/first_step.mp4')

    # Open web cam (ind -> num of camera)
    cap = cv2.VideoCapture(path)

    while True:
        success, img = cap.read()
        cv2.imshow('Your_video', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def reshape_img(show=True, path='../img/communicate.png'):
    """
    \
    :param show: True for showing pic, False to not
    :param path: way to picture
    :return: reshaped picture
    """
    img = cv2.imread(path)
    a, b = img.shape[:2]
    # Change size of img
    new_img = cv2.resize(img, (b // 2, a // 2))

    # Cut picture using arr
    # cv2.imshow('Result', new_img[0:400, 0:650])
    if show:
        cv2.imshow('Result', new_img)
        cv2.waitKey(0)
    return new_img


def prepare_pic(show=True, path='../img/communicate.png'):
    """
    \
    :param show: True for showing pic, False to not
    :param path: Way to picture
    :return: Blured, Gray, and Canny pic
    """
    img = cv2.imread(path)

    # Blur
    new_img = cv2.GaussianBlur(img, (9, 9), 0)

    # Change format from RGB to Black and White
    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

    # Find all corners (ищет контуры)
    # Params lower params = more details
    new_img = cv2.Canny(new_img, 100, 100)

    kernel = np.ones((5, 5), np.uint8)
    new_img = cv2.dilate(new_img, kernel, iterations=1)

    new_img = cv2.erode(new_img, kernel, iterations=1)

    if show:
        cv2.imshow('Result', new_img)
        cv2.waitKey(0)

    return new_img


# cv2.imwrite('../img/communicate.png', reshape_img())
prepare_pic()
