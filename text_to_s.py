#!usr/bin/python3

# importing google text to speech
from gtts import gTTS
# importing for output
import os
text=input("Enter the string to be conveted: ")
# creating object 
# language = english, hi for hindi
tts=gTTS(text ,lang='en')
# saving the file
tts.save("good.mp3")

# playing the output
os.system("mpg321 good.mp3")