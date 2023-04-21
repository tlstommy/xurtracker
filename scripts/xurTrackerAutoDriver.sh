#! /bin/sh
date
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/tweetBotTweet.py
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/generateJSON.py
bash /home/ubuntu/XurTracker/scripts/regenerateHTML.sh
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/deleteOldManifests.py
git pull
git add .
git commit -m "weekly update"
git push
echo committed!
echo fallback attempt...
sudo bash /home/ubuntu/XurTracker/scripts/autocommit.sh
sudo rm /home/ubuntu/*.content
sudo rm /home/ubuntu/manifest_zip