import pycrfsuite
from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
from eval import evaluator
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


def output_entities(sid, tokens, tags):
    beginningbegined = False
    for token in range(len(tokens)):
        if(tags[token]) == "O":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined=False
                print(
                    sid + "|" + tokens[token][1] + "-" + tokens[token][2] + "|" + tokens[token][0] + "|" + tags[token],
                    file=output)
            else:
                print(sid + "|" + tokens[token][1]+"-" + tokens[token][2]+"|" + tokens[token][0] + "|" + tags[token], file=output)
        elif (tags[token]) == "B-group":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined=False
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "group"
                beginningbegined = True
        elif (tags[token]) == "I-group":
            if beginningbegined and typeofword == "group":
                secondoffset = tokens[token][2]
                theString = theString + " " + tokens[token][0]
            elif beginningbegined and typeofword != "group":
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "group"
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "group"
                beginningbegined = True
        elif (tags[token]) == "B-drug":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = False
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword="drug"
                beginningbegined = True
        elif (tags[token]) == "I-drug":
            if beginningbegined and typeofword == "drug":
                secondoffset = tokens[token][2]
                theString = theString + " " + tokens[token][0]
            elif beginningbegined and typeofword != "drug":
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "drug"
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "drug"
                beginningbegined = True
        elif (tags[token]) == "B-brand":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = False
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "brand"
                beginningbegined = True
        elif (tags[token]) == "I-brand":
            if beginningbegined and typeofword == "brand":
                secondoffset = tokens[token][2]
                theString = theString + " " + tokens[token][0]
            elif beginningbegined and typeofword != "brand":
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "brand"
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "brand"
                beginningbegined = True


j = 0
k = 0

with open(filetowrite, 'w') as output:
    for i in range(len(Y)):
        if i+k < len(Y):
            if len(Y[i+k]) == 0:
                condition = True
                while condition:
                    k = k+1
                    if len(Y[i+k])>0:
                        condition=False

            output_entities(SID[j], tokens[j], Y[i+k])
            j = j + 1

    # evaluator.evaluate("NER", "../data/devel", output)



'''def bio_classification_report(y_true, y_pred):
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
print(bio_classification_report(Y, y_pred))'''