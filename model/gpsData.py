import serial
import time

port = "/dev/serial0"
baudrate = 9600
timeout = 1
ser = serial.Serial(port, baudrate, timeout=timeout)

def getGpsData():
    status1 = 0
    status2 = 0
    status3 = 0
    gpsDataList = []
    # voor altitude
    while status1 == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPGGA":
            gpsDataList.append(data[9])  #altitude --> 0
            gpsDataList.append(data[6]) #gpsFix --> 1
            gpsDataList.append(data[7]) #usedSat --> 2
            status1 = 1
    # voor Time, date, latitude, longitude, speed
    while status2 == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPRMC":
            gpsDataList.append(data[1]) #time --> 3
            gpsDataList.append(data[9]) #date --> 4
            gpsDataList.append(data[3]) #latitude --> 5
            gpsDataList.append(data[5]) #longitude --> 6
            gpsDataList.append(data[7]) #speed --> 7
            status2 = 1
    return gpsDataList

def convertData():
    gpsDataList = getGpsData()

    print(gpsDataList)

convertData()
