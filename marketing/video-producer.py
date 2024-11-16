from html2image import Html2Image
import csv

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

#create_html("modicum","a small or moderate or token amount.","noun","If my sister had even a modicum of sense, she wouldn't be engaged to that barbarian.")
create_image()
