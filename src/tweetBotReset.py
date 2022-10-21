import tweepy
from credentials import * 

def resetTwitter():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        print("Error during authentication\n",e)
    api.update_profile(location="Unknown Space")
    api.update_profile_banner(filename="/home/ubuntu/XurTracker/imgs/unknownSpace.jpg") 

resetTwitter()