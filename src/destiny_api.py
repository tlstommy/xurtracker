#handles all apu requests to the Destiny 2 API as well as decoding logic
import requests
import json
import aiohttp
import asyncio

#Make a GET request to api and return json
def get_api_request(url, headers):
    try:

            #get api request
            res = requests.get(url, headers=headers)
            
            jsonResponse = json.dumps(res.json(), sort_keys=True, indent=4)

    except aiohttp.client_exceptions.ClientResponseError as e:
        print("ERROR: Could not connect to Bungie.net Endpoint")

    return jsonResponse

async def decode_hash(destiny, hash, manifest_value):
     return await destiny.decode_hash(hash, manifest_value)