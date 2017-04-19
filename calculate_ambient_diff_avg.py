#!/usr/bin/env python3
import csv

mean_sum = 0.0
median_sum = 0.0
count = 0.0

with open('ambient_diff.csv', newline='') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data_reader:
        mean_sum += float(row[3])
        median_sum += float(row[5])
        count += 1.0

print('mean_angle avg. = ', mean_sum/count)
print('median_angle avg. = ', median_sum/count)
