#! /bin/sh

sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/tweetBotTweet.py
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/generateJSON.py
bash /home/ubuntu/XurTracker/scripts/regenerateHTML.sh
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/deleteOldManifests.py
git add /home/ubuntu/XurTracker/
git commit -m "weekly update"
git push
echo committed!
