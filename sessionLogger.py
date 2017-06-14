from DbClass import DbClass
db = DbClass()

#db.setNewSession('2010-10-10', '10:00:00')
#db.updateSession('11:00:00')

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
list = []

try:
    while True:
        if (button=='up'   and   session == 'NOT-recording'):
            # wait for button press before changing anything
            if not GPIO.input(drukknop):
                GPIO.output(ledRood, 1)
                GPIO.output(ledGroen, 0)
                button='down'
                session = 'recording'

        elif (button=='down' and   session=='recording'):
            # stay in this state until button released
            if GPIO.input(drukknop):
                button='up'

        elif (button=='up' and session=='recording'):
            if not GPIO.input(drukknop):
                GPIO.output(ledGroen, 1)
                GPIO.output(ledRood, 0)
                # Sessie recording ------------
                time.sleep(1)
                while GPIO.input(drukknop) == 1:
                    knop = GPIO.input(drukknop)
                    db.setNewGpsLine(gpsData.getTime(), gpsData.getGpsData()[5], gpsData.getGpsData()[6], gpsData.getGpsData()[7], "99", gpsData.getGpsData()[0], "8")
                    #db.setNewGpsLine(time, latitude, longitude, speed, course, altitude, sessionID)

                    print("insert succesvol")
                    time.sleep(0.5)
                #-----------------------------
                #Rode led laten branden zodat gebruiker weet dat recording gestopt is -------
                GPIO.output(ledGroen, 0)
                GPIO.output(ledRood, 0)
                # -----------------------------
                # Data verwerken -----------------------------
                print(list)
                list.clear()
                # -----------------------------
                button = 'down'
                session = 'NOT-recording'
                for i in range(5):
                    GPIO.output(ledRood, 1)
                    time.sleep(0.2)
                    GPIO.output(ledRood, 0)
                    time.sleep(0.2)

                sys.exit("Gedaan")
        elif (button=='down' and session=='NOT-recording'):
            if GPIO.input(drukknop):
                button='up'
        time.sleep(0.1)
except KeyboardInterrupt:
    print("KeyboardInterrupt detected")
    GPIO.output(ledGroen, GPIO.LOW)
    GPIO.output(ledRood, GPIO.LOW)
    GPIO.cleanup()