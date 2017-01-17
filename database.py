from peewee import *
import sqlite3
from peewee_models import rover_mission_data
from peewee_models import rover_photo_data
import peewee_models as pm
import datetime
import time

class DbHandler:
    def __init__(self, nmrc):
        self.db = pm.db
        self.db.connect()
        self.db.create_tables([rover_mission_data, rover_photo_data],safe=True)
        self.api = nmrc
        # TODO: this goes into a sceduler thread object...
        # TODO: CAN ALSO BECOME A HEROKU SCHEDULER THING
        # self.update_mission_manifest()
        # schedule.every().day.at("10:30").do(self.update_mission_manifest())


    # TODO: Create a Scheduler of some kind to do this (USE HEROKU : https://devcenter.heroku.com/articles/clock-processes-python ).
    def update_mission_manifest(self):
        # for each of the three rovers
        for rover_num in range(0, 3):
            # grab the new data
            manifest = self.api.mission_manifest_data(rover_num)
            # pass the name tofetch the record to delete
            del_man = self.fetch_mission_manifest(manifest['name'])
            # /delete that row
            del_man.delete_instance()
            # save the new data
            self.save_mission_manifest_data(manifest)
        print('Rover Manifest Data Updated')

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
            rover = rover_mission_data.create(name=rover_data['name'],
                                              launch_date=launch_date,
                                              landing_date=landing_date,
                                              max_date=max_date,
                                              total_photos=total_photos,
                                              status=rover_data['status'],
                                              max_sol=rover_data['max_sol'])

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
                print('Those Photos Already Exist in The DB, ignore Save Request')

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
