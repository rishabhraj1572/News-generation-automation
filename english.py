from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from datetime import datetime
import requests
import json
from gtts import gTTS 
import os
from moviepy.editor import *
import time
import schedule
import pytz

api_key = 'YOUR_API_KEY'

def eng():
    
    CLIENT_SECRET_FILE = 'client file.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'

    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']



# datetime object containing current date and time
    UTC = pytz.utc

    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)



# In[5]:

    try:
        
        
        r = requests.get('http://newsapi.org/v2/top-headlines?sources=google-news-in,language=hi&apiKey='+api_key)
        r


# In[11]:


        data = json.loads(r.content)

# In[31]:


        News1 = data ['articles'][0]['title']
        print(News1)
        News2 = data ['articles'][1]['title']
        print(News2)
        News3 = data ['articles'][2]['title']
        print(News3)
        News4 = data ['articles'][3]['title']
        print(News4)
        News5 = data ['articles'][4]['title']
        print(News5)
        News6 = data ['articles'][5]['title']
        print(News6)
        News7 = data ['articles'][6]['title']
        print(News7)
        News8 = data ['articles'][7]['title']
        print(News8)
        News9 = data ['articles'][8]['title']
        print(News9)
        News10 = data ['articles'][9]['title']
        print(News10)



#Defining a simple text 

        text = "News 1!"+News1+"..."+"News 2!"+News2+"..."+"News 3!"+News3+"..."+"News 4!"+News4+"..."+"News 5!"+News5+"..."+"News 6!"+News6+"..."+"News 7!"+News7+"..."+"News 8!"+News8+"..."+"News 9!"+News9+"..."+"News 10!"+News10+"...."+"automatically generated..."
#text1 = "ख़बर 1:"+News1+", ख़बर 2:"+News2+", ख़बर 3:"+News3+", ख़बर 4:"+News4+", ख़बर 5:"+News5+", ख़बर 6:"+News6+", ख़बर 7:"+News7+", ख़बर 8:"+News8+", ख़बर 9:"+News9+", ख़बर 10:"+News10+"..............................."+"Automatically Generated"

        language = 'hi' 

        speech = gTTS(text=text, lang=language, slow=False)

        speech.save("news_en.mp3")


    except :
        print("Only 8 news available...")
        print("")
        print("")
        r = requests.get('http://newsapi.org/v2/top-headlines?sources=google-news-in,language=hi&apiKey='+api_key)
        r


# In[11]:


        data = json.loads(r.content)

# In[31]:



        News1 = data ['articles'][0]['title']
        print(News1)
        News2 = data ['articles'][1]['title']
        print(News2)
        News3 = data ['articles'][2]['title']
        print(News3)
        News4 = data ['articles'][3]['title']
        print(News4)
        News5 = data ['articles'][4]['title']
        print(News5)
        News6 = data ['articles'][5]['title']
        print(News6)
        News7 = data ['articles'][6]['title']
        print(News7)
        News8 = data ['articles'][7]['title']
        print(News8)



#Defining a simple text 

        text = "News 1!"+News1+"..."+"News 2!"+News2+"..."+"News 3!"+News3+"..."+"News 4!"+News4+"..."+"News 5!"+News5+"..."+"News 6!"+News6+"..."+"News 7!"+News7+"..."+"News 8!"+News8+"...."+"automatically generated..."
#text1 = "ख़बर 1:"+News1+", ख़बर 2:"+News2+", ख़बर 3:"+News3+", ख़बर 4:"+News4+", ख़बर 5:"+News5+", ख़बर 6:"+News6+", ख़बर 7:"+News7+", ख़बर 8:"+News8+", ख़बर 9:"+News9+", ख़बर 10:"+News10+"..............................."+"Automatically Generated"

        language = 'hi' 

        speech = gTTS(text=text, lang=language, slow=False)

        speech.save("news_en.mp3")


        



# Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audio1 = AudioFileClip("news_en.mp3")
# Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
    clip1 = ImageClip("eng.png").set_duration(audio1.duration)
# Set the audio of the clip
    clip1 = clip1.set_audio(audio1)
# Export the clip
    clip1.write_videofile("newseng.mp4", fps=24)
            





    try:        # dd/mm/YY H:M:S
        dt_string = datetime_ist.strftime("%d/%m/%Y,%I:%M %p")

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        title = 'News Headlines (India)- '
        desc = 'News 1:'+News1+'\nNews 2:'+News2+'\nNews 3:'+News3+'\nNews 4:'+News4+'\nNews 5:'+News5+'\nNews 6:'+News6+'\nNews 7:'+News7+'\nNews 8:'+News8+'\nNews 9:'+News9+'\nNews 10:'+News10+'\n\nAutomatically Generated...'
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

        mediaFile = MediaFileUpload('newseng.mp4')

        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()

    except:
        print("Only 8 news available...")
        print("")
        print("")
        dt_string = datetime_ist.strftime("%d/%m/%Y,%I:%M %p")

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        title = 'News Headlines (India)- '
        desc = 'News 1:'+News1+'\nNews 2:'+News2+'\nNews 3:'+News3+'\nNews 4:'+News4+'\nNews 5:'+News5+'\nNews 6:'+News6+'\nNews 7:'+News7+'\nNews 8:'+News8+'\n\nAutomatically Generated...'
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

        mediaFile = MediaFileUpload('newseng.mp4')

        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()

    


eng()




