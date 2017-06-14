import serial
import time

port = "/dev/serial0"
baudrate = 9600
timeout = 1
ser = serial.Serial(port, baudrate, timeout=timeout)

def getGpsData():
    status2 = 0
    gpsDataList = []
    while status2 == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPGGA":
            print("------------------")
            gpsDataList.append(data[9])  #altitude --> 0
            gpsDataList.append(data[6]) #gpsFix --> 1
            gpsDataList.append(data[7]) #usedSat --> 2
            status1 = 1
        if data[0] == "b'$GPRMC":
            gpsDataList.append(data[1]) #time --> 3
            gpsDataList.append(data[9]) #date --> 4
            gpsDataList.append(data[3]) #latitude --> 5
            gpsDataList.append(data[5]) #longitude --> 6
            speed = data[7] #speed --> 7
            status2 = 1
    return gpsDataList

print(getGpsData())