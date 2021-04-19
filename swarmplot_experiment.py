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

def one_swarm(randoms, compact):
    start_time = time.perf_counter()
    sns.swarmplot(x=randoms, size=2, compact=compact)
    plt.close()
    return time.perf_counter() - start_time

for rname, rfunc in rand_funcs:
    for iter in range(5):
        for sz in range(100, 3100, 100):
            print(rname)
            print(sz)
            randoms = rfunc(size=sz)
            timediff1 = one_swarm(randoms, False)
            timediff2 = one_swarm(randoms, True)
            print(timediff1)
            print(timediff2)
