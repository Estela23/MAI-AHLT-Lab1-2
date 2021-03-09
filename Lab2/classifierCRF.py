import pycrfsuite
from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer

file = open("test.feat", "r")
data_init = file.readlines()
data = [x[:-2].split("\t") for x in data_init]

X = [data[i][5:] for i in range(len(data)) if len(data[i]) > 4]
Y_provisional = [data[j][4] for j in range(len(data)) if len(data[j]) > 4]
Y = []
for i in range(len(Y_provisional)):
    appender = [Y_provisional[i] for j in range(len(X[i]))]
    Y.append(appender)


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
