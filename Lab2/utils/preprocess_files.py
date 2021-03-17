import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder


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

    if model == "DT":
        features = ["Feature " + str(i + 1) for i in range(len(X_tokens[0]))]
        df_prov = pd.DataFrame(X_tokens, columns=features)

        blank_indexes = [i for i in range(df_prov.shape[0]) if df_prov.iloc[i][0] is None]

        Y_sentences = [Y_tokens[i] for i in range(len(Y_tokens)) if i not in blank_indexes]

        df = df_prov.copy()
        df = df.drop(df.index[blank_indexes])

        encoder = OrdinalEncoder()
        encoded_df = encoder.fit_transform(df)
        X_sentences = encoded_df

        """
        df = df_prov.copy()
        df.drop(df.index[blank_indexes])
        
        encoder = LabelEncoder()
        encoded_columns = []
        for column in range(df.shape[1]):
            encoded_column = encoder.fit_transform(df[:, column])
            encoded_columns.append(encoded_column)
        encoded_df = pd.DataFrame(encoded_columns)"""

        """aux_x = []
        X_sentences = []
        for row_idx in range(encoded_df.shape[0]):
            if row_idx not in blank_indexes:
                aux_x.append(list(encoded_df[row_idx]))
            elif len(aux_x) > 0:
                X_sentences.append(aux_x)
                aux_x = []"""

    elif model == "CRF":
        aux_y = []
        Y_sentences = []
        for element in Y_tokens:
            if element != '':
                aux_y.append(element)
            elif len(aux_y) > 0:
                Y_sentences.append(aux_y)
                aux_y = []

        aux_x = []
        X_sentences = []
        for element in X_tokens:
            if len(element) > 1:
                aux_x.append(element)
            elif len(aux_x) > 0:
                X_sentences.append(aux_x)
                aux_x = []

    return X_sentences, Y_sentences


def create_SID_tokens(data):
    # Creating the list of the Sentence Identifications for the output file
    SID = []
    for i in range(len(data)):
        if (data[i][0] not in SID) and len(data[i][0]) > 0:
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

        if (len(data[i][0])) > 1:
            token_to_attach.append((data[i][1], data[i][2], data[i][3]))
    tokens.append(token_to_attach)

    return SID, tokens
