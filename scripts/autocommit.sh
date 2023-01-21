#! /bin/sh

git pull
git add --all
now=$(date)
git commit -m "Auto-Commit at : $now"
git push -u origin main
echo committed!
