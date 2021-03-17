import sys
from utils.preprocess_files import preprocess
from utils.create_output import output_entities
import pickle

model_to_use = sys.argv[1]
file_to_classify = sys.argv[2]
file_to_write = sys.argv[4]

file = open(file_to_classify, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

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


X_sentences, Y_sentences = preprocess(data, "DT")

# Charging the model
dt_model = pickle.load(open(model_to_use, 'rb'))

# Classifying
y_pred = [list(dt_model.predict(X_sentences[i])) for i in range(len(X_sentences))]


# Creating the output file with the results of the predictions
j = 0
k = 0

with open(file_to_write, 'w') as output:
    for i in range(len(y_pred)):
        if i+k < len(y_pred):
            if len(y_pred[i+k]) == 0:
                condition = True
                while condition:
                    k = k+1
                    if len(y_pred[i+k]) > 0:
                        condition = False
            output_entities(SID[j], tokens[j], y_pred[i+k])
            j = j + 1
