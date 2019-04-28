# RESTful Flask micro service template

## Description
Project template to create a RESTful api using flask. Template can be replicated across multiple servers in order to create a micro service cluster.

## Windows Instructions

### Requirements
- Python 3.7 
- Docker

### Quick Start MacOS
1) Create virtual env and activate
    ```
    cd <root>
    python -m venv env
    source env/bin/activate
    ```
2) Export Flask settings
    ```
    export FLASK_APP=sample
    export FLASK_ENV=development
    ``` 
3) Run Flask
    ```
    flask run
    ```

    
### Setup Microservices
1) Replicate sample service
    Use the sample service to build a working api by adding logic to api.py
 
2) Start Docker

3) Modify Dockerfile
    ```
    FROM python:3.7
    
    WORKDIR /app
    
    COPY . /app
    
    COPY requirements.txt /app
    
    RUN pip install -r requirements.txt
    
    EXPOSE <port>
    
    RUN export FLASK_APP=<service name>
    
    RUN flask run
    ```
   
3) Build Docker container
    ```
    docker build -t <service name> .
    ```
4) Run Container
    ```
    docker run -p <exposed port>:<local port> <service name>
    ```

This method can be used to create multiple services within the docker container.
