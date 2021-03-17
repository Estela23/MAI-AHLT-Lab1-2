import pycrfsuite
import sys
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
from sklearn import tree
import pickle


training_model = sys.argv[1]      # trainer.dt
training_file = sys.argv[2]   # train.feat

file = open(training_file, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_tokens = [data[i][5:] for i in range(len(data))]
Y_tokens = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]

aux_y = []
Y_sentences = []
for element in Y_tokens:
    if element != '':
        aux_y.append(element)
    elif len(aux_y) > 0:
        Y_sentences.append(aux_y)
        aux_y = []

features = ["feat1"]
df_prov = pd.DataFrame(X_tokens, columns=features)

blank_indexes = []
for i in range(df_prov.shape[0]):
    if df_prov.iloc[i][0] is None:
        blank_indexes.append(i)

# define ordinal encoding
encoder = OrdinalEncoder()
# transform data
encoded_df = encoder.fit_transform(df_prov)

aux_x = []
X_sentences = []
for row_idx in range(encoded_df.shape[0]):
    if row_idx not in blank_indexes:
        aux_x.append(list(encoded_df[row_idx]))
    elif len(aux_x) > 0:
        X_sentences.append(aux_x)
        aux_x = []


# Creating and training the Decision Tree model
classifier = tree.DecisionTreeClassifier()
for xseq, yseq in zip(X_sentences, Y_sentences):
    classifier.fit(xseq, yseq)

# Save the model to disk
pickle.dump(classifier, open(training_model, 'wb'))
