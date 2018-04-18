#!/bin/bash

sudo apt update
sudo apt-get install -y python-setuptools python-dev \
build-essential python-virtualenv python-pip redis-server

mkdir  ~/virtualenv/hf-api/
sudo -H -u vagrant virtualenv ~/virtualenv/hf-api
pip install -r /vagrant/requirements.txt

source ~/virtualenv/hf-api/bin/activate

#while true; do curl -X POST "http://localhost:3000/?p1=2&p2=99"; sleep 5; done
