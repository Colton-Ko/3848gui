import serial
import sys
from os import path

def main():
    #Detect arduino serial path (Cater for different USB-Serial Chips)
    if path.exists("/dev/ttyACM0"):
        arduino = serial.Serial(port = '/dev/ttyACM0',baudrate = 115200)
    elif path.exists("/dev/ttyUSB0"):
        arduino = serial.Serial(port = '/dev/ttyUSB0',baudrate = 115200)
    else:
        print("Please plug in the Arduino")
        exit()
    if not(arduino.isOpen()):
        arduino.open()
    try:
        while (True):
            if arduino.inWaiting():
                print("From Arduino serial: %s" %arduino.readline().decode('utf-8'))
            arduino.flushInput()
            arduino.flushOutput()
            try:
                letter=input("Send single letter command to arduino: ")[0]
                if (letter != 'X'):
                    print(f"Sending {letter} to arduino")
                    arduino.write(letter.encode())
            except Exception:
                pass
            
    except KeyboardInterrupt:
        pass

main()