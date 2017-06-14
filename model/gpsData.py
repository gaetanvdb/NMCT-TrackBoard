import serial
import time
from _datetime import datetime, timedelta

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
            status1 = 1
    # voor Time, date, latitude, longitude, speed
    while status2 == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPRMC":
            gpsDataList.append(data[1]) #time --> 1
            gpsDataList.append(data[9]) #date --> 2
            gpsDataList.append(data[3]) #latitude --> 3
            gpsDataList.append(data[5]) #longitude --> 4
            gpsDataList.append(data[7]) #speed --> 5
            status2 = 1
    return gpsDataList

def getTime():
    vartime = 0
    vardate = 0
    status = 0
    while status == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPRMC":
            vartime = data[1]
            vardate = data[9]
            status = 1
    utcDateTime = datetime(year= 2000 + int(vardate[4:6]),month=int(vardate[2:4]), day=int(vardate[0:2]), hour=int(vartime[0:2]), minute=int(vartime[2:4]), second=int(vartime[4:6]))
    gmtDateTime = utcDateTime + timedelta(hours=2)
    return gmtDateTime

def convertData():
    gpsDataList = getGpsData()
convertData()
