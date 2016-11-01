from database import *

db = SqliteDatabase('mars_rover_photo_data.db')


class base_model(Model):
    class Meta:
        database = db


class rover_photo_data(base_model):
    img_src = CharField(max_length=500, unique=True)
    earth_date = DateField('yyyy-mm-dd')
    name = CharField(max_length=15)

class rover_mission_data(base_model):
    name = CharField(max_length=15, unique=True)
    launch_date = DateField('yyyy-mm-dd')
    landing_date = DateField('yyyy-mm-dd')
    max_date = DateField('yyyy-mm-dd')
    total_photos = IntegerField(null=False)
    status = CharField(max_length=20)
    max_sol = IntegerField(null=False)