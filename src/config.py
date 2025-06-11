from credentials import *
import pydest

HEADERS = { "X-API-Key": API_KEY, "Authorization": f"Bearer {ACCESS_TOKEN}" }

pydestDestiny = pydest.Pydest(apiKey)