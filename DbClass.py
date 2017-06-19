class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "127.0.0.1",
            "user": "trackboard",
            "passwd": "Tr@ckB0@rd",
            "db": "dbtrackboard"
        }
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getUser(self, paraUser):
        # Query zonder parameters
        sqlQuery = "SELECT username, password FROM tblusers WHERE username = '" + paraUser + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getSessions(self):
        # Query zonder parameters
        sqlQuery = "SELECT sessionID, date, startTime, stopTime FROM tblsessions ORDER BY sessionID DESC;"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result
#------------------------------------------------------------------------------------------------
    # Queries for weekly - overview
# ------------------------------------------------------------------------------------------------
    def getWeekSessionCount(self):
        # Query zonder parameters
        sqlQuery = "SELECT COUNT(sessionID) as 'Total Sessions' FROM tblsessions WHERE date > (NOW() - INTERVAL 7 DAY);"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
# ------------------------------------------------------------------------------------------------
    def getWeekTotalTime(self):
        # Query zonder parameters
        sqlQuery = "SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime))) AS 'Total Time' FROM tblsessions WHERE date > (NOW() - INTERVAL 7 DAY);"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
# ------------------------------------------------------------------------------------------------
    def getWeekAverageTime(self):
        # Query zonder parameters
        sqlQuery = "SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime))) AS 'Total Time' FROM tblsessions WHERE date > (NOW() - INTERVAL 7 DAY);"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
#------------------- 3 IN 1 --------------
    #SELECT COUNT(sessionID) as 'Total Sessions', SEC_TO_TIME(SUM(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime))) AS 'Total Time', SEC_TO_TIME(AVG(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime))) AS 'AvG Time' FROM tblsessions WHERE date > (NOW() - INTERVAL 7 DAY);
# ------------------------------------------------------------------------------------------------
    def getWeekTopSpeed(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MAX(speed),2) FROM tblgps WHERE sessionID IN (SELECT sessionID FROM tblsessions WHERE tblsessions.date > (NOW() - INTERVAL 7 DAY));"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

# ------------------------------------------------------------------------------------------------
    def getWeekAverageSpeed(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(AVG(speed),2) FROM tblgps WHERE sessionID IN (SELECT sessionID FROM tblsessions WHERE tblsessions.date > (NOW() - INTERVAL 7 DAY));"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

# ------------------------------------------------------------------------------------------------
    def getWeekTotalDistance(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(SUM(totalDistance), 3) FROM tblsessions WHERE date > (NOW() - INTERVAL 7 DAY);"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
# ------------------------------------------------------------------------------------------------
    def getWeekHighestAltitude(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MAX(altitude),2) FROM tblgps WHERE sessionID IN (SELECT sessionID FROM tblsessions WHERE tblsessions.date > (NOW() - INTERVAL 7 DAY));"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

# ------------------------------------------------------------------------------------------------
    def getWeekLowestAltitude(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MIN(altitude),2) FROM tblgps WHERE sessionID IN (SELECT sessionID FROM tblsessions WHERE tblsessions.date > (NOW() - INTERVAL 7 DAY));"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

# ------------------------------------------------------------------------------------------------
    def getWeekAltitudeDifference(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE((MAX(altitude) - MIN(altitude)),2) as 'Altitude difference' FROM tblgps WHERE sessionID IN (SELECT sessionID FROM tblsessions WHERE tblsessions.date > (NOW() - INTERVAL 7 DAY));"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result
# ------------------- 5 IN 1 --------------
    # SELECT TRUNCATE(MAX(speed),2) as 'Max Speed', TRUNCATE(AVG(speed),2) as 'AVG Speed', TRUNCATE(MAX(altitude),2) as 'Max altitude', TRUNCATE(MIN(altitude),2) as 'Min altitude', TRUNCATE((MAX(altitude) - MIN(altitude)),2) as 'Altitude difference' FROM tblgps WHERE sessionID IN (SELECT sessionID FROM tblsessions WHERE tblsessions.date > (NOW() - INTERVAL 7 DAY));
# ------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    # Queries for TOTAL
    # ------------------------------------------------------------------------------------------------
    def getTotalSessionCount(self):
        # Query zonder parameters
        sqlQuery = "SELECT COUNT(sessionID) FROM tblsessions;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getTotalTotalTime(self):
        # Query zonder parameters
        sqlQuery = "SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime))) AS 'Total Time' FROM tblsessions;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getTotalAverageTime(self):
        # Query zonder parameters
        sqlQuery = "SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime))) AS 'AVG Time' FROM tblsessions;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getTotalTopSpeed(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MAX(speed),2) FROM tblgps;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getTotalAverageSpeed(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(AVG(speed),2) FROM tblgps;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getTotalDistance(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(SUM(totalDistance), 3) FROM tblsessions;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getTotalHighestAltitude(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MAX(altitude),2) FROM tblgps;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getTotalLowestAltitude(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MIN(altitude),2) FROM tblgps;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getTotalAltitudeDifference(self):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE((MAX(altitude) - MIN(altitude)),2) as 'Altitude difference' FROM tblgps;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result
#######################################################################################################
# ------------------------------------------------------------------------------------------------
# Voor coordinaten op map weer te geven
# ------------------------------------------------------------------------------------------------
    def getCoordinates(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT latitude, longitude FROM dbtrackboard.tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        #self.__cursor.close() pas sluiten na laatste query
        return result
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# Voor speed en time weer te geven in tabel
# ------------------------------------------------------------------------------------------------
    def getSpeedAndTime(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT truncate(speed, 2), time FROM dbtrackboard.tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        #self.__cursor.close() # PAS SLUITEN NA ALLE QUERIES
        return result
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

    def getSessionBegin(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT startTime FROM tblsessions WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getSessionEnd(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT stopTime FROM tblsessions WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getSessionDuration(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT SEC_TO_TIME(TIME_TO_SEC(stopTime) - TIME_TO_SEC(startTime)) AS 'Total Time' FROM tblsessions WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getSessionTopSpeed(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MAX(speed),2) FROM tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getSessionAverageSpeed(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(AVG(speed),2) FROM tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------
    def getSessionHighestAltitude(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MAX(altitude),2) FROM tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        # self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result

        # ------------------------------------------------------------------------------------------------

    def getSessionLowestAltitude(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE(MIN(altitude),2) FROM tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getSessionDistance(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT totalDistance FROM tblsessions WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close() #PAS SLUITEN NA ALLE QUERIES
        return result
        # ------------------------------------------------------------------------------------------------

    def getSessionAltitudeDifference(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT TRUNCATE((MAX(altitude) - MIN(altitude)),2) as 'Altitude difference' FROM tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result
#######################################################################################################

    def getDataFromDatabase(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tablename"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setDataToDatabase(self, value1):
        # Query met parameters
        sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()


#----------------------------------------------------------------------------------
    # New session with date and starttime
    def setNewSession(self, date, startTime):
        # Query met parameters
        sqlQuery = "INSERT INTO tblsessions (date, startTime) VALUES ('{param1}', '{param2}');"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=date, param2=startTime)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        #self.__cursor.close()

    #Select the last sessionID
    def getLastSessionID(self):
        # Query zonder parameters
        sqlQuery = "SELECT sessionID FROM tblsessions ORDER BY sessionID DESC LIMIT 1;"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        #self.__cursor.close()
        return result

    #Log gps data for new session
    def setNewGpsLine(self, time, latitude, longitude, speed, course, altitude, sessionID ):
        # Query met parameters
        sqlQuery = "INSERT INTO tblgps (time, latitude, longitude, speed, course, altitude, sessionID) VALUES ('{param1}', '{param2}', '{param3}', '{param4}', '{param5}', '{param6}', '{param7}');"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=time, param2=latitude, param3=longitude, param4=speed, param5=course, param6=altitude, param7=sessionID)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        #self.__cursor.close()

    # If the session is done, add the endTime
    def updateSession(self, stopTime, totalDistance):
        # Query met parameters
        sqlQuery = "UPDATE tblsessions SET stopTime = '{param1}', totalDistance = '{param2}' ORDER BY sessionID DESC LIMIT 1;"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=stopTime, param2=totalDistance)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        #self.__cursor.close()

    def closeConnection(self):
        self.__connection.close()
# ----------------------------------------------------------------------------------