import requests
import json
import requests
import os
from dotenv import load_dotenv
import re
import base64



def getFromGithub(path,apiKey=""):
    
    url = f"http://www.omdbapi.com/?{path}apikey={apiKey}"
    
    res = requests.get(url)
    
    return res.json()



load_dotenv()

apiKey = os.getenv("omdbapi_key")

movie = getFromGithub("t=The+Godfather&", apiKey=apiKey)

ratings = movie["Ratings"]