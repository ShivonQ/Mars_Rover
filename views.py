from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='Welcome To The Rover Photo Explorer!',
                           user = 'you')

@app.route('/rover_home', methods=['POST'])
def rover_home():
    # TODO: GET DATABASE INFO FROM DB
    data = request.get_data()
    print(data)
    return render_template('rover_home.html',
                           rover_name='curiosity')
if __name__ == '__main__':
    app.run()
