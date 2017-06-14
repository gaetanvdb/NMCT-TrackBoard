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
    gpsDataList = []
    # voor altitude
    while status1 == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPGGA":
            gpsDataList.append(data[9])  #altitude --> 0
            gpsDataList.append(data[6]) #Fix --> 1
            status1 = 1
    # voor Time, date, latitude, longitude, speed
    while status2 == 0:
        line = str(ser.readline())
        data = line.split(",")
        if data[0] == "b'$GPRMC":
            gpsDataList.append(data[1]) #time --> 2
            gpsDataList.append(data[9]) #date --> 3
            gpsDataList.append(data[3]) #latitude --> 4
            gpsDataList.append(data[5]) #longitude --> 5
            gpsDataList.append(data[7]) #speed --> 6
            status2 = 1
    return gpsDataList


def getTime():
    vartime = getGpsData()[2]
    vardate = getGpsData()[3]
    utcDateTime = datetime(year= 2000 + int(vardate[4:6]),month=int(vardate[2:4]), day=int(vardate[0:2]), hour=int(vartime[0:2]), minute=int(vartime[2:4]), second=int(vartime[4:6]))
    gmtDateTime = utcDateTime + timedelta(hours=2)
    return gmtDateTime

def getSpeed():
    knots = getGpsData()[6]
    kmh = (float(knots) * 1.852)
    return kmh

def getDecLat():
    degreesLat = getGpsData()[4]
    latFirst = float(degreesLat[0:2])
    latSecond = float(degreesLat[2:-1])
    latDecimal = latFirst + latSecond/60
    return latDecimal

def getDecLong():
    degreesLong = getGpsData()[5]
    longFirst = float(degreesLong[0:3])
    longSecond = float(degreesLong[3:-1])
    longDecimal = longFirst + longSecond / 60
    return longDecimal

print(datetime.now())