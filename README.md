# Web_Speech_To_Text
•	I have created web application Speech Recognition with Python and Flask using Cloud AI API. In Which I have Used Cloud Bucket as a storage service for accessing the audio file and after that these audio file will be converted into text using google Cloud Speech API.
# Step 1:
Store the data on Google Storage
# Step 2: 
AI Platform (Cloud AI): 
•	First, I have created a Project Named speechtotextrecognition
•	Downloaded the JSON file as it will authenticate you to the cloud API
•For using cloud speech API in my app, I install google cloud speech package using pip install google-cloud-speech in cloud terminal. And then import all required packages.
•	I have Created Flask Framework for Web app and inside this framework I have used Cloud AI Functionality.
1)	First, I have created A Simple Flask Application and create the First Route Pointing to Home Page and specify both the method GET and POST.
Like: @app.route("/index", methods= ["GET", "POST"])
•	Created index.html contain the Simple User Interface like:
First, I choose the Audio File using choose file button.
And then Convert that Audio file into Text using Speech to Text Button.
# Step 3: 
Deployment of app using App engine-
1)	In App engine First selected the already created app speechtotextrecognition.
2)	Open the cloud shell where I have already created the main.py and index.html file now I have also created two more files app.yaml and requirement.txt
3)		App.yaml, this file specifies how URL paths correspond to request handlers and static files. The app. yaml file also contains information about your app's code, such as the runtime and the latest version identifier.
4)	Dependencies of web app are specified in requirements.txt file.
5)	After this I opened the cloud shell and run some commands for deploying the app.
6)  Then Deploying has been finished after some time and URL generated
# Complete Working of project Shown in the YouTube Link: https://www.youtube.com/watch?v=vSqTSqO6ga4
