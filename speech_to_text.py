import speech_recognition as sr

#Sample rate is how often values are recorded
sample_ratee= 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.
#chuck_sizee= 2048
#Initializing the recognizer 
r = sr.Recognizer()

#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names()

#device id can be generated by using lsusb
#device_id=001

with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        print ("Say Something")
        audio = r.listen(source)
        try: 
            text = r.recognize_google(audio) 
            print ("you said: " + text)
        except sr.UnknownValueError: 
            print ("Google Speech Recognition could not understand audio") 
        except sr.RequestError as e: 
            print ("Could not request results from Google Speech Recognition service;{0}".format(e)) 