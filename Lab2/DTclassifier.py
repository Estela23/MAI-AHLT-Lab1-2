import sys
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
import pickle

model_to_use = sys.argv[1]
file_to_classify = sys.argv[2]
file_to_write = sys.argv[4]

file = open(file_to_classify, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_tokens = [data[i][5:] for i in range(len(data))]
Y_tokens = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]

# Creating the list of the Sentence Identifications for the output file
SID = []
for i in range(len(data)):
    if(data[i][0] not in SID) and len(data[i][0]) > 0:
        SID.append(data[i][0])

# Creating the list of tokens for the output file
tokens = []
token_to_attach = []
for i in range(len(data)):
    if i == 0:
        actualSID = data[i][0]
    elif actualSID != data[i][0] and len(data[i][0]) > 1:
        tokens.append(token_to_attach)
        token_to_attach = []
        actualSID = data[i][0]

    if(len(data[i][0])) > 1:
        token_to_attach.append((data[i][1], data[i][2], data[i][3]))
tokens.append(token_to_attach)

# Creating the appropriate Y to feed the model
aux_y = []
Y_sentences = []
for element in Y_tokens:
    if element != '':
        aux_y.append(element)
    elif len(aux_y) > 0:
        Y_sentences.append(aux_y)
        aux_y = []

# Creating the appropriate X to feed the model
features = ["feat1", "feat2", "feat3", "feat4", "feat5", "feat6", "feat7", "feat8", "feat9", "feat10"]
df_prov = pd.DataFrame(X_tokens, columns=features)

blank_indexes = []
for i in range(df_prov.shape[0]):
    if df_prov.iloc[i][0] is None:
        blank_indexes.append(i)

encoder = OrdinalEncoder()
encoded_df = encoder.fit_transform(df_prov)

aux_x = []
X_sentences = []
for row_idx in range(encoded_df.shape[0]):
    if row_idx not in blank_indexes:
        aux_x.append(list(encoded_df[row_idx]))
    elif len(aux_x) > 0:
        X_sentences.append(aux_x)
        aux_x = []

# Charging the model
dt_model = pickle.load(open(model_to_use, 'rb'))

# Classifying
y_pred = [list(dt_model.predict(X_sentences[i])) for i in range(len(X_sentences))]


def output_entities(sid, tokens, tags):
    beginningbegined = False
    for token in range(len(tokens)):
        if(tags[token]) == "O":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = False
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
                beginningbegined = True
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
                beginningbegined = True
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
                beginningbegined = True
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


# Creating the output file with the results of the predictions
j = 0
k = 0

with open(file_to_write, 'w') as output:
    for i in range(len(Y_sentences)):
        if i+k < len(Y_sentences):
            if len(Y_sentences[i+k]) == 0:
                condition = True
                while condition:
                    k = k+1
                    if len(Y_sentences[i+k]) > 0:
                        condition = False
            output_entities(SID[j], tokens[j], Y_sentences[i+k])
            j = j + 1
