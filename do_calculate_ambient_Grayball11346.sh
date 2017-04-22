#!/bin/bash
# invokes calculate_ambient.py to calculate ambient data

for d in $(ls Grayball11346) ; do
    mkdir Grayball11346_data/$d
    for f in $(find Grayball11346/$d/*.jpg -type f -printf "%f\n") ; do
        python calculate_ambient.py \
            Grayball11346/$d/$f \
            Grayball11346_proceed/$d/$f \
            Grayball11346_data/$d/${f%.*}.npy
    done
done
