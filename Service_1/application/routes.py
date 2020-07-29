from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random
from os import environ



# 3a617fb3dde7803d7e4513616c2973ee secret key

# export SECRET_KEY=3a617fb3dde7803d7e4513616c2973ee
# export MYSQL_USER=root
# export MYSQL_PASSWORD=hwg10IAR
# export MYSQL_HOST=34.105.241.68
# export MYSQL_PORT=3306
# export MYSQL_DB_NAME=sfia2db
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# @app.route('/', methods=['GET', 'POST'])
# def home():
    
#     piratename = requests.get('http://service_4:5003/piratename')
#     print(piratename)
#     piratename = response.text
#     post_data = Pirate(
#         pirate_name=piratename
#     )
#     return render_template('index.html', piratename = piratename, title = 'Home')

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/piratename')
    print(response)
    piratename = response.text
    return render_template('index.html', piratename = piratename, title = 'Home')

@app.route('/add', methods=['GET', 'POST'])
def add():

    post_data = Pirate(
        pirate_name=piratename
    )
    db.session.add(post_data)
    db.session.commit()
    return redirect(url_for('/'))



class Pirate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pirate_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "".join(
            [
                'Name: ' + self.pirate_name 

            ]
        )


