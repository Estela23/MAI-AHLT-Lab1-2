def output_entities(output, sid, tokens, tags):
    beginningbegined = False
    for token in range(len(tokens)):
        if(tags[token]) == "O":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = False
                print(
                    sid + "|" + tokens[token][1] + "-" + tokens[token][2] + "|" + tokens[token][0] + "|" + tags[token],
                    file=output)
            else:
                print(sid + "|" + tokens[token][1]+"-" + tokens[token][2]+"|" + tokens[token][0] + "|" + tags[token], file=output)
        elif (tags[token]) == "B-group":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "group"
                beginningbegined = True
        elif (tags[token]) == "I-group":
            if beginningbegined and typeofword == "group":
                secondoffset = tokens[token][2]
                theString = theString + " " + tokens[token][0]
            elif beginningbegined and typeofword != "group":
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "group"
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "group"
                beginningbegined = True
        elif (tags[token]) == "B-drug":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword="drug"
                beginningbegined = True
        elif (tags[token]) == "I-drug":
            if beginningbegined and typeofword == "drug":
                secondoffset = tokens[token][2]
                theString = theString + " " + tokens[token][0]
            elif beginningbegined and typeofword != "drug":
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "drug"
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "drug"
                beginningbegined = True
        elif (tags[token]) == "B-brand":
            if beginningbegined:
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "brand"
                beginningbegined = True
        elif (tags[token]) == "I-brand":
            if beginningbegined and typeofword == "brand":
                secondoffset = tokens[token][2]
                theString = theString + " " + tokens[token][0]
            elif beginningbegined and typeofword != "brand":
                print(
                    sid + "|" + firstoffset + "-" + secondoffset + "|" + theString + "|" + typeofword,
                    file=output)
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "brand"
                beginningbegined = True
            else:
                firstoffset = tokens[token][1]
                secondoffset = tokens[token][2]
                theString = tokens[token][0]
                typeofword = "brand"
                beginningbegined = True
