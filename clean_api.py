import pandas as pd
from test import *

#clean df_m

df_m = pd.DataFrame(movie)

df_m = df_m.iloc[0]

df_m = df_m[["Title", "Year", "Released", "Runtime", "Genre", 
"Director", "Actors", "Language", "Country"]]


#clean df_r

df_r = pd.DataFrame(ratings)

def clean_rating(df_r):
    rate = []
    for e in df_r.Value:
        if e[-2:] == "10":
            e = int(e.replace(".","").replace("/10",""))/100
            
        elif e[-1] == "%":
            e = int(e.replace("%",""))/100
            
        elif e[-3:] == "100":
            e = int(e.replace("/100",""))/100

        rate.append(e)
    return rate

df_r.Value = clean_rating(df_r)

print(df_m,"\n")
print(df_r)

