import requests
from bs4 import BeautifulSoup
import re
import json
import os
from dotenv import load_dotenv
import pandas as pd
import argparse

#get argumets
def get_arg():
    parser = argparse.ArgumentParser(description="Find relevant info about the movie you like")
    parser.add_argument("--movie", "-m", help="Type a movie", required=True)
    arg = vars(parser.parse_args())
    arg = " ".join([e.replace(" ","+") for e in arg.values()])
    return arg

#action on adq_imdb.py file
def request(url):
    res = requests.get(url)
    print(res.status_code, res.url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup

#action on adq_imdb.py file
def find_ids(lsts):
    ids = []
    for e in lsts:
        s = re.search(r'(title/?)(.*)(\/" title?)',str(e))
        ids.append(s.group(2))
    return ids


#action on adq_api.py file
def get_api():
    load_dotenv()
    host = "http://www.omdbapi.com/"
    path = get_arg()
    apiKey = os.getenv("omdbapi_key")
    
    url = f"{host}?t={path}&apikey={apiKey}"
    
    res = requests.get(url)
    
    return res.json()


#action on adq_api.py file
def clean_movie(movie):
    df_m = pd.DataFrame([movie])
    df_m = df_m.iloc[0] if len(df_m.index) > 1 else df_m

    df_m = df_m[["Title", "Year", "Released", "Runtime", "Genre", 
    "Director", "Actors", "Language", "Country", "imdbID"]]
    return df_m

#action on adq_api.py file
def clean_rating(ratings):
    df_r = pd.DataFrame(ratings)
    rate = []
    for e in df_r.Value:
        if e[-2:] == "10":
            e = int(e.replace(".","").replace("/10",""))/100
            
        elif e[-1] == "%":
            e = int(e.replace("%",""))/100
            
        elif e[-3:] == "100":
            e = int(e.replace("/100",""))/100

        rate.append(e)
    df_r.Value = rate
    return df_r