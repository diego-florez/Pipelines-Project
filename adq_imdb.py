import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import functions as f


def get_imdb():
    url = ('http://www.imdb.com/chart/top?','https://www.imdb.com/chart/moviemeter/?')
    both_lsts = []

    for e in url:      
        soup = f.request(e)
        href = soup.find_all("href")

        lsts = [href for href in soup.select("td.titleColumn")]
        lsts = f.find_ids(lsts)
        both_lsts.append(lsts)
    
    df_tp = pd.DataFrame({"top_movies": pd.Series(both_lsts[0]), "popular_movies": pd.Series(both_lsts[1])})
    return df_tp

df_tp = get_imdb()

print(df_tp)
