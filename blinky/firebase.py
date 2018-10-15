import pyrebase
import firebase_admin
from firebase_admin import credentials
from datetime import datetime


cred = credentials.Certificate("eye-blink.json")
firebase_admin.initialize_app(cred)

def motiondetect(a):


    config = {
    "apiKey": "AIzaSyDFcpcoGQbYkt7D-WPUpd2gHl3ZxzfMPxQ",
    "authDomain": "eye-blink.firebaseapp.com",
    "databaseURL": "https://eye-blink.firebaseio.com",
    "storageBucket": "eye-blink.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()

    data = {"Blinked Eye at : ": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"name": a}
    db.child("eye-blink").push(data)
