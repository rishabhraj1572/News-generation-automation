from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client file.json'
API_NAME = 'youtube'
API_VERSION = 'v3'

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

from datetime import datetime
import pytz

# datetime object containing current date and time
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)




from gnewsclient import gnewsclient

client = gnewsclient.NewsClient(language='hindi',
								location='india',
								topic='nation')

news_list = client.get_news()

News1 = news_list [0]['title']
print(News1)
News2 = news_list [1]['title']
print(News2)
News3 = news_list [2]['title']
print(News3)
News4 = news_list [3]['title']
print(News4)
News5 = news_list [4]['title']
print(News5)
News6 = news_list [5]['title']
print(News6)
News7 = news_list [6]['title']
print(News7)
News8 = news_list [7]['title']
print(News8)
News9 = news_list [8]['title']
print(News9)
News10 = news_list [9]['title']
print(News10)



from gtts import gTTS 

import os

#Defining a simple text 

text = "ख़बर 1!"+News1+"..."+"ख़बर 2!"+News2+"..."+"ख़बर 3!"+News3+"..."+"ख़बर 4!"+News4+"..."+"ख़बर 5!"+News5+"..."+"ख़बर 6!"+News6+"..."+"ख़बर 7!"+News7+"..."+"ख़बर 8!"+News8+"..."+"ख़बर 9!"+News9+"..."+"ख़बर 10!"+News10+"...."+"automatically generated..."
text1 = "News 1:"+News1+", News 2:"+News2+", News 3:"+News3+", News 4:"+News4+", News 5:"+News5+", News 6:"+News6+", News 7:"+News7+", News 8:"+News8+", News 9:"+News9+", News 10:"+News10+"..............................."+"Automatically Generated"
language = 'hi' 

speech = gTTS(text=text, lang=language, slow=False)


speech.save("news_hindi.mp3")

from moviepy.editor import *

audio2 = AudioFileClip("news_hindi.mp3")
# Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
clip2 = ImageClip("hin.png").set_duration(audio2.duration)
# Set the audio of the clip
clip2 = clip2.set_audio(audio2)
# Export the clip
clip2.write_videofile("newshin.mp4", fps=24)





# dd/mm/YY H:M:S
dt_string = datetime_ist.strftime("%d/%m/%Y,%I:%M %p")

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
title = 'Hindi News (भारत)- '
desc = "ख़बर 1:"+News1+"\nख़बर 2:"+News2+"\nख़बर 3:"+News3+"\nख़बर 4:"+News4+"\nख़बर 5:"+News5+"\nख़बर 6:"+News6+"\nख़बर 7:"+News7+"\nख़बर 8:"+News8+"\nख़बर 9:"+News9+"\nख़बर 10:"+News10+"\n\nAutomatically Generated..."
spon= '\n\nFor Advertisement Contact : newsproviderindia@gmail.com'

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': title+dt_string+' GMT+5:30',
        'description': desc+spon,
        'tags': ['News', 'Headlines', 'India']
    },
    'status': {
        'privacyStatus': 'public',
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': True
}

mediaFile = MediaFileUpload('newshin.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

