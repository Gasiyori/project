import serial
import time

# if __name__ == '__main__': 
#     ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) 
#     ser.flush() 
#     while True: 

arduino = serial.Serial('/dev/ttyACM0', 9600)

while 1 : 
    c = input()
    if c == 'q':
        break
    else:
        c = c.encode('utf-8')
        arduino.write(c)

    if arduino.in_waiting > 0: 
        line = arduino.readline().decode('utf-8').rstrip()
        print(line)