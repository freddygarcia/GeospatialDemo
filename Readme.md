# Geospatial Demo

This project exposes an API using the dataset _grocery-store-locations-2-1.geo_ (from [data.world](https://data.world/dcopendata/1d7c9d0e3aac49c1aa88d377a3bae430-4)). The dataset contains information about grocery stores in the United States. The project also contains a ReactJS application that uses the API to display the grocery stores in a map.

Some cool things this project:

- The React application uses the [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial) to display the grocery stores in a map.
- The user is able to select and zoom in on a specific grocery store.
- Users can create a new grocery store location.


## Before you start

The basic requirement is in the branch [_only-api_](https://github.com/freddygarcia/geospatialdemo/tree/only-api) of the repository. It contains the Flask API setup and tests.
**This requirement duration was about 2 hours**.

The whole project is in the branch [_master_](https://github.com/freddygarcia/GeospatialDemo/tree/master). It contains the following:

- The Flask API setup.
- Flask tests with 86% coverage.
- Swagger documentation.
- The React application.
- Nginx reverse proxy.
- Postgres database with PostGIS support.
- _docker compose_ to handle development and deployment on AWS ECS.

I spent about 4 more hours putting everything together.

## Getting started

Please make sure before you start that you have the following:

- Docker installed and running.
- Docker compose installed.

To start the project, run the following command:

```
$ docker-compose -f docker/develop.yml --project-directory `pwd` up
```

By default, the project available at [http://localhost](http://localhost).
If you prefer to use a different port, you can change it in the **.env** file.

At `/` you will see the React application.

At `/api` you will see the API Swagger documentation.

At `GET: /api/stores/` you get a JSON list of all grocery stores.

At `GET: /api/stores/{id}` you get a JSON object with the grocery store information.

At `POST: /api/stores/` you can create a new grocery store.


## Geospatial-api testing

You can run the tests and get the coverage report with the following command:

```
$ python -m pytest --setup-show --cov=app --cov-config=.coveragerc --cov-report html
```

The coverage report is available at `htmlcov/index.html`.

<img src="https://user-images.githubusercontent.com/6600991/171801918-213ba0c0-3a87-4cb6-8cf1-5acd8725b827.png" width="500" />

## AWS

The project can be found at [http://geosp-loadb-1avw1ouse7vg4-15203507.us-west-2.elb.amazonaws.com/](http://geosp-loadb-1avw1ouse7vg4-15203507.us-west-2.elb.amazonaws.com/).
The deployment on AWS was made using the aws cli on a ECS Task. 


<img src="https://user-images.githubusercontent.com/6600991/171806847-99a28290-c7cd-4b13-8e59-d2fa0e5db707.png" width="500" />

<img src="https://user-images.githubusercontent.com/6600991/171806856-20495b8a-2f8c-4363-8127-e076dd6d6875.png" width="500" />

<img src="https://user-images.githubusercontent.com/6600991/171806867-79e0bbc0-3e6a-4a15-bf85-771b85953545.png" width="500" />

## Tech

This project uses a number of third party libraries to work properly:

- [Flask](https://flask.palletsprojects.com/en)
- [Flask RESTX](https://flask-restx.readthedocs.io/en/latest/)
- [SQL Alchemy](https://www.sqlalchemy.org/)
- [Postgres](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [React](https://reactjs.org/)
- [Google Maps API](https://developers.google.com/maps/documentation/javascript/)
- [Gunicorn](https://gunicorn.org/)

