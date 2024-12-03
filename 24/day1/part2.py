import pandas as pd

df = pd.read_csv('input', names=['x', 'y'], delimiter='   ')
list1 = df['x'].to_list()
list2 = df['y'].to_list()

dict2 = {}
for i in list2:
    dict2[i] = dict2.get(i, 0) + 1

similarity_score = 0
for i in list1:
    if i in dict2:
        similarity_score += i * dict2[i]

print(similarity_score)
