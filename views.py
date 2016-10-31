from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='Welcome To The Rover Photo Explorer!',
                           user = 'you')

@app.route('/photo_display',methods=['POST'])
def image_carousel():
    data = request.get_data(as_text=True)
    print(data)

@app.route('/rover_home', methods=['POST'])
def rover_home():
    # TODO: GET DATABASE INFO FROM DB
    data = request.get_data(as_text=True)
    print(request.form)
    print(data)
    print(data)
    return render_template('rover_home.html',
                           rover_name='curiosity')
if __name__ == '__main__':
    app.run()
