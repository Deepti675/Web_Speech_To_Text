# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:42:28 2022

@author: Deepti
"""
import os
from google.cloud import speech
import speech_recognition as sr

# calling to GOOGLE application credential and atttached
sr.__version__
#from the web application framwork flask importing request, flask, render template
from flask import Flask, render_template,request,redirect
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
app= Flask("__name__")
@app.route("/index", methods=["GET", "POST"])
def index():
    transcript = ""
    #POST request access if it is true means the form has been submitted with some data
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        
        #redirect handler function will redirect your Audio file for transcription.
        if "file" not in request.files: return redirect(request.url)
            
         #request module is  use to access incoming data in flask
        Audio_file = request.files["file"]
        if Audio_file.filename == "":  return redirect(request.url)

        if Audio_file:
            #Direct use of API for speech to text conversion 
            #Recognizer Model work at character level so that as you speak, it outputs words character-by-character
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(Audio_file)
            with audioFile as source:
                #contant recorded for conversion
                Txt_file = recognizer.record(source)
                #speech to text conversion Stored in transcript
            transcript = recognizer.recognize_google(Txt_file, key=None)
           #return the value to show in html 
    return render_template('index.html', transcript=transcript)


if __name__ == '__main__':
    #calling function
    app.run(host='127.0.0.1', debug=True)