import requests
import json
import os
from dotenv import load_dotenv
import re
import base64
import functions as f
import sys



def get_movie():
    movie = f.get_api()
    if movie["Response"] == "False":
        return sys.exit("The movie is not in the database or the name is not correct, please correct the name or try other movie")
    else:
        df_m = f.clean_movie(movie)
        return df_m


def get_ratings():
    movie = f.get_api()
    if movie["Response"] == "False":
        return sys.exit("The movie is not in the database or the name is not correct, please correct the name or try other movie")
    else:
        ratings = movie["Ratings"]
        if ratings == []:
            return sys.exit("This movie doesn't have ratings yet")
        else:
            df_r = f.clean_rating(ratings)
            return df_r

