#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/ProsperousHeart/django-rest-proj1.git'

# PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'
# PROJECT_BASE_PATH='/usr/local/apps/django-rest-proj1'
PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Create project directory
mkdir -p $PROJECT_BASE_PATH
# git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/django-rest-proj1

# Create virtual environment
# mkdir -p $PROJECT_BASE_PATH/env
mkdir -p $VIRTUALENV_BASE_PATH
# python3 -m venv $PROJECT_BASE_PATH/env
python3 -m venv $VIRTUALENV_BASE_PATH/profiles_api

# Install python packages
# $PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
# $VIRTUALENV_BASE_PATH/profiles_api/bin/pip install -r $PROJECT_BASE_PATH/profiles-rest-api/requirements.txt
$VIRTUALENV_BASE_PATH/profiles_api/bin/pip install -r $PROJECT_BASE_PATH/django-rest-proj1/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# # Run migrations and collectstatic
# cd $PROJECT_BASE_PATH
# $PROJECT_BASE_PATH/env/bin/python manage.py migrate
# $PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Run migrations
# cd $PROJECT_BASE_PATH/profiles-rest-api/src
cd $PROJECT_BASE_PATH/django-rest-proj1/src

# Configure supervisor
# cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
cp $PROJECT_BASE_PATH/django-rest-proj1/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Configure nginx
# cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
cp $PROJECT_BASE_PATH/django-rest-proj1/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
systemctl restart nginx.service

echo "DONE! :)"
