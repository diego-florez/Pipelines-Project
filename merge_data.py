import pandas as pd
from adq_api import *
from adq_imdb import *
from adq_oscars import *



def check_imdb():
    dfm = get_movie()
    df_id = dfm.imdbID.iloc[0]
    df_title = dfm.Title[0]

    dfi = get_imdb()
    df_top = dfi.top_movies
    df_pop = dfi.popular_movies

    result = ""

    if df_id in df_top.values and df_id in df_pop.values:
        result = f"The movie {df_title} is one of the Top Rated Movies and one of the Most Popular Movies based in imdb"
    elif df_id in df_top.values:
        result = f"The movie {df_title} is one of the Top Rated Movies based in imdb"
    elif df_id in df_pop.values:
        result = f"The movie {df_title} is one of the Most Popular Movies based in imdb"
    else:
        result = f"The movie {df_title} is neither a Top Rated Movie nor one of the Most popular movies based in imdb"
    return result


result = check_imdb()
print(result)

def check_oscars():
    dfm = get_movie()
    df_id = dfm.imdbID.iloc[0]
    df_title = dfm.Title[0]

    df_oscars = get_oscars()
    year = df_oscars.loc[df_oscars.title==df_title, "year"].values[0]
    awards = df_oscars.loc[df_oscars.title==df_title, "awards"].values[0]
    nominations = df_oscars.loc[df_oscars.title==df_title, "nominations"].values[0]

    result = ""

    if df_title in df_oscars.title.values:
        result = f"The movie {df_title} in {year} Oscars ceremony had {awards} Oscars and {nominations} nominations"
    
    else:
        result = f"{df_title} didnt have any nominations in the Oscars ceremony"
    return result


r2 = check_oscars()
print(r2)