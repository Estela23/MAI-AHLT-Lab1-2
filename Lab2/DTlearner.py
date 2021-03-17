import sys
from sklearn import tree
import pickle
from utils.preprocess_files import preprocess


training_model = sys.argv[1]      # trainer.dt
training_file = sys.argv[2]   # train.feat

file = open(training_file, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_sentences, Y_sentences = preprocess(data, "DT")

# Creating and training the Decision Tree model
classifier = tree.DecisionTreeClassifier()
for xseq, yseq in zip(X_sentences, Y_sentences):
    classifier.fit(xseq, yseq)

# Save the model to disk
pickle.dump(classifier, open(training_model, 'wb'))
