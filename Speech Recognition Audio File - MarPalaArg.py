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
##Using record() to Capture Data From a File
################################################################
audio_file = sr.AudioFile('file.wav')
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

################################################################
##Invoke recognize_google() to attempt recognize any speech
################################################################
audio_to_text = r.recognize_google(audio)

