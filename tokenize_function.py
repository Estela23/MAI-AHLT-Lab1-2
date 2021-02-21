from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer as twt


def tokenize(s):
    """
    Task:
    Given a sentence, calls nltk.tokenize to split it in
    tokens, and adds to each token its start/end offset
    in the original sentence.
    Input:
    s: string containing the text for one sentence
    Output:
    Returns a list of tuples (word, offsetFrom, offsetTo)
    Example:
    tokenize("Ascorbic acid, aspirin, and the common cold.")
    [("Ascorbic", 0, 7), ("acid", 9, 12) , (",", 13, 13),
    ("aspirin", 15, 21), (",", 22, 22), ("and", 24, 26),
    ("the", 28, 30), ("common", 32, 37), ("cold", 39, 42),
    (".", 43, 43)]
    """

    # List of the words of the sentence s
    list_tokens = word_tokenize(s)

    # span_tokenize identifies the tokens using integer offsets: (start_i, end_i)
    list_offset = list(twt().span_tokenize(s))
    real_offset = [(x, y - 1) for (x, y) in list_offset]

    # Create the list of tuples of each token and its start/end offset
    tokens = [(list_tokens[i], real_offset[i][0], real_offset[i][1]) for i in range(len(list_tokens))]

    return tokens
