import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/NSDUH_MODIFIED_2017.csv")



# ages = df.to_numpy()
#
# np.random.shuffle(ages)
# #2505
# print("starting loop")
#
# new_ages = np.copy(ages[:3000])
#
# for i in range(new_ages.shape[0]):
#     print(new_ages[i])
#     age = new_ages[i][2504]
#     num = age[:2]
#     if int(num) < 17 or int(num) > 19:
#         np.delete(new_ages, i, axis=0)
# df = pd.DataFrame(new_ages)
# df.to_csv("Datasets/NSDUH_MODIFIED_2017.csv")

