import cv2 as cv
import numpy as np
import glob
import copy
import os
from PIL import Image
'''
红色：0 69 160 255 255
蓝色：89 141 255 255 255
'''
COLOR_THRE = 0.1

def pre(src):
    img = copy.copy(src)
    #gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(img, 3)
    out = blur
    return out


def color_rate(src, mode='red'):
    img = copy.copy(src)
    if mode == 'red':
        hmin, hmax, smin, smax, vmin, vmax = (0, 10, 43, 255, 43, 255)
    elif mode == 'blue':
        hmin, hmax, smin, smax, vmin, vmax = (100, 124, 43, 255, 46, 255)
    else:
        return 0
    if img.shape[0]*img.shape[1] == 0:
        return 0

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    dst = cv.inRange(hsv, (hmin, smin, vmin), (hmax, smax, vmax))
    return np.sum(dst > 50)/dst.shape[0]/dst.shape[1]


def split(src, mode, color=None,line=1):
    img = copy.copy(src)
    if mode == 1:  # 背景色差
        span = 23
        decay = 0
        lower = 4
        upper = 32
    elif mode == 2:  # 有圈圈的
        span = 16
        decay = 6
        lower = 5
        upper = 25
    elif mode == 3:  # 有箭头的
        span = 16
        decay = 6
        lower = 5
        upper = 25
    elif mode == 4:  # 倾斜类
        span = 16
        decay = 6
        lower = 2
        upper = 30
    elif mode == 6:  # 多行的
        span = 16
        decay = 4
        lower = 2
        upper = 44
        img = img[lower:upper, decay:]
        img1 = img[2:23, :]
        img2 = img[23:44, :]
        img1 = [img1[:, i*span:i*span+span] for i in range(6)]
        img2 = [img2[:, i*span:i*span+span] for i in range(6)]
        if line == 2:
            return img1
        else:
            img1.extend(img2)
            return img1
    elif mode == 5:  # 正常类
        span = 16
        decay = 6
        lower = 1
        upper = 27
    elif mode == 7:
        pass  # 有大有小
    img = img[lower:upper, decay:]
    imgs = [img[:, i*span:i*span+span] for i in range(6)]
    outs = []
    if color is not None:
        for im in imgs:
            if color_rate(im, mode=color) > COLOR_THRE:
                outs.append(im)
        return outs
    return imgs


'''cv.namedWindow("Trackbar")
def nothing(n):
    pass
cv.createTrackbar("hmin","Trackbar",1,180,nothing)
cv.createTrackbar("hmax","Trackbar",155,180,nothing)
cv.createTrackbar("smin","Trackbar",1,255,nothing)
cv.createTrackbar("smax","Trackbar",155,255,nothing)
cv.createTrackbar("vmin","Trackbar",1,255,nothing)
cv.createTrackbar("vmax","Trackbar",155,255,nothing)'''
if __name__ == '__main__':

    src = cv.imread("/media/xueaoru/DATA/ubuntu/paipai/code/单行/12_8_42.png")
    imgs = split(src, mode=2, color='blue')
    print(len(imgs))
