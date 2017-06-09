class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "169.254.10.1",
            "user": "root",
            "passwd": "root",
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

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

    def getCoordinates(self, paraID):
        # Query zonder parameters
        sqlQuery = "SELECT latitude, longitude FROM dbtrackboard.tblgps WHERE sessionID = '" + paraID + "';"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

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