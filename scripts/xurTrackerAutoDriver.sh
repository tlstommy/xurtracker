#! /bin/sh
date
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/tweetBotTweet.py
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/generateJSON.py
sudo netlify build --cwd=/home/ubuntu/XurTracker/frontend
sudo netlify deploy --prod --cwd=/home/ubuntu/XurTracker/frontend

bash /home/ubuntu/XurTracker/scripts/regenerateHTML.sh
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/deleteOldManifests.py
cd /home/ubuntu/XurTracker/
#/usr/bin/git pull
#/usr/bin/git add .
#/usr/bin/git commit -m "automated weekly update"
#/usr/bin/git push -u origin master
#/usr/bin/git push
#echo committed!
#echo fallback attempt...
#sudo bash /home/ubuntu/XurTracker/scripts/autocommit.sh
sudo rm /home/ubuntu/XurTracker/*.content
sudo rm /home/ubuntu/XurTracker/src/*.content
sudo rm /home/ubuntu/scripts/XurTracker/*.content
sudo rm /home/ubuntu/manifest_zip

#clear up vscode logs 
sudo rm -rf /home/ubuntu/.vscode-server

#run clean script
bash /home/ubuntu/XurTracker/scripts/clean.sh