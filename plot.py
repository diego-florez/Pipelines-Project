import matplotlib.pyplot as plt
from adq_api import *
import pandas as pd

def ratings_plot():
    dfm = get_movie()
    df_title = dfm.Title[0]

    dfr = get_ratings()

    x_pos = [i for i, _ in enumerate(dfr.Source)]

    plt.bar(x_pos, dfr.Value, color='green')
    plt.xlabel("Database")
    plt.ylabel("Rating")
    plt.title(f"{df_title} Ratins by Database")

    plt.xticks(x_pos, dfr.Source)

    return plt.show()

plot = ratings_plot()
print(plot)