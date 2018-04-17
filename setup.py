sudo apt update
sudo apt-get install -y python-setuptools python-dev \
build-essential python-virtualenv python-pip redis-server

sudo -H -u vagrant virtualenv ~/virtualenv/hf-api
pip install -r /vagrant/requirements.txt

source ~/virtualenv/hfapi/bin/activate
