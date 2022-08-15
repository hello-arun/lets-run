#!/bin/bash
srcDIR=$PWD
inDIR="$srcDIR/in"
outDIR="$srcDIR/out"

cd $inDIR
list=$(ls *.mp4)
cd $srcDIR

rm -f $srcDIR/log.log
mkdir -p $outDIR
for filename in $list; do
    if [ -f $outDIR/$filename ]; then
        echo "Already Compressed : $filename" >> $srcDIR/log.log
    else
        echo "Compressing Video  : $filename" >> $srcDIR/log.log
        ffmpeg -i $inDIR/$filename -vcodec libx265 -crf 28 -strict -2 $outDIR/$filename
        echo "Compressed : $filename" >> $srcDIR/log.log
    fi
done
