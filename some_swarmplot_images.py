import time

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")
rand_funcs = [
    ("uniform", np.random.uniform),
    ("normal", np.random.uniform),
    ("lognormal", np.random.uniform)
]

def one_swarm(randoms, rname, sz, compact):
    sns.swarmplot(x=randoms, size=4, compact=compact)
    plt.savefig("swarmplot_images/{}-{}-{}.png".format(
        rname, sz, compact), dpi=300)
    plt.close()

for rname, rfunc in rand_funcs:
    for iter in range(1):
        for sz in range(200, 1000, 200):
            randoms = rfunc(size=sz)
            one_swarm(randoms, rname, sz, False)
            one_swarm(randoms, rname, sz, True)
