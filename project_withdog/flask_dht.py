
import time
from flask import Flask,render_template
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./withdog-ccee3-firebase-adminsdk-txj36-94e9ee1fe3.json")
firebase_admin.initialize_app(cred) 
db = firestore.client()

app = Flask(__name__)


def temp():
    doc_ref = db.collection(u'With').document(u'Pi')
    doc = doc_ref.get()
    print(u'Document data: {}'.format(doc.to_dict()))
    data = doc.to_dict()
    return data
    # except google.cloud.exceptions.NotFound:
    #     print(u'No such document!')

def Intime():
    doc_ref = db.collection(u'Dog').document(u'Pi')

    doc = doc_ref.get()
    print(u'Document data: {}'.format(doc.to_dict()))
    clock = doc.to_dict()
    return clock

@app.route('/')                   
def index():
    DHT22 = temp()
    clock = Intime()
    dogs = {'temp' : DHT22['temp'], 'humi' : DHT22['humi'], 'clock' : clock['clock']}
    return render_template('index.html',**dogs)

@app.route('/time')             
def about():
    clock = Intime()
    return render_template('time.html',**clock)

@app.route('/contact')       
def contact():
    return 'This is contact page'

if __name__ == '__main__':
    app.run(port=8080)
    