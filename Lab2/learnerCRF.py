import pycrfsuite

file = open("devel.feat", "r")
data_init = file.readlines()
data = [x[:-2].split("\t") for x in data_init]

X = [data[i][5:] for i in range(len(data)) if len(data[i]) > 4]
Y_provisional = [data[j][4] for j in range(len(data)) if len(data[j]) > 4]
Y = []
for i in range(len(Y_provisional)):
    appender = [Y_provisional[i] for j in range(len(X[i]))]
    Y.append(appender)


def learnerCRF(X, Y):
    trainer = pycrfsuite.Trainer(verbose=False)
    j=0
    for xseq, yseq in zip(X, Y):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier

        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })
    trainer.train('conll2002-esp.crfsuite')
    return 0


learnerCRF(X, Y)
