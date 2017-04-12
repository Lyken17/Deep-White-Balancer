#!/usr/bin/env python3
#use do_calculate_ambient.sh for batch processing

import numpy as np
import argparse
from PIL import Image as im


parser = argparse.ArgumentParser(description='calculate ambient data')

parser.add_argument('original_image',
        default='Grayball11346_clip_resize/ApacheTrail/00000.jpg')

parser.add_argument('adjusted_image',
        default='Grayball11346_clip_resize_proceed/ApacheTrail/00000.jpg')

parser.add_argument('output',
        default='Grayball11346_clip_resize_data/ApacheTrail/00000.jpg.npy')

args = parser.parse_args()

org = im.open(args.original_image)
adj = im.open(args.adjusted_image)
out = args.output

w, h = org.size[0], org.size[1]

# 3 channel(r,g,b) for each pixel
res = np.zeros((w, h, 3))

for y in range(0, h):
    for x in range(0, w):
        p_org = org.getpixel((x, y))
        p_adj = adj.getpixel((x, y))

        # + 1 to avoid zero ZeroDivisionError
        res[x][y][0] = (p_org[0] + 1) / (p_adj[0] + 1)
        res[x][y][1] = (p_org[1] + 1) / (p_adj[1] + 1)
        res[x][y][2] = (p_org[2] + 1) / (p_adj[2] + 1)

        # print('p_org:', p_org)
        # print('p_adj:', p_adj)
        # print(res[x][y])

np.save(out, res)

org.close()
adj.close()
