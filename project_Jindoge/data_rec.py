import time
import requests
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

url = 'http://203.253.128.177:7579/Mobius/walwal/training/la'
headers = {'Accept':'application/json',
            'X-M2M-RI':'12345',
            'X-M2M-Origin':'SOrigin'}

while(True):

###### receive data from Mobius server #######
    r = requests.get(url, headers=headers)

    try:
        r.raise_for_status()
        jr = r.json()
        
        print(jr)
        print(jr['m2m:cin']['con'])
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    tr = jr['m2m:cin']['con']

    #아두이노로 데이터 전송
    arduino.write(tr) 

    #음성 출력
    

    #아두이노에서 데이터 수신
    if arduino.in_waiting > 0: 
        line = arduino.readline().decode('utf-8').rstrip()

    #훈련 성공 여부 판단

    #성공시

    #실패시