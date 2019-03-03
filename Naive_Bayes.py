import numpy as np
from sklearn.naive_bayes import BernoulliNB

alcohol_data = np.load("alcohol_data.npy")
marijuana_data = np.load("marijuana_data.npy")
nicotine_data = np.load("nicotine_data.npy")

# Data preprocessing for alcohol
features = []
labels = []
blank = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for data_point in range(len(alcohol_data)):
    if alcohol_data[data_point][0] == "true":
        labels.append(1)
    else:
        labels.append(0)
    array_in = alcohol_data[data_point][1:]
    for value in range(len(array_in)):
        string_value = array_in[value]
        if string_value == "male":
            blank[0] = 1
        if string_value == "female":
            blank[2] = 1
        if string_value == "asian":
            blank[3] = 1
        if string_value == "hispanic":
            blank[4] = 1
        if string_value == "multiple_race":
            blank[5] = 1
        if string_value == "homosexual":
            blank[6] = 1
        if string_value == "heterosexual":
            blank[7] = 1
        if string_value == "homosexual":
            blank[8] = 1
        if string_value == "bisexual":
            blank[9] = 1
        if string_value == "not_sure":
            blank[10] = 1
    array_in = blank
    features.append(array_in)

temp = []
temp_features = []
for feature in range(len(features[0])):
    for data_point in range(len(features)):
        temp.append(features[data_point][feature])
    temp_features.append(temp)
    temp = []
features = temp_features

np.random.shuffle(features)
np.random.shuffle(labels)

print(np.array(features).shape)
print(np.array(labels).shape)

features_train = features[1:1900]
features_test = features[1900:len(features)]
labels_train = features[1:1900]
labels_test = features[1900:len(labels)]

# Runs classifier on alcohol data
clf_alcohol = BernoulliNB()
clf_alcohol.fit(features_train, labels_train)
predicted_labels = clf_alcohol.predict(features_test)
print(predicted_labels)
alcohol_accuracy = clf_alcohol.score(features_test, labels_test)

# Data preprocessing for marijuana
features = []
labels = []
blank = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for data_point in range(len(marijuana_data)):
    if marijuana_data[data_point][0] == "true":
        labels.append(1)
    else:
        labels.append(0)
    array_in = marijuana_data[data_point][1:]
    for value in range(len(array_in)):
        string_value = array_in[value]
        if string_value == "male":
            blank[0] = 1
        if string_value == "female":
            blank[2] = 1
        if string_value == "asian":
            blank[3] = 1
        if string_value == "hispanic":
            blank[4] = 1
        if string_value == "multiple_race":
            blank[5] = 1
        if string_value == "homosexual":
            blank[6] = 1
        if string_value == "heterosexual":
            blank[7] = 1
        if string_value == "homosexual":
            blank[8] = 1
        if string_value == "bisexual":
            blank[9] = 1
        if string_value == "not_sure":
            blank[10] = 1
    array_in = blank
    features.append(array_in)

temp = []
temp_features = []
for feature in range(len(features[0])):
    for data_point in range(len(features)):
        temp.append(features[data_point][feature])
    temp_features.append(temp)
    temp = []
features = temp_features

np.random.shuffle(features)
np.random.shuffle(labels)

print(np.array(features).shape)
print(np.array(labels).shape)

features_train = features[1:1000]
features_test = features[1000:len(features)]
labels_train = features[1:1000]
labels_test = features[1000:len(labels)]

# Runs classifier on marijuana data
clf_marijuana = BernoulliNB()
clf_marijuana.fit(features_train, labels_train)
predicted_labels = clf_marijuana.predict(features_test)
print(predicted_labels)
marijuana_accuracy = clf_marijuana.score(features_test, labels_test)

# Data preprocessing for Nicotine
features = []
labels = []
blank = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for data_point in range(len(nicotine_data)):
    if nicotine_data[data_point][0] == "true":
        labels.append(1)
    else:
        labels.append(0)
    array_in = nicotine_data[data_point][1:]
    for value in range(len(array_in)):
        string_value = array_in[value]
        if string_value == "male":
            blank[0] = 1
        if string_value == "female":
            blank[2] = 1
        if string_value == "asian":
            blank[3] = 1
        if string_value == "hispanic":
            blank[4] = 1
        if string_value == "multiple_race":
            blank[5] = 1
        if string_value == "homosexual":
            blank[6] = 1
        if string_value == "heterosexual":
            blank[7] = 1
        if string_value == "homosexual":
            blank[8] = 1
        if string_value == "bisexual":
            blank[9] = 1
        if string_value == "not_sure":
            blank[10] = 1
    array_in = blank
    features.append(array_in)

temp = []
temp_features = []
for feature in range(len(features[0])):
    for data_point in range(len(features)):
        temp.append(features[data_point][feature])
    temp_features.append(temp)
    temp = []
features = temp_features

np.random.shuffle(features)
np.random.shuffle(labels)

print(np.array(features).shape)
print(np.array(labels).shape)

features_train = features[1:1000]
features_test = features[1000:len(features)]
labels_train = features[1:1000]
labels_test = features[1000:len(labels)]

# Runs classifier on nicotine data
clf_nicotine = BernoulliNB()
clf_nicotine.fit(features_train, labels_train)
predicted_labels = clf_nicotine.predict(features_test)
print(predicted_labels)
nicotine_accuracy = clf_nicotine.score(features_test, labels_test)

print("Alcohol accuracy" + alcohol_accuracy)
print("Marijuana accuracy" + marijuana_accuracy)
print("Nicotine accuracy" + nicotine_accuracy)
