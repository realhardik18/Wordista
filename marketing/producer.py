from html2image import Html2Image
from moviepy.editor import ImageClip,AudioFileClip
import os
import pandas as pd
import random

def create_image(word):
    hti = Html2Image()
    hti.screenshot(
        html_file=f'{word}.html', css_file='word.css',
        save_as=f'{word}.png',size=(1080, 1920)
    )    

def create_html(word,meaning,pos,example):
    #@ -> for word
    #% -> for meaning
    #^ -> for part of speech
    #* -> for example
    with open('template.html','r') as file:
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

def create_video(word):    
    audio_folder = 'audio_assets'
    audio_track = random.choice(os.listdir(audio_folder))
    audio_path = os.path.join(audio_folder, audio_track)    
    audio_clip = AudioFileClip(audio_path)    
    audio_duration = audio_clip.duration    

    image_clip = ImageClip(f'{word}.png', duration=audio_duration)    
    video_clip = image_clip.set_audio(audio_clip)
    
    output_path = f"output_vids/{word}.mp4"
    
    video_clip.write_videofile(output_path, fps=24)

    os.remove(f'{word}.html')
    os.remove(f'{word}.png')
    
    print(f"video created for {word}")

def get_word(index):
    df=pd.read_csv('db.csv')
    data=dict()
    data['word']=df['word'][index]
    data['meaning']=df['definition'][index]
    data['pos']=df['part of speech'][index]
    data['ex']=df['example'][index]
    return data

def clean_data():
    df=pd.read_csv('db.csv')    
    df=df.dropna()
    df.to_csv('db.csv')
