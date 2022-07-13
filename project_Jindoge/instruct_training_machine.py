import sys
import time
import serial
import os

def instruct_send(code):
    while True:
        code = str(code).encode('utf-8')
        temp = arduino.write(code)
            
        if temp > 2000:
            break

if __name__ == '__main__':
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    
    arduino.flush()
    
    instruct_send(1) # send to arduino value of 1 or 2
    print("Sit1 OK")
    
    os.system('omxplayer sit.m4a &')
    import sit
    file_sit = 'sit.py'
    sit_return = sit.return_value
    sit_return = bool(sit_return)

    # sit_return = True ############################################# temp value of return sit test

    # training result and arduino excute
    if sys.argv[1] == '1': #if argv is sit?
        if sit_return == True: #<<sit mode>> return value true?
            instruct_send(5) #arduino 'give snack'
            print("GIVE SNACK OK(SIT)")
            instruct_send(3) #arduino return sit
            print("Sit2 OK(SUCCEED)")
            arduino.flush()
        elif sit_return == False: #<<sit mode>> return value false?
            instruct_send(6)
            print("Dummy for control Error")
            instruct_send(3) #arduino 'sit2'
            print("Sit2 OK(FAILED)")
            arduino.flush()
    elif sys.argv[1] == '2':
        if sit_return == True: #<<sit mode>> return value true??
            instruct_send(2) #arduino 'wait1'            
            print("WAIT1 OK(SUCCEED)")
            os.system('omxplayer wait.m4a &')            
            import wait
            file_wait = 'wait.py'
            wait_return = wait.return_value
            wait_return = bool(wait_return)
            # wait_return = False ######################################################## temp value of return wait test
            if wait_return == True: #<<wait mode>> return value true??
                instruct_send(5) #arduino 'give snack'
                print("GIVE SNACK OK(WAIT)")
                instruct_send(4)
                print("WAIT2 OK(SUCCEED)")
                arduino.flush()
            elif wait_return == False: #<<wait mode>> return value false?
                instruct_send(6)
                print("Dummy for control Error")
                instruct_send(4)
                print("WAIT2 OK(FAILED)")
                arduino.flush()
        elif sit_return == False:
            instruct_send(6)
            print("Dummy for control Error")
            instruct_send(3) #arduino 'sit2'
            print("SIT2 OK(FAILED IN WAIT)")
            arduino.flush()