import pycrfsuite
from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer

file = open("devel.feat", "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_provisional = [data[i][5:] for i in range(len(data))]
# X = [data[i][5:] for i in range(len(data)) if len(data[i]) > 4]
Y_provisional = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]
# Y_provisional = [data[j][4] for j in range(len(data)) if len(data[j]) > 4]
# Y=[Y_provisional[i] for i in range(len(Y_provisional)) for j in range(len(X_provisional[i]))]
listaauxiliar = []
X = []
for i in range(len(X_provisional)):
    if len(X_provisional) > i:
        if len(X_provisional[i]) > 1:
            listaauxiliar.extend(X_provisional[i])
            # listaauxiliar2.extend([Y_provisional[i] for j in range(len(X_provisional[i]))])
        else:
            X.append(listaauxiliar)
            listaauxiliar=[]
            '''Y.append(listaauxiliar2)
            listaauxiliar = []'''
Y = []
listaauxiliar = []
for i in range(len(Y_provisional)):
    if(Y_provisional[i]) != '':
        listaauxiliar.extend([Y_provisional[i] for j in range(len(X_provisional[i]))])
    else:
        Y.append(listaauxiliar)
        listaauxiliar = []


tagger = pycrfsuite.Tagger()
tagger.open('conll2002-esp.crfsuite')


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


y_pred = [tagger.tag(xseq) for xseq in X]
print(bio_classification_report(Y, y_pred))
