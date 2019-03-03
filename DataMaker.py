import numpy as np


def data_generator(substance_name):
    # Iterates over the total amount of people
    # Creates males who use
    substance = []
    for true_point_male in range(max_values[substance_name]["gender"]["male"][0]):
        substance.append(["true", "male"])
    # Creates males who do not use
    for false_point_male in range(max_values[substance_name]["gender"]["male"][1]):
        substance.append(["false", "male"])
    # Creates females who use
    for true_point_female in range(max_values[substance_name]["gender"]["female"][0]):
        substance.append(["true", "female"])
    # Creates females who do not use
    for false_point_female in range(max_values[substance_name]["gender"]["female"][1]):
        substance.append(["false", "female"])

    substance_np = np.array(substance)
    np.random.shuffle(substance_np)
    substance = substance_np.tolist()

    asian_true = max_values[substance_name]["ethnicity"]["Asian"][0]
    asian_false = max_values[substance_name]["ethnicity"]["Asian"][1]
    black_true = max_values[substance_name]["ethnicity"]["Black"][0]
    black_false = max_values[substance_name]["ethnicity"]["Black"][1]
    hispanic_true = max_values[substance_name]["ethnicity"]["Hispanic"][0]
    hispanic_false = max_values[substance_name]["ethnicity"]["Hispanic"][1]
    multiple_race_true = max_values[substance_name]["ethnicity"]["Multiple Race"][0]
    multiple_race_false = max_values[substance_name]["ethnicity"]["Multiple Race"][1]

    for data_point in range(len(substance)):
        if substance[data_point][0] == "true":
            if asian_true > 0:
                substance[data_point].append("asian")
                asian_true = asian_true - 1
                continue
            if black_true > 0:
                substance[data_point].append("black")
                black_true = black_true - 1
                continue
            if hispanic_true > 0:
                substance[data_point].append("hispanic")
                hispanic_true = hispanic_true - 1
                continue
            if multiple_race_true > 0:
                substance[data_point].append("multiple_race")
                multiple_race_true = multiple_race_true - 1
                continue
            else:
                substance[data_point].append("NaN")
                continue
        else:
            if asian_false > 0:
                substance[data_point].append("asian")
                asian_false = asian_false - 1
                continue
            if black_false > 0:
                substance[data_point].append("black")
                black_false = black_false - 1
                continue
            if hispanic_false > 0:
                substance[data_point].append("hispanic")
                hispanic_false = hispanic_false - 1
                continue
            if multiple_race_false > 0:
                substance[data_point].append("multiple_race")
                multiple_race_false = multiple_race_false - 1
                continue
            else:
                substance[data_point].append("NaN")
                continue

    substance_np = np.array(substance)
    np.random.shuffle(substance_np)
    substance = substance_np.tolist()

    heterosexual_true = max_values[substance_name]["sexual orientation"]["Heterosexual"][0]
    heterosexual_false = max_values[substance_name]["sexual orientation"]["Heterosexual"][1]
    homosexual_true = max_values[substance_name]["sexual orientation"]["Homosexual"][0]
    homosexual_false = max_values[substance_name]["sexual orientation"]["Homosexual"][1]
    bisexual_true = max_values[substance_name]["sexual orientation"]["Bisexual"][0]
    bisexual_false = max_values[substance_name]["sexual orientation"]["Bisexual"][1]
    not_sure_true = max_values[substance_name]["sexual orientation"]["Not sure"][0]
    not_sure_false = max_values[substance_name]["sexual orientation"]["Not sure"][1]

    for data_point in range(len(substance)):
        if substance[data_point][0] == "true":
            if heterosexual_true > 0:
                substance[data_point].append("heterosexual")
                heterosexual_true = heterosexual_true - 1
                continue
            if homosexual_true > 0:
                substance[data_point].append("homosexual")
                homosexual_true = homosexual_true - 1
                continue
            if bisexual_true > 0:
                substance[data_point].append("bisexual")
                bisexual_true = bisexual_true - 1
                continue
            if not_sure_true > 0:
                substance[data_point].append("not_sure")
                not_sure_true = not_sure_true - 1
                continue
            else:
                substance[data_point].append("NaN")
                continue

        else:
            if heterosexual_false > 0:
                substance[data_point].append("heterosexual")
                heterosexual_false = heterosexual_false - 1
                continue
            if homosexual_false > 0:
                substance[data_point].append("homosexual")
                homosexual_false = homosexual_false - 1
                continue
            if bisexual_false > 0:
                substance[data_point].append("bisexual")
                bisexual_false = bisexual_false - 1
                continue
            if not_sure_false > 0:
                substance[data_point].append("not_sure")
                not_sure_false = not_sure_false - 1
                continue
            else:
                substance[data_point].append("NaN")
                continue

    for data_point in range(len(substance))[::-1]:
        for value in substance[data_point]:
            if value == "NaN":
                substance.pop(data_point)
                break

    substance_np = np.array(substance)
    np.random.shuffle(substance_np)
    substance = substance_np.tolist()

    return substance


max_values = {"Alcohol":
                  {"gender": {"total": [.2977, 12984],
                              "male": [.2756, 6172],
                              "female": [.3184, 6708]
                              },
                   "ethnicity": {"Asian": [.1217, 599],
                                 "Black": [.2080, 2367],
                                 "Hispanic": [.3134, 3111],
                                 "White": [.3239, 5690],
                                 "Multiple Race": [.3268, 743]
                                 },
                   "sexual orientation": {"Heterosexual": [0.2973, 10695],
                                          "Homosexual": [0.3370, 295],
                                          "Bisexual": [.3841, 975],
                                          "Not sure": [.2152, 523]
                                          }
                   },
              "Marijuana":
                  {"gender": {"total": [.1980, 14386],
                              "male": [.1996, 6880],
                              "female": [.1958, 7396]
                              },
                   "ethnicity": {"Asian": [.0730, 634],
                                 "Black": [.2531, 2666],
                                 "Hispanic": [.2345, 3548],
                                 "White": [.1766, 6190],
                                 "Multiple Race": [.2032, 810]
                                 },
                   "sexual orientation": {"Heterosexual": [0.1912, 11864],
                                          "Homosexual": [0.3000, 331],
                                          "Bisexual": [.3081, 1101],
                                          "Not sure": [.1892, 578]
                                          }
                   },
              "Nicotine":
                  {"gender": {"total": [.1949, 12884],
                              "male": [.2339, 6174],
                              "female": [.1559, 6598]
                              },
                   "ethnicity": {"Asian": [.0554, 590],
                                 "Black": [.1488, 2463],
                                 "Hispanic": [.1661, 3070],
                                 "White": [.2242, 5537],
                                 "Multiple Race": [.1998, 720]
                                 },
                   "sexual orientation": {"Heterosexual": [0.1920, 10519],
                                          "Homosexual": [0.2529, 317],
                                          "Bisexual": [.2778, 983],
                                          "Not sure": [.1871, 526]
                                          }
                   },
              }

population_size = 3300
constant = 0
# Adjusts population sizes in max_values data structure
# Iterates over substances
for substance in max_values:
    # Iterates over features in substances
    for feature in max_values.get(substance):
        # Iterates through categories in features
        for category in max_values.get(substance).get(feature):
            # Sets a constant such that any population number * constant <= population_size using "total" category
            if category == "total":
                current_data = max_values.get(substance).get(feature).get("total")
                constant = population_size / (current_data[1] / current_data[0])
            current_data = max_values.get(substance).get(feature).get(category)
            new_data = [0, 0]
            new_data[0] = int(current_data[1] * constant)
            new_data[1] = int(((current_data[1] / current_data[0]) * constant) - new_data[0])
            max_values[substance][feature][category] = new_data

alcohol_data = np.array(data_generator("Alcohol"))
marijuana_data = np.array(data_generator("Marijuana"))
nicotine_data = np.array(data_generator("Nicotine"))

print(len(alcohol_data))
print(len(marijuana_data))
print(len(nicotine_data))

np.save("alcohol_data", alcohol_data)
np.save("marijuana_data", marijuana_data)
np.save("nicotine_data", nicotine_data)

alcohol_data1 = np.load("alcohol_data.npy")
marijuana_data1 = np.load("marijuana_data.npy")
nicotine_data1 = np.load("nicotine_data.npy")

print(len(alcohol_data1))
print(len(marijuana_data1))
print(len(nicotine_data1))
