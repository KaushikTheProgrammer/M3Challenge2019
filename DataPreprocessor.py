import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/NSDUH_2017.csv")
ages = df.to_numpy()

#2505
print(ages.shape[0])

for i in range(ages.shape[0]):
    age = ages[i][2504]
    num = age[:2]
    if int(num) < 17 or int(num) > 19:
        np.delete(ages, i, axis=0)

df.to_csv("Datasets/NSDUH_2017.csv")


