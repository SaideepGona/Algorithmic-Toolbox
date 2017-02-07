import pandas as pd
import seaborn
from altair import Chartelope_calcs(n):
    running_counts = [0]

    for x in range(1, n + 1):
        previous_calcs = []

        if int(x % 3) != 0:
            previous_calcs.append(x + 1)
        elif int(x % 3) == 0 and x != 0:
            previous_calcs.append(running_counts[(x // 3)])

        if int(x % 2) != 0:
            previous_calcs.append(x + 1)
        elif int(x % 2) == 0:
            previous_calcs.append(running_counts[(x // 2)])

        previous_calcs.append(running_counts[x - 1])

        running_counts.append(min(previous_calcs) + 1)

    return running_counts

df = pd.DataFrame()

nums = develope_calcs(200)
therange = range(201)

df['x'] = therange
df['y'] = nums

seaborn.lmplot('x', 'y', data=df, fit_reg=True)

# ALTAIR
c = Chart(df).mark_line().encode(
    x='x',
    y='y',
    color='kind'
)
print(c)
import matplotlib

def dev