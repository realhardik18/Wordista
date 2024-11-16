from html2image import Html2Image
from moviepy.editor import ImageClip,AudioFileClip
import os
import pandas as pd
import random

def create_image():
    hti = Html2Image()
    hti.screenshot(
        html_file='modicum.html', css_file='word.css',
        save_as='blue_page.png',size=(1080, 1920)
    )

def create_html(word,meaning,pos,example):
    #@ -> for word
    #% -> for meaning
    #^ -> for part of speech
    #* -> for example
    with open('word.html','r') as file:
        data=file.read()    

    data=data.replace('@',word)
    data=data.replace('%',meaning)
    data=data.replace('^',pos)
    data=data.replace('*',example)

    with open(f'{word}.html','w') as file:
        file.write(data)

def make_order():
    indexes=list(range(1,1066))        
    for _ in range(len(indexes)):
        index=random.choice(indexes)
        indexes.remove(index)
        with open('used-words.txt','a') as file:
            file.write(f'{index}\n')

def create_video(image):    
    audio_folder = 'audio_assets'
    audio_track = random.choice(os.listdir(audio_folder))
    audio_path = os.path.join(audio_folder, audio_track)    
    audio_clip = AudioFileClip(audio_path)    
    audio_duration = audio_clip.duration    

    image_clip = ImageClip(image, duration=audio_duration)    
    video_clip = image_clip.set_audio(audio_clip)
    
    output_path = "output_video.mp4"
    
    video_clip.write_videofile(output_path, fps=24)

    print(f"Video created successfully! Saved to {output_path}")
    return output_path


print(create_video('blue_page.png'))

