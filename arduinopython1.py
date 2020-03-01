import serial
import time
ser = serial.Serial('com5', 9600)
while(1):
    a=raw_input("Enter a")
    if a =="F":
        print ("Forward")
        time.sleep(1)
        ser.write('1')
    elif a =="S":
        print ("Stop")
        time.sleep(1)
        ser.write('5')
    else:
        print ("Stop")
        time.sleep(1)
        ser.write('5')
