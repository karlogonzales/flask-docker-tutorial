from flask import Flask
from flask_restful import Api
from api.user import User
from flask.cli import FlaskGroup

app = Flask(__name__)

api = Api(app)
cli = FlaskGroup(app)

api.add_resource(User, '/api/user')
if __name__ == '__main__':
    cli()
