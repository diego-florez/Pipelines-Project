import matplotlib.pyplot as plt
from adq_api import *
import pandas as pd
from pandas.plotting import table
import numpy as np

def ratings_plot():
    dfm = get_movie()
    df_title = dfm.Title[0]

    dfr = get_ratings()

    fig, ax = plt.subplots(1,1)

    x_pos = [i for i, _ in enumerate(dfr.Source)]

    plt.bar(x_pos, dfr.Value, color='green')
    plt.xlabel("Database")
    plt.ylabel("Rating")
    plt.title(f"{df_title} Ratins by Database")

    fig = plt.xticks(x_pos, dfr.Source)

    table(ax, np.round(dfr.describe(),2),loc="upper right",colWidths=[0.2, 0.2, 0.2])
    
    dfr.plot(ax=ax,use_index=(fig),xlim=(-1,6), ylim=(0, 1), legend=None)

    return plt.show()

plot = ratings_plot()
print(plot)