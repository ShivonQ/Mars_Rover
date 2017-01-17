from flask import Flask
from flask import render_template
from flask import request
from database import DbHandler as DBH
from nasa_mars_rover_client import NasaMarsClient as nmrc
import parse_reqs as pr
app = Flask(__name__)
nmrc = nmrc()
db = DBH(nmrc)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='Welcome To The Rover Photo Explorer!',
                           user = 'you')

@app.route('/photos',methods=['POST'])
def images():

    req = request.get_data(as_text=True)
    print(req)
    data = pr.parse_name_and_date(req)
    # TODO: Make this reqeust parse into a dict, {name:name, date:date}, OR [name,date]
    '''
    We fetch the 3 common cams for this rover, pack them into that dictionary, with their cam names
    and also pass along the name, and date parameters
    '''
    three_cams_data = []
    for num in range(3):
        photos = nmrc.date_image_query(data[1], num, data[0])
        if photos != None:
            three_cams_data.append(photos)
        else:
            print('No Images, So No Addition')
        print(three_cams_data)

    # photos = db.fetch_photos_for_date(data,'Curiosity')

    return render_template('photos.html', photos=three_cams_data,
                                          rover_name=data[0],
                                          date=data[1])

@app.route('/rover_home', methods=['POST'])
def rover_home():
    # TODO: GET DATABASE INFO FROM DB
    data = request.get_data(as_text=True)
    split=data.split('=')
    print(split)
    manifest = db.fetch_mission_manifest(split[1])
    print(request.form)
    return render_template('rover_home.html',
                           rover_name=manifest.name,
                           launch_date=manifest.launch_date,
                           landing_date=manifest.landing_date,
                           max_date=manifest.max_date,
                           status=manifest.status,
                           total_photos=manifest.total_photos,
                           max_sol=manifest.max_sol)
if __name__ == '__main__':
    app.run()
