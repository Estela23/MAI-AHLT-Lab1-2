'''
import pycrfsuite
import sys

modeltotrain=sys.argv[1]#'conll2002-esp.crfsuite'
filetotrainwith=sys.argv[2]

file = open(filetotrainwith, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_provisional = [data[i][5:] for i in range(len(data))]
#X = [data[i][5:] for i in range(len(data)) if len(data[i]) > 4]
Y_provisional = [data[j][4] if len(data[j])>4 else '' for j in range(len(data))]
#Y_provisional = [data[j][4] for j in range(len(data)) if len(data[j]) > 4]
#Y=[Y_provisional[i] for i in range(len(Y_provisional)) for j in range(len(X_provisional[i]))]
listaauxiliar = []
X = []
for i in range(len(X_provisional)):
    if len(X_provisional)>i:
        if len(X_provisional[i])>1:
            listaauxiliar.extend(X_provisional[i])
            #listaauxiliar2.extend([Y_provisional[i] for j in range(len(X_provisional[i]))])
        else:
            X.append(listaauxiliar)
            listaauxiliar=[]
Y = []
listaauxiliar = []
for i in range(len(Y_provisional)):
    if(Y_provisional[i])!='':
        listaauxiliar.extend([Y_provisional[i] for j in range(len(X_provisional[i]))])
    else:
        Y.append(listaauxiliar)
        listaauxiliar=[]


def learnerCRF(X, Y):
    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X, Y):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier

        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })
    trainer.train(modeltotrain)
    return 0


learnerCRF(X, Y)
'''

import pycrfsuite
import sys

modeltotrain = sys.argv[1]      # 'conll2002-esp.crfsuite'
filetotrainwith = sys.argv[2]

file = open(filetotrainwith, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_provisional = [data[i][5:] for i in range(len(data))]
Y_provisional = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]
toappend = []
Y = []
for element in Y_provisional:
    if element != '':
        toappend.append(element)
    elif len(toappend) > 0:
        Y.append(toappend)
        toappend = []
toappend = []
X = []
for element in X_provisional:
    if len(element) >= 1:
        toappend.append(element)
    elif len(toappend) > 0:
        X.append(toappend)
        toappend = []


def learnerCRF(X, Y):
    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X, Y):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier
        'feature.possible_transitions': True
    })
    trainer.train(modeltotrain)
    return 0


learnerCRF(X, Y)
