import pycrfsuite
from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
from utils.create_output import output_entities
import sys

modeltoUse = sys.argv[1]       # 'conll2002-esp.crfsuite'
filetoclassify = sys.argv[2]
filetowrite = sys.argv[4]

file = open(filetoclassify, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_provisional = [data[i][5:] for i in range(len(data))]
Y_provisional = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]

SID = []
for i in range(len(data)):
    if(data[i][0] not in SID) and len(data[i][0]) > 0:
        SID.append(data[i][0])

tokens = []
toattachToken = []
for i in range(len(data)):
    if i == 0:
        actualSID = data[i][0]
    elif actualSID != data[i][0] and len(data[i][0]) > 1:
        tokens.append(toattachToken)
        toattachToken = []
        actualSID = data[i][0]

    if(len(data[i][0])) > 1:
        toattachToken.append((data[i][1], data[i][2], data[i][3]))
tokens.append(toattachToken)

################

toappend = []
Y = []
for element in Y_provisional:
    if element != '':
        toappend.append(element)
    else:
        Y.append(toappend)
        toappend = []
toappend = []

X = []
for element in X_provisional:
    if len(element) > 1:
        toappend.append(element)
    else:
        X.append(toappend)
        toappend = []

tagger = pycrfsuite.Tagger()
tagger.open(modeltoUse)
y_pred = [tagger.tag(xseq) for xseq in X]

######################

j = 0
k = 0

with open(filetowrite, 'w') as output:
    for i in range(len(Y)):
        if i+k < len(Y):
            if len(Y[i+k]) == 0:
                condition = True
                while condition:
                    k = k+1
                    if len(Y[i+k]) > 0:
                        condition = False

            output_entities(output, SID[j], tokens[j], Y[i+k])
            j = j + 1
