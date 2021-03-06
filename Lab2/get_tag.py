

def get_tag(token, gold):
    """ Task:
            Given a token and a list of ground truth entities in a sentence, decide which is the B-I-O tag for the token

        Input:
            token: A token, i.e. one triple (word, offsetFrom, offsetTo)
            gold: A list of ground truth entities, i.e. a list of triples (offsetFrom, offsetTo, type)

        Output:
            The B-I-O ground truth tag for the given token ("B-drug", "I-drug", "B-group", "I-group", "O", ...)

        Example:
            >> get_tag((" Ascorbic ", 0, 7), [(0, 12, "drug"), (15, 21, "brand")])
            B-drug
            >> get_tag ((" acid ", 9, 12), [(0, 12, "drug"), (15, 21, "brand ")])
            I-drug
            >> get_tag ((" common ", 32, 37), [(0, 12, "drug"), (15, 21, "brand")])
            O
            >> get_tag ((" aspirin ", 15, 21), [(0, 12, "drug"), (15, 21, "brand ")])
            B-brand
    """

    offset_B = [gold[i][0] for i in range(len(gold))]
    offset_L = [gold[i][1] for i in range(len(gold))]
    offset_int = [(offset_B[i], offset_L[i]) for i in range(len(gold))]

    if token[1] in offset_B:
        index = [x for x, y in enumerate(gold) if y[0] == token[1]]
        tag = "B-" + str(gold[index[0]][2])
    elif token[2] in offset_L:
        index = [x for x, y in enumerate(gold) if y[1] == token[2]]
        tag = "I-" + str(gold[index[0]][2])
    else:
        flag = 0
        for inter in offset_int:
            if token[1] > inter[0] and token[2] <= inter[1]:
                index = [x for x, y in enumerate(gold) if y[0] == inter[0]]
                tag = "I-" + str(gold[index[0]][2])
                flag = 1
        if flag == 0:
            tag = "O"
    return tag
