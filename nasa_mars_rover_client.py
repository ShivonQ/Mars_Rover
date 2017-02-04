import requests
from api_key import key as key


class NasaMarsClient:
    def __init__(self):
        self.photo_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'
        self.manifest_url = 'https://api.nasa.gov/mars-photos/api/v1/manifests/'

        self.rover = ['Spirit','Opportunity','Curiosity']
        self.key = 'api_key=' + key

    def get_rovers(self):
        return self.rover

    # todo: change rover_num to a name
    def date_image_query(self, date,cam_num, rover_name):
        # modify in the future so that multiple cameras can be added
        # Rover_number is a list number, 0,1,2
        earth_date = 'earth_date='
        date = date
        # 0,1,2 are the options
        common_cams = ['navcam','rhaz','fhaz']
        constructed_url = self.photo_url + rover_name + '/photos?' + earth_date + date +'&camera='+ common_cams[cam_num] + '&'+self.key
        # if there are photos then a keyerror wont occur
        try:
            info = requests.get(constructed_url)
            # print(info.json())
            data = {'cam_name': common_cams[cam_num], 'img_src': []}
            photo_urls = []
            for photo in info.json()['photos']:
                for photo_url in photo:
                    if photo_url == 'img_src':
                        photo_urls.append(photo[photo_url])
            data['img_src'] = photo_urls
            # print(data)
            # print(photo_list)
            return data
        # otherwise a key error will occur
        except KeyError as e:
            # return None in that case
            print('No Images From that Query to the API')
            return None


    def mission_manifest_data(self, rover_name):

        name = rover_name
        constructed_url = self.manifest_url+name+'?'+self.key

        info = requests.get(constructed_url)
        # "name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active","max_sol":1502,"max_date":"2016-10-27"
        base_mission_manifest = {}
        # {"sol": 1, "total_photos": 16, "cameras": ["MAHLI", "MAST", "NAVCAM"]},
        all_days_of_missions = []
        for piece in info.json()['photo_manifest']:
            if piece != 'photos':
                base_mission_manifest[piece] = info.json()['photo_manifest'][piece]
                print(base_mission_manifest)
        return base_mission_manifest
        # print(info.json())

    # def get_manifest(self, rover_num):




