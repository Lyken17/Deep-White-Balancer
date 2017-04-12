#!/bin/bash
# invokes calculate_ambient.py to calculate ambient data

for d in $(ls Grayball11346_clip_resize) ; do
    mkdir Grayball11346_clip_resize_data/$d
    for f in $(find Grayball11346_clip_resize/$d/*.jpg -type f -printf "%f\n") ; do
        python calculate_ambient.py \
            Grayball11346_clip_resize/$d/$f \
            Grayball11346_clip_resize_proceed/$d/$f \
            Grayball11346_clip_resize_data/$d/${f%.*}.npy
    done
done
