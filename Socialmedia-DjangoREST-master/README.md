
# Socialmedia-DjangoREST

Design an API for a posts like/dislike system for a social media site similar to facebook, instagram, etc... the system allows users to see posts 
that have been added by the admin and users are allowed to either like or dislike the posts and the next set of posts should be based on posts users previously liked or disliked.

## Getting Started with project
PipEnv is a way to create virtual environments in Python that allows for environment agnostic dependency installation.

git clone https://github.com/Ananthan7/Socialmedia-DjangoREST.git

python3 -m pip3 install pipenv

start by just grabbing a pipenv shell in the root directory

pipenv shell

cd media 

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver

view http://127.0.0.1:8000

http://127.0.0.1:8000/admin

USER ADMIN: admin1234@gmail.com
PASSWORD: admin1234

GET social media post added by only admin at : http://127.0.0.1:8000/api/post/

User signup : http://127.0.0.1:8000/api/user/ (postman testing use json format below & method=post) Example:
{
    "email": "name@dev.com",
    "password": "12345",
    "is_superuser": "True"
}

LOGIN : http://127.0.0.1:8000/api/user/login/ (postman testing use Body formdata add email & password as key value pairs )

LOGOUT : http://127.0.0.1:8000/api/user/logout/ID (id is generated and returned in json while signup plese use at ID )(postman testing use Body formdata add email & password as key value pairs)

Used Token Authentication for user login Token generates automatically
