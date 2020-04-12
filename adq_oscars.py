import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import functions as f


def get_oscars():
    url = (f'https://www.imdb.com/event/ev0000003/{oscar}/1/?')

    soup = f.request(e)
    href = soup.find_all("href")

    lsts = [href for href in soup.select("#center-3-react > div > div > div:nth-child(1) > h3")]
    
    return lsts


def get_year():
    lst = []
    for oscar in range(2020,1929):
        lst=get_oscars(oscar) 
    return lst

oscars = get_year()
print(oscars)