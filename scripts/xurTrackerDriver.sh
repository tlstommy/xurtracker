#! /bin/sh

#help menu function
Help()
{
    echo "usage: xurTrackerDriver -m [mode] -c [command]"
    echo -e "\nFLAGS:"
    echo "  - m     mode to run."
    echo "  - c     command for mode, if applicable."
    echo -e "\nMODES:"
    echo "  - twitter       update the status of @XurTrack."
    echo "  - generate      generate new HTML/JSON."
    echo "  - clean         clean out old manifests."
    echo "  - oauth         generate new oauth tokens."
    echo "  - webserver     start/stop the webserver."
}


while getopts m:c: flag
do
    case "${flag}" in
        m) mode=${OPTARG};;
        c) command=${OPTARG};;
    esac
done

#error check. may not be the best way to do this...
if [[ "$mode" == "twitter" || "$mode" == "generate" || "$mode" == "clean" || "$mode" == "oauth" || "$mode" == "webserver" || "$mode" == "help" ]];then :
else
    Help
fi


if [[ "$mode" == "twitter" ]];then
    echo "Twitter mode"
    if [[ "$command" == "tweet" ]];then
        sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/tweetBotTweet.py
        echo "[sent a new tweet]"
    fi

    if [[ "$command" == "reset" ]];then
        sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/tweetBotReset.py
        echo "[reset twitter to xur left state]"
    fi

    if [[ "$command" != "tweet" && "$command" != "reset" ]];then
        echo "usage: xurTrackerDriver -m twitter -c [command]"
        echo -e "\nCommands:"
        echo "  - tweet     Tweet out Xur's information."
        echo "  - reset     Reset @XurTrack when Xur has left the system."
    fi    

fi

if [[ "$mode" == "generate" ]];then
    echo "generate mode"
    if [[ "$command" == "html" ]];then
        echo "generate mode - html"
        bash regenerateHTML.sh
        echo "[regenerated all html files]"
    fi

    if [[ "$command" == "json" ]];then
        echo "generate mode - json"
        sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/generateJSON.py
        echo "[regenerated data json]"
    fi

    if [[ "$command" != "html" && "$command" != "json" ]];then
        echo "usage: xurTrackerDriver -m generate -c [command]"
        echo -e "\nCommands:"
        echo "  - html      Regenerate new HTML."
        echo "  - json      Regenerate new JSON."
    fi    
fi

if [[ "$mode" == "clean" ]];then
    echo "clean mode"
    sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/deleteOldManifests.py
    echo "[cleaned manifests]"

fi

if [[ "$mode" == "oauth" ]];then
    echo "oauth mode"
    sudo /usr/bin/python3 /home/ubuntu/XurTracker/src/regenerateToken.py
    echo "[regenerated oAuth tokens]"
fi

if [[ "$mode" == "webserver" ]];then
    echo "web mode"
    if [[ "$command" == "start" ]];then
        sudo pkill gunicorn && sudo gunicorn --certfile=/home/ubuntu/XurTracker/data/cert.pem --keyfile=/home/ubuntu/XurTracker/data/key.pem --workers=5 --threads=2 --bind 0.0.0.0:443 wsgi:app  
    fi

    if [[ "$command" == "kill" ]];then
        sudo pkill gunicorn
        echo "[killed webserver]"
    fi

    if [[ "$command" != "start" && "$command" != "kill" ]];then
        echo "usage: xurTrackerDriver -m webserver -c [command]"
        echo -e "\nCommands:"
        echo "  - start     Start up the webserver."
        echo "  - kill      Kill the webserver."
    fi    
fi