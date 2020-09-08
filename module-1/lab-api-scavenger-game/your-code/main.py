from dotenv import load_dotenv
import os
import json
import requests
import datetime
load_dotenv()
api_key = os.getenv("API_KEY")


def getFromGithub(path,queryParams=dict(),api_key=""):

    
    # Construct the resource url
    url = f"https://api.github.com{path}"
    
    # If apiKey is defined, pass a header
    headers = {"Authorization":f"token {api_key}"} if api_key else {}

    # Perform the request
    res = requests.get(url, params=queryParams, headers=headers)
    print(res.status_code, res.url)
    
    # Extract json from body response
    return res.json()

