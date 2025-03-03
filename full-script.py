#installs necessary moduels

!pip install openai-whisper # to convert audio to text
!pip install moviepy   # to convert video to audio

#imports necessary libraries
import os
import whisper
from moviepy.editor import VideoFileClip
import warnings

try:  # to catch errors we used try block
    warnings.filterwarnings("ignore")  # tohandle errors and ignres
    directory_path=input("Enter directory address::\n") #We ask manually to tenter directory path to search audio video files
    # print(directory_path,os.getcwd())

# function to convert video audio files to text
    def video_audio_files(directory_path):     # giving input what we have asked , the source directory
        audio_formats={".mp3",".wav",".m4a",".wma"}   # to declare required audio extensions 
        video_formats={".mpeg", "mpeg4",".mp4",".mov",".avi"} # to declare required video extensions
        audio_files=[]    #collects all audio files in the directory to this list
        video_files=[]    # collects all video files in the directory to this list

    
        if os.path.exists(directory_path): # checks if file exists

            for root,items,files in os.walk(directory_path): 
                # os.walk returns as  generator with 3 tuples root,folder,files
                # for loop to be used here to iterate all folder , subfolders and files in the directory path 
                for item in files: #iterates all files to check audio, video formats given
                    
                    if item.lower().endswith(tuple(audio_formats)):  #if a file ends with given audio format
                        audio_files.append(os.path.join(root,item))  # appends to the list names audio_files
                    
                    elif item.lower().endswith(tuple(video_formats)): #else check if a file ends with given video formats
                        video_files.append(os.path.join(root,item))  # appends to given video_files list 

        return audio_files, video_files   # returns the 2 lists of audio_files and video_files
# To extract  audio from video. here we are using moviepy the easier one
    def extract_audio_from_video(video_files):   # give video_files  as a list data type 
        
        count=0         # to count total files extracted of video formats
        for item in video_files:    #iterates each video file
            clip=VideoFileClip(item)   # loads the video into clip variable
            mp3_file_path=os.path.join(directory_path,f"{os.path.basename(item)}.mp3")
            # here we are joining source path of this file with its original name to convert to audio format mp3 
            clip.audio.write_audiofile(mp3_file_path)  #  seperates the given video file to mp3 audio format file

            print("Audio extracted successfully from Video Fles::",f"{os.path.basename(item)}.mp3") # prints the successful confoirmaiton message
            clip.close()  # closes the clip variable 
            audio_files.append(mp3_file_path) # this extrcated mp3 audio file from the video has been appending to audio_files list data type for further convert to text
            count+=1     # increments count value
        print("Total Audio Files extracted::",count)  # prints total numbers of audio files extracted and stored to audio_files lis data type from the source video files
        print("\n")

    

    def convert_audio_to_text(audio_files,directory_path):  # fundtion to convert audio to text
        
        model = whisper.load_model("tiny")  # Here we are using tiny model, which takes less file size, we can use base, turbo and other models
        
        for item in audio_files:   #to iterate each audio file  in the list
            output_folder=os.path.join(directory_path,"output")  # creates outputfolder with a folder name "output" in the given directory path
            os.makedirs(output_folder,exist_ok=True)   # if directory exists leaves else create a folder
            
            with open(os.path.join(output_folder,f"{os.path.basename(item)}.txt"),"w") as file:   
                # we are creating a file with its original basename by giving an extension because we are converting to text format
                result = model.transcribe(item)  # here model transcribes the audio file to text and and stores the in result varibale
                file.write(result["text"])  # write the extracted text to file 
                print("Audio converted to text successfully::",f"{os.path.basename(item)}.txt")  # prints succeessful message after writing into file and the file name
                file.close() # closes the file

# calling each function

    audio_files,video_files=video_audio_files(directory_path)
    extract_audio_from_video(video_files)
    convert_audio_to_text(audio_files,directory_path)

# prints each file 
    [print("Audio Files:::",(i)) for i in enumerate(audio_files)]
    print("\n")
    [print("Video Files:::",(i)) for i in enumerate(video_files)]

# To catch errors and we used here try except else  else system generating lot of warnings.
except Exception as e:
    warnings.filterwarnings("ignore")   

else:
    pass
finally:
    pass