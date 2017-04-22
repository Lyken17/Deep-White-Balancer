#!/bin/bash
# invokes process_balls.lua to process balls image

for d in $(ls Grayball11346) ; do
    mkdir Grayball11346_proceed/$d
    th process_balls.lua -input_dir Grayball11346/$d -output_dir Grayball11346_proceed/$d
done
