import time

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")

data = pd.read_csv("swarmplot_experiment_results.csv")

data["width_ratio"] = data["compact_width"] / data["classic_width"]

def scatter(x, y, title):
    fig, ax = plt.subplots(figsize=(7,7))
    max_point = max(max(data[x]), max(data[y])) * 1.01
    plt.xlim(0, max_point)
    plt.ylim(0, max_point)
    sns.scatterplot(ax=ax, data=data, x=x, y=y, hue="dist").set_title(title)
    plt.plot([0,max_point], [0,max_point], color='k', linestyle='-', linewidth=2)
    plt.show()
    plt.close()

scatter("classic_width", "compact_width", "Width of plot: classic vs compact beeswarm")
scatter("classic_time", "compact_time", "Beeswarm plot creation time: classic vs compact")

x = "n"
y = "width_ratio"
fig, ax = plt.subplots(figsize=(7,7))
sns.scatterplot(ax=ax, data=data, x=x, y=y, hue="dist").set_title(
    "Width ratio (compact width divided by classic width) by number of circles")
plt.show()
plt.close()
