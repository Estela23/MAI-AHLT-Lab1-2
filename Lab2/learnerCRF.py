import pycrfsuite
import sys
from utils.preprocess_files import preprocess

model_to_train = sys.argv[1]      # 'conll2002-esp.crfsuite'
training_file = sys.argv[2]

file = open(training_file, "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_sentences, Y_sentences = preprocess(data, "CRF")


def learnerCRF(X, Y):
    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X, Y):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 100,  # stop earlier
        'feature.possible_transitions': True  # include transitions that are possible, but not observed
    })
    trainer.train(model_to_train)
    return 0


learnerCRF(X_sentences, Y_sentences)
