import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import functions as f


def get_oscars():
    url = ('https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films')

    soup = f.request(url)
    href = soup.find_all("href")

    lsts = [href.text.strip("\n") for href in soup.select("table.wikitable td")]
    title = lsts[0::4]
    year = lsts[1::4]
    awards = lsts[2::4]
    nominations = lsts[3::4]
    dic = {"title":title, "year":year, "awards":awards, "nominations":nominations}
    df_oscars = pd.DataFrame(dic)
    
    return df_oscars


oscars = get_oscars()
print(oscars)