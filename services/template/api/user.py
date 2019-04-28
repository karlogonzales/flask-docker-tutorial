from flask_restful import Resource


class User(Resource):
    def get(self):
        return {
            'status': 'ok',
            'message': 'Hello World'
        }
