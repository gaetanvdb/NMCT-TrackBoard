from DbClass import DbClass
db = DbClass()

import RPi.GPIO as GPIO
import time
import sys
from model import gpsData

GPIO.setwarnings(False)

drukknop  = 21
ledGroen = 16
ledRood = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledGroen, GPIO.OUT)
GPIO.setup(ledRood, GPIO.OUT)
GPIO.setup(drukknop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button='up'
session='NOT-recording'

try:
    while True:
        if (button=='up'   and   session == 'NOT-recording'):
            # wait for button press before changing anything
            GPIO.output(ledRood, 1)
            GPIO.output(ledGroen, 0)
            if not GPIO.input(drukknop):

                button='down'
                session = 'recording'

        elif (button=='down' and   session=='recording'):
            # stay in this state until button released
            if GPIO.input(drukknop):
                button='up'

        elif (button=='up' and session=='recording'):
            if GPIO.input(drukknop):
                print("A new session just started")
                GPIO.output(ledGroen, 1)
                GPIO.output(ledRood, 0)
                time.sleep(1) #anders start de sessie niet!!
                db.setNewSession(gpsData.getTime(), gpsData.getTime())
                while GPIO.input(drukknop) == 1:
                    if float(gpsData.getGpsData()[1]) != 0: #Als de gps connectie heeft met een satteliet
                        db.setNewGpsLine(gpsData.getTime(), gpsData.getDecLat(), gpsData.getDecLong(), gpsData.getSpeed(), "00", gpsData.getGpsData()[0], db.getLastSessionID()[0])
                        print("Data inserted successfully ")
                    else:
                        print("No connection with satellite")
                GPIO.output(ledGroen, 0)
                GPIO.output(ledRood, 0)
                # Data verwerken -----------------------------
                db.updateSession(gpsData.getTime()) #Session EndTime
                print("Session just ended!")
                for i in range(5):
                    GPIO.output(ledRood, 1)
                    time.sleep(0.2)
                    GPIO.output(ledRood, 0)
                    time.sleep(0.2)
                button = 'up'
                session = 'NOT-recording'

except:
    print("Stopped")
    GPIO.output(ledGroen, GPIO.LOW)
    GPIO.output(ledRood, GPIO.LOW)
    GPIO.cleanup()