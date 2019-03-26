import requests
import json
import shutil
from split import *
import os
import constents


def recognize(path=constents.imgPath, mode=1):
    img = cv.imread(path)
    imgs = split(img, mode, color="red", line=1)

    if not os.path.exists("temp"):
        os.mkdir("temp")
    labels = []
    for idx, img in enumerate(imgs):
        cv.imwrite("temp/{}.png".format(idx), img)
        files = {'images': open("temp/{}.png".format(idx), 'rb')}
        r = requests.post(constents.url, files=files,
                          headers=constents.headers)
        rr = json.loads(r.text)
        print(r.text)
        labels.append(rr["predicted_label"])
    return "".join(labels)
