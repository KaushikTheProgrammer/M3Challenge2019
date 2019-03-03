from time import time
import numpy as np

alcohol_data = np.load("alcohol_data.npy")
marijuana_data = np.load("marijuana_data.npy")
nicotine_data = np.load("nicotine_data.npy")

print(len(alcohol_data))
print(len(marijuana_data))
print(len(nicotine_data))

features = []
labels = []

for data_point in range(len(alcohol_data)):
    labels.append(alcohol_data[data_point][0])
    array_in = alcohol_data[data_point][1:]
    features.append(array_in)

np.random.shuffle(features)
np.random.shuffle(labels)

print(len(features))
print(len(labels))

features_train = features[1:1900]
features_test = features[1900:len(features)]
labels_train = features[1:1900]
labels_test = features[1900:len(labels)]


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print("training time", round(time()-t0, 3), "s")
t0 = time()
predicted_labels = clf.predict(features_test)
print("training time", round(time()-t0, 3), "s")
print(predicted_labels)
accuracy = clf.score(features_test, labels_test)
print(accuracy)
