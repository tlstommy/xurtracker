#https://d2bearer.tlstommy.com/

import requests
from credentials import *


#POST request parameters
params = {
    'grant_type': 'refresh_token',
    'refresh_token': OAUTH_REFRESH_TOKEN,
    'client_id': OAUTH_CLIENT_ID,
    'client_secret': OAUTH_CLIENT_SECRET
}

#send the refresh post request to the oauth endpoint
response = requests.post("https://www.bungie.net/Platform/App/OAuth/Token/", data=params)

#handle request incase it failed somehow
if response.status_code == 200:
    
    #grab tokens
    accessToken = response.json()['access_token']
    refreshToken = response.json()['refresh_token']
    print('Access token refreshed!')
    print(response.json())
    #save the tokens
    with open(OAUTH_REFRESH_TOKEN_LOCATION, 'w') as f:
        f.write(refreshToken)
        f.close()
    with open(OAUTH_ACCESS_TOKEN_LOCATION, 'w') as f:
        f.write(accessToken)
        f.close()
else:
    print(f"Error refreshing tokens: {response.json()['error_description']}")