import string
from nltk import pos_tag


def extract_features(s):
    file = open("../resources/DrugBank.txt", "r")
    DrugBank = file.read()
    DrugBank = DrugBank.split("\n")
    DrugBank = [x.lower() for x in DrugBank]
    # Lists of the labeled entities found in the DrugBank file
    drugs = [line.split("|")[0] for line in DrugBank if (len(line.split("|")) > 1 and line.split("|")[1] == "drug")]
    brands = [line.split("|")[0] for line in DrugBank if (len(line.split("|")) > 1 and line.split("|")[1] == "brand")]
    groups = [line.split("|")[0] for line in DrugBank if (len(line.split("|")) > 1 and line.split("|")[1] == "group")]
    # Computing the list of POStags of the tokens in the current sentence
    sentence = [s[i][0] for i in range(len(s))]
    pos_tags = [pos_tag(sentence)[i][1] for i in range(len(sentence))]
    # After initializing as empty the list of features of a sentence, we start computing the features for each token
    listFeatureVectors = []
    for i in range(len(s)):
        # We initialize the feature vector for the current token with some basic features and keep adding features
        FeatureVector = ["Form=" + s[i][0], "Suf5=" + s[i][0][-5:], "POStag=" + pos_tags[i]]

        punctuation_feature = [True for j in range(len(string.punctuation)) if string.punctuation[j] in s[i][0]]
        if len(punctuation_feature) > 0:
            FeatureVector.append("HasSpecialCharacters")
        else:
            FeatureVector.append("hasNotSpecialCharacters")

        if s[i][0][-1] == "s":
            FeatureVector.append("EndsWithS")
        else:
            FeatureVector.append("NotEndwithS")

        if s[i][0].isupper():
            FeatureVector.append("IsCapitalized")
        else:
            FeatureVector.append("IsNotCapitalized")

        if any(map(str.isdigit, s[i][0])):
            FeatureVector.append("HasDigits")
        else:
            FeatureVector.append("HasNotDigits")

        drug_n_feature = [True for j in range(len(s[i][0])) if
                          (s[i][0][j].isdigit() or s[i][0][j] == "-" or s[i][0][j] == ",") or s[i][0][j] == "I"]
        if len(drug_n_feature) > 0:
            FeatureVector.append("IsaDrugN")
        else:
            FeatureVector.append("IsNotaDrugN")

        if s[i][1] == 0:
            FeatureVector.append("Prev=_BoS_")
            FeatureVector.append("PrevPOStag=_BoS_")
        else:
            FeatureVector.append("Prev=" + s[i - 1][0])
            FeatureVector.append("PrevPOStag=" + pos_tags[i - 1])

        if i > 1:
            FeatureVector.append("Prev2=" + s[i - 2][0])
        else:
            FeatureVector.append("Prev2=_BoS_")

        if i < (len(s) - 1):
            FeatureVector.append("Next=" + s[i + 1][0])
            FeatureVector.append("NextSuf5=" + s[i + 1][0][-5:])
        else:
            FeatureVector.append("Next=_EoS_")
            FeatureVector.append("NextSuf5=_EoS_")

        if i < (len(s) - 2):
            FeatureVector.append("Next2=" + s[i + 2][0])
        else:
            FeatureVector.append("Next2=_EoS_")

        if s[i][0] in drugs:
            FeatureVector.append("IsADrug")
        elif s[i][0] in brands:
            FeatureVector.append("IsABrand")
        elif s[i][0] in groups:
            FeatureVector.append("IsAGroup")
        else:
            FeatureVector.append("IsNothing")

        if i > 0:
            if s[i-1][0] in drugs:
                FeatureVector.append("PrevIsADrug")
            elif s[i-1][0] in brands:
                FeatureVector.append("PrevIsABrand")
            elif s[i-1][0] in groups:
                FeatureVector.append("PrevIsAGroups")
            else:
                FeatureVector.append("PrevIsNothing")
        else:
            FeatureVector.append("_BoS_")

        listFeatureVectors.append(FeatureVector)
    return listFeatureVectors
