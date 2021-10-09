# matcher-app

## build

docker-compose build
or
docker build .

## test

docker-compose run --rm app sh -c 'python manage.py test <appname> && flake8'
docker-compose run --rm app sh -c 'python manage.py test plant && flake8'

docker-compose run --rm app sh -c 'python manage.py test && flake8'

## new app

docker-compose run app sh -c 'python manage.py startapp <appname>'

## everytime we make a model change

docker-compose run --rm app sh -c 'python manage.py makemigrations <appname>'
docker-compose run --rm app sh -c 'python manage.py migrate <appname>'

docker-compose run app sh -c 'python manage.py makemigrations <appname>'

## removes container if we don't need it/optional

docker-compose run --rm ...

## runs local host server

docker-compose up

## removes containers

docker-compose down

## request Headers in Mod Headers extension

Authorization
Token ....
With token already in there, should be able to access info

/api/recipe/tags/?assigned_only=1
/api/recipe/tags/?assigned_only=0
/api/recipe/recipes/?ingredients=1

## Endpoints
admin/
api/user/ create/ [name='create']
api/user/ token/ [name='token']
api/user/ me/ [name='me']

api/user/id - GET, DELETE, PATCH

api/search/


api/space

miles within zip code
days preference?

api/space/ ^spaces/$ [name='space-list']
api/space/ ^spaces\.(?P<format>[a-z0-9]+)/?$ [name='space-list']
api/space/ ^spaces/(?P<pk>[^/.]+)/$ [name='space-detail']
api/space/ ^spaces/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='space-detail']
api/space/ ^spaces/(?P<pk>[^/.]+)/upload-image/$ [name='space-upload-image']
api/space/ ^spaces/(?P<pk>[^/.]+)/upload-image\.(?P<format>[a-z0-9]+)/?$ [name='space-upload-image']
api/space/ ^$ [name='api-root']
api/space/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^media/(?P<path>.*)$

/api/space/spaces/?users=1