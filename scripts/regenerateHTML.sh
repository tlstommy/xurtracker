#! /bin/sh
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/html/generateHTMLAllItems.py
echo "[Regenerated all_items.html]"
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/html/generateHTMLExotics.py
echo "[Regenerated exotic_items.html]"
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/html/generateHTMLLegendaryWeapons.py
echo "[Regenerated legendary_weapons.html]"
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/html/generateHTMLHunterArmor.py
echo "[Regenerated hunter_armor.html]"
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/html/generateHTMLTitanArmor.py
echo "[Regenerated titan_armor.html]"
sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/html/generateHTMLWarlockArmor.py
echo "[Regenerated warlock_armor.html]"