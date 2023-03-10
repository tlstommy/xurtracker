#! /bin/sh
sudo pkill gunicorn  
sudo rm /home/ubuntu/XurTracker/data/logger.txt
rm /home/ubuntu/XurTracker/data/logger.txt
touch /home/ubuntu/XurTracker/data/logger.txt
#run with config file
sudo gunicorn -c /home/ubuntu/XurTracker/gunicorn.conf.py wsgi:app
