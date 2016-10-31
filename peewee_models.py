from database import *

db = SqliteDatabase('mars_rover_photo_data.db')


class base_model(Model):
    class Meta:
        database = db


class rover_photo_data(base_model):
    img_src = CharField
    earth_date = DateField
    name = CharField(max_length=15)

class rover_mission_data(base_model):
    name = CharField(max_length=15, unique=True)
    launch_date = DateField
    landing_date = DateField
    max_date = DateField
    total_photos = IntegerField
    status = CharField(max_length=20)
    max_sol = IntegerField