#! /bin/sh
sudo pkill gunicorn  
sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --max-requests 1000 --bind 0.0.0.0:443  --chdir /home/ubuntu/XurTracker --access-logfile /home/ubuntu/XurTracker/data/logger.txt wsgi:app
#sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --bind 0.0.0.0:443 wsgi:app
