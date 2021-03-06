import pycrfsuite


def learnerCRF(X, Y):
    trainer = pycrfsuite.Trainer(verbose=False)

    for xseq, yseq in zip(X, Y):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier

        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })
    trainer.train('conll2002-esp.crfsuite')
    return 0
