from flask import Flask
app = Flask(__name__)
app.secret_key='pineapple'
DATABASE = 'burgers'


from flask_app.controllers import burgers
