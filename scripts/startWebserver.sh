#! /bin/sh
sudo pkill gunicorn  
sudo rm /home/ubuntu/XurTracker/data/logger.txt
#run with config file
sudo gunicorn -c /home/ubuntu/XurTracker/gunicorn.conf.py wsgi:app




#sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --max-requests 1000 --bind 0.0.0.0:443  --chdir /home/ubuntu/XurTracker wsgi:app
#sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --max-requests 1000 --bind 0.0.0.0:443  --chdir /home/ubuntu/XurTracker --access-logfile /home/ubuntu/XurTracker/data/logger.txt --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' wsgi:app
#sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --bind 0.0.0.0:443 wsgi:app
