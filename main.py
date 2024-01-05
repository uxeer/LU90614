import serial
from time import sleep
'''
Change the com port according to your device port
'''

ser = serial.Serial('COM4', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 1)
human = b'\xFA\xC5\xBF'
object = b'\xFA\xC6\xC0'
temp = b'\xFA\xCA\xC4'
flag = 0

def check_temperature():
    global flag
    if flag == 0:
        print("Press a key to check temperature (1 for human, 2 for object, 3 to stop):")
        while True:
            key = input("Enter key: ")
            if key.lower() == '1':
                flag = 1
                break
            elif key.lower() == '2':
                flag = 2
                break
            elif key.lower() == '3':
                flag = 0
                break

while True:
    check_temperature()
    if flag == 1 or flag == 2:
        if flag == 1:
            ser.write(serial.to_bytes(human))
            print(human)
        elif flag == 2:
            ser.write(serial.to_bytes(object))
            print(object)
        ser.write(serial.to_bytes(temp))
        print(temp)

        sensor = ser.read(9)
        if len(sensor) == 9:
            if flag == 1:
                if sensor[2] == 255 and sensor[3] == 255:
                    print("Human temperature out of range")
                else:
                    print("Human Temp : " + str(sensor[2]) + "." + str(sensor[3]) + "°C")
            elif flag == 2:
                if sensor[2] == 255 and sensor[3] == 255:
                    print("Object temperature out of range")
                else:
                    print("Object Temp : " + str(sensor[2]) + "." + str(sensor[3]) + "°C")

    elif flag == 0:
        print("Ready")


