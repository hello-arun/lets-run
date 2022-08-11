import cv2 as cv

def hhmmss(duration_sec):
    minutes = int(duration_sec/60)
    hours = int(minutes/60)
    minutes = minutes%60
    seconds = duration_sec%60
    return f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"

def get_dur(fileName):
    cap = cv.VideoCapture(fileName)
    fps = cap.get(cv.CAP_PROP_FPS)      # OpenCV v2.x used "CV_CAP_PROP_FPS"
    frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    duration_sec = frame_count/fps
    cap.release()
    return duration_sec
def get_resolution(fileName):
    vcap = cv.VideoCapture(fileName) # 0=camera
    width  = vcap.get(cv.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = vcap.get(cv.CAP_PROP_FRAME_HEIGHT)  # float `height`
    vcap.release()
    return width,height


def video_id(file_name):
    if file_name.endswith(".mp4"):
        len=file_name.index("-")
        return int(file_name[0:len])
    return 0

def get_chapter_name(file_name):
    if file_name.endswith(".mp4"):
        len=file_name.index("-")
        return file_name[len+2:-4]

import os
files = os.listdir()
files.sort(key = video_id)
meta_data = ""
filelist = ""
start_time_sec = 0
filestr=""
filterstr=""
i=0
for video_name in files:
    if video_name.endswith(".mp4"):
        print(f"Processing {video_name}, \nRes: {get_resolution(video_name)}")
        filestr+=f"-i \'{video_name}\' `\n"
        filterstr+=f"[{i}:v] [{i}:a] `\n"
        i+=1
        chapter_name = get_chapter_name(video_name)
        meta_data += f"{hhmmss(start_time_sec)} - {chapter_name}\n"
        start_time_sec += get_dur(video_name)

        # file = file.replce(" ","")
        filelist+=f"file \'{video_name}\'\n"

os.makedirs("./merged",exist_ok=True)

with open("./merged/meta-data.txt","w") as metafile:
    metafile.write(meta_data)
with open("./file-list.txt","w") as metafile:
    metafile.write(filelist)
message=f"ffmpeg {filestr} -filter_complex \"{filterstr} concat=n={i}:v=1:a=1 [vv] [aa]\" -map \"[vv]\" -map \"[aa]\" -r 30 ./merged/output.mp4"
# -r 30 means 30 FPS
with open("./merge-command.txt","w") as command_file:
    command_file.write(message)


# print(meta_data)
# print(filelist)
print("\nTotal Length",hhmmss(start_time_sec))

print("\nTo Upscale a video use ")
print("ffmpeg -i input.mp4 -vf scale=1280x720:flags=lanczos output_1080p.mp4")
print("\nTo merge see merge-command.txt file")
print("type merge-command.txt\n\nor\n\n")
print("ffmpeg.exe -safe 0 -f concat -i file-list.txt -c copy ./merged/output.mp4")