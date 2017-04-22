#!/usr/bin/env python3

import numpy as np
import scipy.io

def angle_between(v1, v2):
    v1_u = v1 / np.linalg.norm(v1)
    v2_u = v2 / np.linalg.norm(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

real_rgb_list = scipy.io.loadmat('groundtruth_568/real_illum_568..mat')['real_rgb']
image_list_file = open('dataset_568/filelist.txt')

import csv
data_file = open('ambient_diff_dataset_568.csv', 'w', newline='')
data_filednames = [
    'file',
    'ground_truth',
    'ambient_mean',
    'mean_angle',
    'ambient_median',
    'median_angle']
data_writer = csv.DictWriter(data_file,
                             delimiter=',',
                             quotechar='|',
                             quoting=csv.QUOTE_MINIMAL,
                             fieldnames=data_filednames)

for f, real_rgb in zip(image_list_file, real_rgb_list):
    basename = f.replace('\n', '')
    proceed_rgb_mat = np.load('dataset_568_data/' +
        basename + '.npy')

    # flattern 3d mat [x1:[y1:[rgb1:[]]...]...]
    # to 2d mat rgb_list[rgb:[]...]
    proceed_rgb_list = proceed_rgb_mat.reshape((-1, \
                        proceed_rgb_mat.shape[-1]))

    mean = np.mean(proceed_rgb_list, axis = 0)
    median = np.median(proceed_rgb_list, axis = 0)

    mean_angle = angle_between(real_rgb, mean)
    median_angle = angle_between(real_rgb, median)

    data_writer.writerow({
        'file': basename,            # file_name
        'ground_truth': real_rgb,    # ground_truth
        'ambient_mean': mean,        # proceed mean
        'mean_angle': mean_angle,    # angle(ground_truth, mean)
        'ambient_median': median,    # proceed median
        'median_angle': median_angle # angle(groung_truth, median)
    })

data_file.close()
image_list_file.close()
