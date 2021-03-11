import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier as DTC
from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer

# ########################### LEARNING ######################
file = open("train_WO_blanks.feat", "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_provisional = [data[i][5:] for i in range(len(data))]
Y_provisional = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]

features = ["feat1", "feat2", "feat3", "feat4", "feat5", "feat6", "feat7", "feat8", "feat9", "feat10"]
df_prov = pd.DataFrame(X_provisional, columns=features)
df_prov["class"] = Y_provisional

# define ordinal encoding
encoder = OrdinalEncoder()
# transform data
df = encoder.fit_transform(df_prov)

X = df[:, :-1]
y = df[:, -1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)


# ######################### CLASSIFYING ##########################
file_dev = open("devel_WO_blanks.feat", "r")
data_init_dev = file_dev.readlines()
data_dev = [x.strip().split("\t") for x in data_init_dev]

X_provisional_dev = [data_dev[i][5:] for i in range(len(data_dev))]
Y_provisional_dev = [data_dev[j][4] if len(data_dev[j]) > 4 else '' for j in range(len(data_dev))]

features = ["feat1", "feat2", "feat3", "feat4", "feat5", "feat6", "feat7", "feat8", "feat9", "feat10"]
df_prov_dev = pd.DataFrame(X_provisional_dev, columns=features)
df_prov_dev["class"] = Y_provisional_dev

# define ordinal encoding
encoder = OrdinalEncoder()
# transform data
encoder.fit(df_prov_dev)
df_dev = encoder.transform(df_prov_dev)

X_dev = df_dev[:, :-1]
y_dev = df_dev[:, -1]


y_pred_dev = clf.predict(X_dev)

# df_pred_dev = np.concatenate((X_dev, y_pred_dev))
df_pred_dev = pd.DataFrame(X_dev)
df_pred_dev["predicted class"] = y_pred_dev

df_pred_dev = encoder.inverse_transform(df_pred_dev)
y_pred_dev = list(df_pred_dev[:, -1])


def bio_classification_report(y_true, y_pred):
    """
    Classification report for a list of BIO-encoded sequences.
    It computes token-level metrics and discards "O" labels.
    Note that it requires scikit-learn 0.15+ (or a version from github master)
    to calculate averages properly!
    """
    lb = LabelBinarizer()
    y_true_combined = lb.fit_transform(list(chain.from_iterable(y_true)))
    y_pred_combined = lb.transform(list(chain.from_iterable(y_pred)))

    tagset = set(lb.classes_) - {'O'}
    tagset = sorted(tagset, key=lambda tag: tag.split('-', 1)[::-1])
    class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}

    return classification_report(
        y_true_combined,
        y_pred_combined,
        labels=[class_indices[cls] for cls in tagset],
        target_names=tagset,
    )


# print(bio_classification_report(Y_provisional_dev, y_pred_dev))
