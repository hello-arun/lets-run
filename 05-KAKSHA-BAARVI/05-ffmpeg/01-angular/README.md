## process.py

This is an add on program to merge and filter `Angular Tutorial` provided by `code-with-mosh`. Output of the program is shown in `process.log`. It creates mainly three files 

* `file-list.txt`  
    List of all the files that it processed

* `merge-command.txt`  
    Generate an FFMPEG command for merging different file. Note that all files need to be of `same resolution`. We can check the resolution of each video in output-log of `process.py` run. After carefully checking just paste the content of merge-command.txt in `powershell` to merge the videos. For `bash terminal` you only need to change the multi line saperator "`" with "\\" 

*  `./merged/meta-data.txt`  
    It is a timestamp file 

### How to run

```powershell
# if opencv does not exist..install it via
# pip install opencv-python 

# for example
cd '.\17. Unit Testing\'
python ../process.py
```