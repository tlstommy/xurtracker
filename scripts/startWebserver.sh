#! /bin/sh
sudo pkill gunicorn  
sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --bind 0.0.0.0:443 wsgi:app
