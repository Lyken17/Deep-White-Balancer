#!/bin/bash
# invokes calculate_ambient.py to calculate ambient data

for f in $(find dataset_568_crop/*.png -type f -printf "%f\n") ; do
    python calculate_ambient.py \
        dataset_568_crop/$f \
        dataset_568_crop_proceed/$f \
        dataset_568_data/${f%.*}.npy \
        1 \
        2.2
done
