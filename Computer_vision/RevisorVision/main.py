import cv2
import numpy as np
import shutil
from os import listdir
from os.path import isfile, join


def get_images():
    cap = cv2.VideoCapture('Camera.mp4')
    # cap = cv2.VideoCapture(0)
    counter = 0
    while True:
        _, frame = cap.read()
        if frame is None:
            break
        counter += 1
        if counter % 15 == 0:
            path = './images/img' + str(counter // 15) + '.jpeg'
            print(path)
            frame = frame[210:446, 115:351]
            print(frame.shape)
            frame = cv2.resize(frame, (116, 116))

            cv2.imwrite(path, frame)


# 60 per sec
# 23796 - 6:30:18 = 23418
# x - 10321
# x = 10487
# 9483 - 9876
def test():
    cap = cv2.VideoCapture('Camera.mp4')
    counter = 0
    while True:
        _, frame = cap.read()
        if frame is None:
            break
        counter += 1
        if counter % 15 == 0:
            cv2.imshow("img", frame)
            cv2.waitKey(1)
            print(counter)


def move(start, stop, target='./Empty_table'):
    source_dir = './images/'
    target_dir = target

    file_names = [f"img{n}.jpeg" for n in range(start, stop + 1)]

    for file_name in file_names:
        shutil.move(source_dir + file_name, target_dir)


def to_gray():
    onlyfiles = [f for f in listdir('./Empty_table') if isfile(join('./Empty_table', f))]
    for file in onlyfiles:
        gray = cv2.cvtColor(cv2.imread(f'./Empty_table/{file}'), cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"./images/Gray_Empty_table/{file}", gray)

    onlyfiles = [f for f in listdir('./Positive_target') if isfile(join('./Positive_target', f))]
    for file in onlyfiles:
        gray = cv2.cvtColor(cv2.imread(f'./Positive_target/{file}'), cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"./images/Gray_Positive_target/{file}", gray)


def Gauss_blur():
    onlyfiles = [f for f in listdir('./Empty_table') if isfile(join('./Empty_table', f))]
    for file in onlyfiles:
        blur = cv2.GaussianBlur(cv2.imread(f'./Empty_table/{file}'), (5, 5), 0)
        cv2.imwrite(f"./images/Blur_Empty_table/{file}", blur)

    onlyfiles = [f for f in listdir('./Positive_target') if isfile(join('./Positive_target', f))]
    for file in onlyfiles:
        blur = cv2.GaussianBlur(cv2.imread(f'./Positive_target/{file}'), (5, 5), 0)
        cv2.imwrite(f"./images/Blur_Positive_target/{file}", blur)

    onlyfiles = [f for f in listdir('./images/Gray_Empty_table') if isfile(join('./images/Gray_Empty_table', f))]
    for file in onlyfiles:
        blur = cv2.GaussianBlur(cv2.imread(f'./images/Gray_Empty_table/{file}'), (5, 5), 0)
        cv2.imwrite(f"./images/Blur_Gray_Empty_table/{file}", blur)

    onlyfiles = [f for f in listdir('./images/Gray_Positive_target') if isfile(join('./images/Gray_Positive_target', f))]
    for file in onlyfiles:
        blur = cv2.GaussianBlur(cv2.imread(f'./images/Gray_Positive_target/{file}'), (5, 5), 0)
        cv2.imwrite(f"./images/Blur_Gray_Positive_target/{file}", blur)


def RGB_BLUR_jpeg():
    onlyfiles = [f for f in listdir('./images/Blur_Empty_table') if isfile(join('./images/Blur_Empty_table', f))]
    for file in onlyfiles:
        save_file = cv2.imread(f'./images/Blur_Empty_table/{file}')
        save_file = cv2.cvtColor(save_file,cv2.COLOR_BGR2RGB)
        cv2.imwrite(f'./FinalDatasetPhotos/Negative/{file}', save_file)

    onlyfiles = [f for f in listdir('./images/Blur_Positive_target') if isfile(join('./images/Blur_Positive_target', f))
                 ]
    for file in onlyfiles:
        save_file = cv2.imread(f'./images/Blur_Positive_target/{file}')
        save_file = cv2.cvtColor(save_file, cv2.COLOR_BGR2RGB)
        cv2.imwrite(f'./FinalDatasetPhotos/Positive/{file}', save_file)




# RGB_BLUR_jpeg()


# to_gray()
# Gauss_blur()
#
# pic = cv2.imread("./Empty_table/img1.jpeg")
# gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("./images/Gray_Empty_table/test.jpeg", gray)


# move(24193, 24572,  target='./Positive_target')
# move(24573, 37683)
