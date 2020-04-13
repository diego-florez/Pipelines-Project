import matplotlib.pyplot as plt
from adq_api import *
import pandas as pd
from pandas.plotting import table
import numpy as np

def ratings_plot():
    dfm = get_movie()
    df_title = dfm.Title[0]

    dfr = get_ratings()

    fig, ax = plt.subplots(figsize=(10,6))
    
    plt.ylabel("Ratings")
    plt.xlabel("Database")
    plt.title(f"{df_title} Ratings by Database")

    table(ax, np.round(dfr.describe(),2),loc="upper right",zorder=3,colWidths=[0.1, 0.1, 0.1])

    ax2 = ax.twinx()
    ax2.bar(dfr.Source, dfr.Value, color="green", alpha=0.5)
    ax2.set_xticks(ax2.get_xticks())
    plot = plt.savefig('../OUTPUT/plot.png')
    return plot