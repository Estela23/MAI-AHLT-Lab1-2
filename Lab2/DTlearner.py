import pycrfsuite
import sys
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
from sklearn import tree
import pickle


training_model = sys.argv[1]      # 'conll2002-esp.crfsuite'
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
    else:
        Y_sentences.append(aux_y)
        aux_y = []

features = ["feat1", "feat2", "feat3", "feat4", "feat5", "feat6", "feat7", "feat8", "feat9", "feat10"]
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
    else:
        X_sentences.append(aux_x)
        aux_x = []


"""
def learnerDT(X, Y):
    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X, Y):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier
        'feature.possible_transitions': True
    })
    trainer.train(training_model)
    return 0
"""


""""""
# TODO: checkear que esto lo hace por frases, porque yo creo que hace falta un zip(X, Y) como el de arriba.... :D
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X_sentences, Y_sentences)

# save the model to disk
file_classifier = 'decision_tree_classifier.sav'
pickle.dump(classifier, open(file_classifier, 'wb'))

""""""

# learnerDT(X_sentences, Y_sentences)
