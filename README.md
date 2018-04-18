# hf-api

hf-api is a request aggregator that saves the count, average, maximum, minimum for each key sent.

## Quick Start
```
mkdir ~/src
cd ~/src
git clone https://github.com/theologian/hf-api.git
cd hf-api
vagrant up
vagrant ssh 
bash /vagrant/setup.sh
nohup python /vagrant/hf-api/app.py &
bash /vagrant/hf-api/request_generator.sh 2
```
