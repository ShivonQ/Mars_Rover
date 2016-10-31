from peewee import *
import sqlite3
from peewee_models import rover_mission_data
from peewee_models import rover_photo_data
import peewee_models as pm

class DbHandler:
    def __init__(self):
        self.db = pm.db
        self.db.connect()
        self.db.create_tables([rover_mission_data, rover_photo_data])

    @staticmethod
    def save_mission_manifest_data(rover_data):
        rover = rover_mission_data(rover_mission_data.create(name=rover_data['name'],launch_date=rover_data['launch_date'],
                                                             landing_date=rover_data['landing_date'],max_date=rover_data['max_date'],
                                                             total_photos=rover_data['total_photos'],ststus=rover_data['status'], max_sol=rover_data['max_sol']))
        try:
            rover.save()
        except IntegrityError as e:
            print(e)

    @staticmethod
    def save_photo_data(photo_data):
        photos = rover_photo_data(rover_photo_data.create(img_src=photo_data['img_src'],
                                                          earth_date=photo_data['earth_date'],name=photo_data['rover']))
        try:
            photos.save()
        except IntegrityError as e:
            print(e)

    @staticmethod
    def fetch_photos_for_date(date, rover_name):
        photos = rover_photo_data.get(rover_photo_data.name.startswith(rover_name).where(rover_photo_data.earth_date.startswith(date)))
        return photos

    @staticmethod
    def fetch_mission_manifest(rover_name):
        manifest = rover_mission_data.get(rover_mission_data.name.startswith(rover_name))
        return manifest