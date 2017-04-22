#!/usr/bin/env python3

from math import inf, floor
import subprocess

import numpy as np
from PIL import Image as im

with open('dataset_568/filelist.txt', 'r') as flist:
    for f in flist:
        f = f.replace('\n', '')
        imgPath = 'dataset_568/human/' + f + '.png'
        cordPath = 'dataset_568/coordinates/' + f + '_macbeth.txt'
        outputPath = '/tmp/dataset_568_crop/' + f + '.png'

        # get image size
        img = im.open(imgPath)
        iw, ih = img.size

        cord_ratio_x, cord_ratio_y = 0, 0

        # get a minimal rect to cover cord area
        xmin, ymin = inf, inf
        xmax, ymax = 0, 0

        with open(cordPath, 'r') as cords:
            for num, cord in enumerate(cords, 1):
                cord = cord.replace('\n', '')
                x, y = [float(n) for n in cord.split(' ')]

                if num == 1:
                    cord_ratio_x = iw / x
                    cord_ratio_y = ih / y
                    continue

                if x < xmin:
                    xmin = x
                elif x > xmax:
                    xmax = x

                if y < ymin:
                    ymin = y
                elif y > ymax:
                    ymax = y

        # crop offset
        cx, cy = 0, 0
        # crop rect size
        cw, ch = 0, 0

        if (ih - ymax) > (ymin - 0):
           cy = ymax
           ch = ih - ymax
        elif (ih - ymax) <= (ymin - 0):
            cy = 0
            ch = ymin - 0

        if (iw - xmax) > (xmin - 0):
            cx = xmax
            cw = iw - xmax
        elif (iw - xmax) <= (xmin - 0):
            cx = 0
            cw = xmin - 0

        xmin *= cord_ratio_x
        xmax *= cord_ratio_x
        ymin *= cord_ratio_y
        ymax *= cord_ratio_y
        cx *= cord_ratio_x
        cw *= cord_ratio_x
        cy *= cord_ratio_y
        ch *= cord_ratio_y

        print(f, (int(cx),
              int(cy),
              int(floor(cx + cw)),
              int(floor(cy + ch))))
        img.crop((int(cx),
                  int(cy),
                  int(floor(cx + cw)),
                  int(floor(cy + ch))))\
            .resize((256, 256))\
            .save(outputPath)
        img.close()
