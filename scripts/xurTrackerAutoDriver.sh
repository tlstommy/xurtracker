#! /bin/sh
date
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/tweetBotTweet.py
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/generateJSON.py
bash /home/ubuntu/XurTracker/scripts/regenerateHTML.sh
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/deleteOldManifests.py
cd /home/ubuntu/XurTracker/
/usr/bin/git pull
/usr/bin/git add .
/usr/bin/git commit -m "automated weekly update"
/usr/bin/git push -u origin master
/usr/bin/git push
echo committed!
echo fallback attempt...
sudo bash /home/ubuntu/XurTracker/scripts/autocommit.sh
sudo rm /home/ubuntu/*.content
sudo rm /home/ubuntu/manifest_zip