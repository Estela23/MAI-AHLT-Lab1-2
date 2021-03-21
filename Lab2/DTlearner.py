import sys
from sklearn import tree
import pickle
from utils.preprocess_files import preprocess
from matplotlib import pyplot as plt


training_model = sys.argv[1]      # trainer.dt
training_file = sys.argv[2]   # train.feat

file = open(training_file, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_sentences, Y_sentences = preprocess(data, "DT")

# Creating and training the Decision Tree model
classifier = tree.DecisionTreeClassifier()
classifier.fit(X_sentences, Y_sentences)

features = ["Feature " + str(i + 1) for i in range(X_sentences.shape[1])]

fig = plt.figure(figsize=(25, 20))
_ = tree.plot_tree(classifier, feature_names=features, class_names=classifier.classes_, filled=True)
fig.savefig("decision_tree.png")


# Save the model to disk
pickle.dump(classifier, open(training_model, 'wb'))
