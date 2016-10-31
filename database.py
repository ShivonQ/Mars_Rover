from peewee import *
import sqlite3
from peewee_models import rover_mission_data
from peewee_models import rover_photo_data
import peewee_models as pm
import datetime

class DbHandler:
    def __init__(self):
        self.db = pm.db
        self.db.connect()
        self.db.create_tables([rover_mission_data, rover_photo_data],safe=True)

    @staticmethod
    def save_mission_manifest_data(rover_data):
        # date = datetime.date(int(date_list[0]),int(date_list[1]),int(date_list[2]))
        launch_date_list = DbHandler.modify_date(rover_data['launch_date'])
        launch_date = datetime.date(launch_date_list[0],launch_date_list[1],launch_date_list[2])
        landing_date_list = DbHandler.modify_date(rover_data['landing_date'])
        landing_date = datetime.date(landing_date_list[0],landing_date_list[1],landing_date_list[2])
        max_date_list = DbHandler.modify_date(rover_data['max_date'])
        max_date = datetime.date(max_date_list[0],max_date_list[1],max_date_list[2])
        total_photos = rover_data['total_photos']
        try:
            rover = rover_mission_data.create(name=rover_data['name'],launch_date=launch_date,
                                                             landing_date=landing_date,max_date=max_date,
                                                             total_photos=total_photos,status=rover_data['status'], max_sol=rover_data['max_sol'])

            rover.save()
        except IntegrityError as e:
            print(e)

    @staticmethod
    def save_photo_data(photo_data):
        name = photo_data['rover']
        date_list = DbHandler.modify_date(photo_data['earth_date'])
        date = datetime.date(int(date_list[0]),int(date_list[1]),int(date_list[2]))
        for url in photo_data['img_src']:
            try:
                photo = rover_photo_data.create(img_src=url, earth_date=date, name=name)
                print(photo)
                photo.save()
            except IntegrityError as e:
                print(e)

    @staticmethod
    def modify_date(date_str):
        date_list = date_str.split('-')
        count = 0
        for num in date_list:
            date_list[count] = int(num)
            count += 1
        return date_list

    @staticmethod
    def fetch_photos_for_date(date, rover_name):
        photos = rover_photo_data.get(rover_photo_data.name.startswith(rover_name).where(rover_photo_data.earth_date.startswith(date)))
        return photos

    @staticmethod
    def fetch_mission_manifest(rover_name):
        manifest = rover_mission_data.get(rover_mission_data.name.startswith(rover_name))
        return manifest
