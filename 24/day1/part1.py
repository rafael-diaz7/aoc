import pandas as pd
import math

df = pd.read_csv('input', names=['x', 'y'], delimiter='   ')
s = 0
for x, y in zip(sorted(df['x'].to_list()), sorted(df['y'].to_list())):
    s += math.fabs(x - y)
print(s)