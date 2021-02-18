# Car API
A technical recruitement task to build a simple REST API that is interacting with an external API

the project can be accessed at https://mjanusz-car-api.herokuapp.com/

## Technologies
* Python 3.9
* Django 3.1.6
* Django REST Framework 3.12.2
* Docker 20.10.3
* docker-compose 1.28.2

## Setup
To run this project you have to have Docker and docker-compose installed locally

Enter the project's root directory and execute commands 

```
docker-compose build

docker-compose run web python3 manage.py migrate

docker-compose run web python3 manage.py loaddata data.json

docker-compose up
```

The development server should start and the app should be accessible at [localhost:8000](localhost:8000) or the local ip address of the machine

## URLs

/cars/ : GET - list of all cars with avg_rating, POST - add a new car to local db by checking its existence in an external API, 'make' and 'model' in request

/cars/{id} : DELETE - delete a car with id = {id}

/rate/ : POST - rate a car 'car_id' and 'rating' in request

/popular/ : GET - list of the most popular cars based on no. rates
