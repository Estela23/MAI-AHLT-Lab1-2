import pycrfsuite
from utils.preprocess_files import preprocess, create_SID_tokens
from utils.create_output import output_entities
import sys

model_to_use = sys.argv[1]       # 'conll2002-esp.crfsuite'
file_to_classify = sys.argv[2]
file_to_write = sys.argv[4]

file = open(file_to_classify, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

# Generate the list of SIDs and tokens from the data to print in the output file
SID, tokens = create_SID_tokens(data)

# Generate the data X and Y corresponding to the data we want to classify
X_sentences, Y_sentences = preprocess(data, "CRF")


tagger = pycrfsuite.Tagger()
tagger.open(model_to_use)
y_pred = [tagger.tag(xseq) for xseq in X_sentences]


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

            output_entities(output, SID[j], tokens[j], y_pred[i+k])
            j = j + 1
