# Video Compressor

Video compression made easy. This repo can only compress `mp4` video format. Other formats are not tested and implemented.

## To clone this repo

```
git clone https://gitlab.com/hello-arun/video-compressor.git
```

## Getting started guide

To edit videos put all of them inside [in](./in) folder and run [compress](./compress.sh) script. Compressed videos will be stored inside [out](./out) folder.

```
./compress.sh
```

To run it on IBEX you may submit the job via [compress.sbatch](./compress.sbatch)

```
sbatch compress.sbatch
```

## Quality control

Although this works well almost always but if you want to have manual control over the quality you may edit the [compress.sh](./compress.sh) script. This controls the compression rate and information loss.

[```ffmpeg -i $inDIR/$filename -vcodec libx265 -crf 28 -strict -2 $outDIR/$filename```](https://gitlab.com/hello-arun/video-compressor/-/blob/main/compress.sh#L17)

you can change crf value. lower crf means lower compression and higher quality but large file size.

## Required packages

1. ffmpeg



