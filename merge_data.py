import pandas as pd
from adq_api import *
from adq_imdb import *



def check():
    dfm = get_movie()
    df_id = dfm.imdbID.iloc[0]
    df_title = dfm.Title[0]

    dfi = get_imdb()
    df_top = dfi.top_movies
    df_pop = dfi.popular_movies

    result = ""

    if df_id in df_top.values and df_id in df_pop.values:
        result = f"{df_title} is one of the Top Rated Movies and one of the Most Popular Movies based in imdb"
    elif df_id in df_top.values:
        result = f"{df_title} is one of the Top Rated Movies based in imdb"
    elif df_id in df_pop.values:
        result = f"{df_title} is one of the Most Popular Movies based in imdb"
    else:
        result = f"{df_title} is neither a Top Rated Movie nor one of the Most popular movies based in imdb"
    return result


result = check()
print(result)