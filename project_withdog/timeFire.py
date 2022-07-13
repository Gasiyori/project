import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading

state = 0
d1 = 0
d2 = 0
showtime = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def weightsetup():
    EMULATE_HX711=False
    referenceUnit = 1
    if not EMULATE_HX711:
        from hx711 import HX711
    else:   
        from emulated_hx711 import HX711

    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(-160)
    #hx.set_reference_unit(referenceUnit)
    hx.reset()
    hx.tare()
    return hx

def weight():
    global state, d2, d1, showtime
    
    hx = weightsetup()
    val = hx.get_weight(5)
    print("val:{0}".format(val))

    if val > 0 and state == 0:
        state = 1
        d1 = time.time()
        print(state)

    if state >= 1 :
        if val <= 0:
            state += 1
            print(state)
        if state > 3 :
            d2 = time.time()
            print("using time")
            print(d2 - d1 - 9)
            state = 0
        
    showtime = int(d2-d1-9)
    
    if showtime > 0 :
        db = firestore.client()
        doc_ref = db.collection(u'Dog').document(u'Pi')
        doc_ref.set({
            u'clock' : showtime
        })
        print("send")
        # threading.Timer(2, sendto).start()

    hx.power_down()
    hx.power_up()
    time.sleep(2)

# def sendto(showtime):
#     db = firestore.client()
#     doc_ref = db.collection(u'With').document(u'RaspberryPi')
#     doc_ref.set({
#         u'clock' : showtime
#     })
#     print("send")
#     threading.Timer(2, sendto).start()

cred = credentials.Certificate("./withdog-ccee3-firebase-adminsdk-txj36-94e9ee1fe3.json")
firebase_admin.initialize_app(cred)

while True:
    weight()
    


