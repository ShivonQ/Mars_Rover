from flask import Flask
from flask import render_template
from flask import request
from database import DbHandler as DBH

app = Flask(__name__)
db = DBH()

@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='Welcome To The Rover Photo Explorer!',
                           user = 'you')

@app.route('/photo_display',methods=['POST'])
def image_carousel():
    data = request.get_data()
    photos = db.fetch_photos_for_date(data,'Curiosity')
    print(data)
    return render_template('photo_display.html',photos)

@app.route('/rover_home', methods=['POST'])
def rover_home():
    # TODO: GET DATABASE INFO FROM DB
    data = request.get_data(as_text=True)
    manifest = db.fetch_mission_manifest('Curiosity')
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
