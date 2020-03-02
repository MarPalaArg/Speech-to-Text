# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:34:02 2020

@author: mpala
"""

import speech_recognition as sr
print(sr.__version__)

################################################################
##Creating a Recognizer instance 
################################################################
r = sr.Recognizer()

################################################################
##Use the default system Microphone
################################################################
mic = sr.Microphone()

################################################################
##Use listen() function to capture input from mic
################################################################
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=None)
    
################################################################
##Invoke recognize_google() to attempt recognize any speech
################################################################
audio_to_text = r.recognize_google(audio)

print(audio_to_text)



