#---------------------------------------------------------------------------------
import math
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
#---------------------------------------------------------------------------------
def afstandBerekenen(list):
    latList = []
    lngList = []
    for item in list:
        latList.append(item[0])
        lngList.append(item[1])

    totaleAfstand = 0
    i = 0
    while i < (len(latList) - 1):
        afstand = distance((latList[i], lngList[i]), (latList[i+1], lngList[i+1]))
        i += 1
        totaleAfstand += afstand
    return round(totaleAfstand, 3)