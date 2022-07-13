import RPi.GPIO as GPIO
import Adafruit_DHT as dht
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DHT = 4
LED_t = 24
LED_h = 16
GPIO.setup(LED_t, GPIO.OUT)
GPIO.setup(LED_h, GPIO.OUT)
GPIO.output(LED_t, GPIO.LOW)
GPIO.output(LED_h, GPIO.LOW)


def check():
    h, t = dht.read_retry(dht.DHT22, DHT)
    h = int(h)
    t = int(t)
    print('Temp = {0}*C, Humidity={1}%'.format(t,h))
    sleep(2)
    if round(t)>20: 
        GPIO.output(LED_t, GPIO.HIGH)
    else:
        GPIO.output(LED_t, GPIO.LOW)
    
    if round(h)>30: 
        GPIO.output(LED_h, GPIO.HIGH)
    else:
        GPIO.output(LED_h, GPIO.LOW)

    DATA = { 'temp' : t, 'humi' : h}

    return DATA

def sendto():
    temperature = check()
    doc_ref = db.collection(u'With').document(u'Pi')
    doc_ref.set({
        u'temp' : temperature['temp'],
        u'humi' : temperature['humi'],
    })
    threading.Timer(2, sendto).start()

cred = credentials.Certificate("./withdog-ccee3-firebase-adminsdk-txj36-94e9ee1fe3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
sendto()

