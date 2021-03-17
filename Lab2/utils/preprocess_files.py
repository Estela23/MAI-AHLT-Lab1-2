import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


def preprocess(data, model):
    """
    Args:
        data: data.feat read by lines and converted to a list
        model: "DT" or "CRF" depending on the model we want to use

    Returns: X_sentences: list of lists of lists with the sorted features of the tokens in the original file
             Y_sentences: list of lists with the "real" tags of the words of each sentence

    """

    X_tokens = [data[i][5:] for i in range(len(data))]
    Y_tokens = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]

    aux_y = []
    Y_sentences = []
    for element in Y_tokens:
        if element != '':
            aux_y.append(element)
        elif len(aux_y) > 0:
            Y_sentences.append(aux_y)
            aux_y = []

    if model == "DT":
        features = ["Feature " + str(i + 1) for i in range(len(X_tokens[0]))]
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

    elif model == "CRF":
        aux_x = []
        X_sentences = []
        for element in X_tokens:
            if len(element) > 1:
                aux_x.append(element)
            elif len(aux_x) > 0:
                X_sentences.append(aux_x)
                aux_x = []

    return X_sentences, Y_sentences
