'''  I was studying one technology by watching downloaded videos. 
I want to know the time required to watch all videos. Hence, python helped me to do this. '''

from moviepy.editor import VideoFileClip
import os


def work():
    time = 0;
    for (dirPath, dirName, fileNames) in (
            os.walk("/root/Desktop")):
      
        print()
        for file in fileNames:
            full_path = os.path.join(dirPath, file)
            filename, file_extension = os.path.splitext(file)
            if (file_extension == ".mp4"):
                clip = VideoFileClip(full_path)
                print("Directory : " + dirPath)
                print(file)
                print(clip.duration / 60, " min")
                time += clip.duration / 60
    print("Total time (Min) : ", time, " Min.")
    print("Total time (Hrs) : ", time / 60, " hrs.")


work()
