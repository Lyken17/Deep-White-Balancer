#!/bin/bash
# invokes process_balls.lua to process balls image

for d in $(ls Grayball11346_clip_resize) ; do
    mkdir Grayball11346_clip_resize_proceed/$d
    th process_balls.lua -input_dir Grayball11346_clip_resize/$d -output_dir Grayball11346_clip_resize_proceed/$d
done
