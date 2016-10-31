from nasa_mars_rover_client import *
from database import DbHandler
db = DbHandler()
NMC = NasaMarsClient()
record = NMC.date_image_query('2016-4-13',1,2)
db.save_photo_data(record)
# NMC.mission_manifest_data(2)