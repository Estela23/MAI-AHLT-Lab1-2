import sys
from utils.preprocess_files import preprocess, create_SID_tokens
from utils.create_output import output_entities
import pickle

model_to_use = sys.argv[1]
file_to_classify = sys.argv[2]
file_to_write = sys.argv[4]

file = open(file_to_classify, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

# Generate the list of SIDs and tokens from the data to print in the output file
SID, tokens = create_SID_tokens(data)

# Generate the data X and Y corresponding to the data we want to classify
X_sentences, Y_sentences = preprocess(data, "DT")

# Charging the model
dt_model = pickle.load(open(model_to_use, 'rb'))

# Classifying
# y_pred = [list(dt_model.predict(X_sentences[i])) for i in range(X_sentences.shape[0])]
y_pred = dt_model.predict(X_sentences)

# Rearranging y_pred
lengths = [len(tokens[i]) for i in range(len(tokens))]

predictions = []
for j in range(len(lengths)):
    aux = []
    for i in range(lengths[j]):
        aux.append(y_pred[i])
    predictions.append(aux)
    y_pred = y_pred[lengths[j]:]


# Creating the output file with the results of the predictions
j = 0
k = 0

with open(file_to_write, 'w') as output:
    for i in range(len(predictions)):
        if i+k < len(predictions):
            if len(predictions[i+k]) == 0:
                condition = True
                while condition:
                    k = k+1
                    if len(predictions[i+k]) > 0:
                        condition = False
            output_entities(output, SID[j], tokens[j], predictions[i+k])
            j = j + 1
