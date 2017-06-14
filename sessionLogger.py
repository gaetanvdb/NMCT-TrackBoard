from DbClass import DbClass

db = DbClass()

db.setNewSession('2010-10-10', '10:00:00')
db.updateSession('11:00:00')