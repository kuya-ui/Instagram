# Instagram
#### A website cloneofinstagram app
#### By MAXMILLAN KUYA
## Description
A website clone of instagram  where a user can create an account and sign in. It also has uploading of images,liking and commenting.


## Set Up and Installations
Requirements

1. Clone the repository
* Clone the the repository by running

* git clone https://github.com/kuya-ui/Instagram or download a zip file of the project from github

* Navigate to the project directory

* cd Insagram

2. Create a virtual environment
* Install Virtualenv pip install virtualenv

* To create a virtual environment named virtual, run virtualenv virtual

* To activate the virtual environment we just created, run source virtual/bin/activate

3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress

$ psql

* Then run the following query to create a new database named gallery

4.create database Galleria
5.Install dependencies
* To install the requirements from requirements.txt file,

* pip install -r requirements.txt
6.Create Database migrations
* Making migrations on postgres using django

* python3 manage.py makemigrations gallery

* then run the command below;

* python3 manage.py migrate

7.Run the app
* To run the application on your development machine,

* python3 manage.py runserver

### Clone the Repo

Run the command on  terminal:
`git clone https://github.com/kuya-ui/Instagram.git then cg Instagram`

### Activate virtual environment

Activate virtual environment using python3.6 as the default
virtualenv virtual
source venv/bin/activate

### Install dependencies

Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
psql
CREATE DATABASE '';
```
### .env file
Create .env file and  paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = '<dbname>'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration

python3.6 manage.py makemigrations
python3.6 manage.py migrate
```

### Run the app

python3.6 manage.py runserver

## Known bugs

No any known bugs

## Technologies used

    * Python 3.6
    * HTML
    * CSS
    * Bootstrap
    * Heroku

## Support and contact details

* kuyamaxmillan@gmail.com

### License

[MIT Licence](https://choosealicense.com/licenses/mit/)