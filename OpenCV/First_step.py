import cv2


def open_img():
    # Work with images
    img = cv2.imread('img/communicate.png')

    cv2.imshow('Result', img)
    cv2.waitKey(0)


def open_video(path=0):
    # Open my videos
    # cap = cv2.VideoCapture('videos/first_step.mp4')

    # Open web cam (ind -> num of camera)
    cap = cv2.VideoCapture(path)

    while True:
        success, img = cap.read()
        cv2.imshow('Your_video', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def reshape_img():
    img = cv2.imread('img/communicate.png')
    a, b = img.shape[:2]
    # Change size of img
    new_img = cv2.resize(img, (b // 2, a // 2))

    # Blur
    new_img = cv2.GaussianBlur(new_img,(9,9),0)

    # Change format from RGB to Black and White
    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

    # Find all corners (ищет контуры)
    # Params lower params = more details
    new_img = cv2.Canny(new_img, 30, 30)

    # Cut picture using arr
    # cv2.imshow('Result', new_img[0:400, 0:650])
    cv2.imshow('Result', new_img)
    cv2.waitKey(0)

reshape_img()