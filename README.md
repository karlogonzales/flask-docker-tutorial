# RESTful Flask micro service template
## Description
Project template to create a RESTful api using flask and docker
### Microservices

#### Flask
The user management will provide the registering, login and authentication function exposed to the user. It will also provide the authentication token used by the UI to communicate with the System Logic service. In addition it will provide the interface for the other services to validate the user’s authentication tokens.  

#### Docker
The league manager service maps the data of the players with the appropriate user that has selected the player. It takes care of compiling the total amount of points for the players owned by each user.

#### Requirements
1) python 3.6.7^

## Windows Instructions
### Setup Restful Flask
1) Clone the repository: 
    ```
    https://github.com/karlogonzales/flask-docker-tutorial.git
    ```
2) Create a service directory and _init_ file
    ```
    cd <root>
    mkdir <service-name>
    type nul > _init_.py
    ```
4) Create a models directory and file
    ```
    mkdir \services\<service-name>\models
    type nul> \services\models\<model-name>.py
    ```
3) Create python virtual environment and activate:
    ```
    python -m venv services\<service-name>
    services\<service-name>\env\Scripts\activate.bat
    ```

5) Install Flask: 
    ```
    (env) pip install flask
    (env) pip install Flask-RESTful
    ```
5) Create basic flask application
    
    ```
    from flask import Flask, jsonify
    from flask_restful import Api

    app = Flask(__name__)

    api = Api(app)
    ```
6) Define api
    ```
    # user.py
    
    from flask_restful import Resource
    
    class User(Resource):
        def get(self):
            return {
                'status': 'ok',
                'message': 'Hello World'
            }

    ```
    
7) Add route to application in
    ```
    # _init_.py
    
    from services.template.api.user import User
    
    api.add_resource(User, '/api/user')
    ```
    
### Setup Docker

