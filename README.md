
# django-drf-vue-postgres-todoapp

## Setup the backend

go to backend folder

`$ cd backend`

create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
ENV_NAME='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'

run the command:

`python manage.py migrate`

finally the project run with: 

`$ python manage.py runserver`

open your RESTCLIENT (like postman) in: 

`GET http://localhost:8000/text/`\
`GET http://localhost:8000/image/`\
`POST http://localhost:8000/convert/`

## Setup the frontend

go to frontend folder and

`$ cd frontend`

install dependencies

`$ npm install`

and run server

`$ npm run serve`

open your browser in:

`http://localhost:8080/`
