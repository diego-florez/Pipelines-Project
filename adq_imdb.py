import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'

def get(url):
    res = requests.get(url)
    print(res.status_code, res.url)
    
    return res.text

res = get(url)
soup = BeautifulSoup(res, "html.parser")

t = [e.text for e in soup.select("td.titleColumn")][0:3]

print(t)