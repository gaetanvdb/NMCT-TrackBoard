from DbClass import DbClass
import distanceCalculator
import sys, os
db = DbClass()

import RPi.GPIO as GPIO
import time
from subprocess import call
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
            if not GPIO.input(drukknop):
                GPIO.output(ledRood, 1)
                GPIO.output(ledGroen, 0)
                print("Programma in stand-by")
                button='down'
                session = 'recording'

        elif (button=='down' and   session=='recording'):
            # stay in this state until button released
            if GPIO.input(drukknop):
                button='up'

        elif (button=='up' and session=='recording'):
            time.sleep(0.3)
            if not GPIO.input(drukknop):
                print("A new session just started")
                GPIO.output(ledGroen, 1)
                GPIO.output(ledRood, 0)
                time.sleep(1) #anders start de sessie niet!!
                from model import gpsData
                db.setNewSession(gpsData.getTime(), gpsData.getTime())
                #-----------------------------
                while GPIO.input(drukknop):
                    if float(gpsData.getGpsData()[1]) != 0: #Als de gps connectie heeft met een satteliet
                        db.setNewGpsLine(gpsData.getTime(), gpsData.getDecLat(), gpsData.getDecLong(),gpsData.getSpeed(), "00", gpsData.getGpsData()[0], db.getLastSessionID()[0])
                        print("Data inserted successfully ")
                    else:
                        print("No connection with satellite")
                # -----------------------------
                for i in range(5):
                    GPIO.output(ledRood, 1)
                    time.sleep(0.2)
                    GPIO.output(ledRood, 0)
                    time.sleep(0.2)
                coordinates = db.getCoordinates(str(db.getLastSessionID()[0]))
                print(coordinates)
                totaleAfstand = distanceCalculator.afstandBerekenen(coordinates)
                print(totaleAfstand)
                db.updateSession(gpsData.getTime(), totaleAfstand) #Session EndTime
                GPIO.output(ledGroen, 0)
                print("Logging DONE")
                for i in range(5):
                    GPIO.output(ledRood, 1)
                    time.sleep(0.2)
                    GPIO.output(ledRood, 0)
                    time.sleep(0.2)
                button = 'down'
                session = 'NOT-recording'
                call("sudo reboot", shell=True)

except Exception as e:
    print("Stopped:" + str(e))
    exc_type, exc_obj, exc_tb = sys.exc_info() #error type en lijn
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    GPIO.output(ledGroen, GPIO.LOW)
    GPIO.output(ledRood, GPIO.LOW)
    GPIO.cleanup()