#! /bin/sh

git pull
git add --all
now=$(date)
git commit -m "Weekly Auto-Commit at : $now"
git push -u origin main
echo committed!
