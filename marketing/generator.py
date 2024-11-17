import producer

with open('used-words.txt','r') as file:
    indexes=file.readlines()[:168]

counter=0

for index in indexes:
    index=int(index.strip())
    data=producer.get_word(index)            
    producer.create_html(word=data['word'],example=data['ex'],meaning=data['meaning'],pos=data['pos'])    
    producer.create_image(word=data['word'])    
    producer.create_video(word=data['word'])
    print(f'{counter} vids produced!')
    counter+=1
