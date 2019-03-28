import requests
import json
import shutil
from split import *
import os
import constents


def recognize(path=constents.imgPath, description=""):
    print('验证码描述：' + description)
    mode = 5
    img = cv.imread(path)
    imgs = split(img, mode, line=1)

    if not os.path.exists("temp"):
        os.mkdir("temp")
    labels = []
    for idx, img in enumerate(imgs):
        cv.imwrite("temp/{}.png".format(idx), img)
        files = {'images': open("temp/{}.png".format(idx), 'rb')}
        try:
            r = requests.post(constents.url, files=files,
                              headers=constents.headers)
            rr = json.loads(r.text)
            print(r.text)
            labels.append(rr["predicted_label"])
        except:
            labels.append('-')
    return "".join(labels)
