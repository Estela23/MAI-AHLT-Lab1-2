import string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag


def extract_features(s):
    """
    Task:Given a tokenized  sentence , return a feature  vector  for  each  token
     Input:s: A tokenized  sentence (list of  triples (word , offsetFrom , offsetTo) )
     Output:A list of  feature  vectors , one  per  token.
     Features  are  binary  and  vectors  are in  sparse  representation (i.e. onlyactive  features  are  listed)
     
     Example:
     >> extract_features ([(" Ascorbic ",0,7), ("acid ",9,12), (",",13,13),(" aspirin ",15,21), (",",22,22),
     ("and",24,26), ("the",28,30),(" common ",32,37), ("cold ",39,42), ("." ,43 ,43)])
     
     [ [ "form=Ascorbic",   "suf4=rbic", "next=acid", "prev=_BoS_", "capitalized"   ],
     [ "form=acid",   "suf4=acid", "next=,", "prev=Ascorbic" ],
     [ "form=,",   "suf4=,", "next=aspirin", "prev=acid", "punct" ],
     [ "form=aspirin",   "suf4=irin", "next=,", "prev=," ],
     ...]
     """

    suffixes_5 = ["amine", "asone", "azine", "azole", "bicin", "bital", "caine", "fenac", "idine", "iptan", "iptin",
                  "isone",
                  "micin", "mycin", "nacin", "olone", "onide", "parin", "plase", "tinib", "terol", "urane", "zepam",
                  "zolam", "zosin"]
    suffixes_6 = ["azepam", "cillin", "clovir", "curium", "dazole", "dipine", "iazide", "iclyne", "igmine", "kinase",
                  "lamide", "nazole", "oxacin", "profen", "ridone", "ronate", "ronium", "ropium", "sartan", "semide",
                  "setron", "sonide", "statin", "tadine", "tyline", "ustine", "vudine", "ylline", "zodone"]

    """file = open("../resources/HSDB.txt", "r")
    HSDB = file.readlines()
    HSDB = [x[:-2].lower() for x in HSDB]"""

    """   file2 = open("../resources/DrugBank.txt", "r")
    DrugBank = file2.read()
    DrugBank = DrugBank.split("\n")
    DrugBank = [x.lower() for x in DrugBank]

    drugs = []
    brands = []
    groups = []

    for line in DrugBank:
        drugorbrand = line.split("|")
        if len(drugorbrand) > 1:
            if drugorbrand[1] == "drug":
                drugs.append(drugorbrand[0])
            elif drugorbrand[1] == "brand":
                brands.append(drugorbrand[0])
            elif drugorbrand[1] == "group":
                groups.append(drugorbrand[0])"""


    # lemmatizer = WordNetLemmatizer()

    sentence = [s[i][0] for i in range(len(s))]
    pos_tags = [pos_tag(sentence)[i][1] for i in range(len(sentence))]

    listFeatureVectors = []
    for i in range(len(s)):
        punctuation_feature = [True for j in range(len(string.punctuation)) if string.punctuation[j] in s[i][0]]
        drug_n_feature = [True for j in range(len(s[i][0])) if
                          (s[i][0][j].isdigit() or s[i][0][j] == "-" or s[i][0][j] == ",") or s[i][0][j] == "I"]

        FeatureVector = []
        FeatureVector.append("form=" + s[i][0])
        # FeatureVector.append("suf4=" + s[i][0][-4:])
        FeatureVector.append("suf5=" + s[i][0][-5:])
        # FeatureVector.append("suf6=" + s[i][0][-6:])
        # FeatureVector.append("pref3=" + s[i][0][:3])
        # FeatureVector.append("pref4=" + s[i][0][:4])
        # FeatureVector.append("lemma=" + lemmatizer.lemmatize(s[i][0]))
        FeatureVector.append("POStag=" + pos_tags[i])

        if len(punctuation_feature) > 0:
            FeatureVector.append("hasSpecialCharacters")
        else:
            FeatureVector.append("hasNotSpecialCharacters")

        if s[i][0][-5:] in suffixes_5 or s[i][0][-6:] in suffixes_6:
            FeatureVector.append("drugSuffix")
        else:
            FeatureVector.append("notDrugSuffix")

        if s[i][0][-1] == "s":
            FeatureVector.append("endsWithS")
        else:
            FeatureVector.append("notEndwithS")

        if s[i][0].isupper():
            FeatureVector.append("isCapitalized")
        else:
            FeatureVector.append("isNotCapitalized")

        if s[i][1] == 0:
            FeatureVector.append("prev=_BoS_")
            # FeatureVector.append("None")
            FeatureVector.append("prevPOS=None")
        else:
            FeatureVector.append("prev=" + s[i - 1][0])
            # FeatureVector.append("prevsuf5=" + s[i - 1][0][-5:])
            FeatureVector.append("prevPOStag=" + pos_tags[i - 1])

        """if i == len(s)-1:
            FeatureVector.append("None")
        else:
            FeatureVector.append("nextPOS=" + pos_tags[i+1])"""

        if i > 1:
            FeatureVector.append("prev2=" + s[i - 2][0])
            # FeatureVector.append("prev2suf5=" + s[i - 1][0][-5:])
        else:
            FeatureVector.append("prev2=_BoS_")
            # FeatureVector.append("None")

        if i < (len(s) - 1):
            FeatureVector.append("next=" + s[i + 1][0])
            FeatureVector.append("nextsuf5=" + s[i + 1][0][-5:])
            # FeatureVector.append("nextpref4=" + s[i+1][0][:4])
        else:
            FeatureVector.append("next=_EoS_")
            FeatureVector.append("nextsuf5=None")
            # FeatureVector.append("None")

        if i < (len(s) - 2):
            FeatureVector.append("next2=" + s[i + 2][0])
            # FeatureVector.append("next2suf5=" + s[i + 2][0][-5:])
            # FeatureVector.append("nextpref4=" + s[i+1][0][:4])
        else:
            FeatureVector.append("next2=_EoS_")
            # FeatureVector.append("None")
            # FeatureVector.append("None")

        """if s[i][0] in string.punctuation:
            FeatureVector.append("punct")
        else:
            FeatureVector.append("None")"""

        if any(map(str.isdigit, s[i][0])):
            FeatureVector.append("hasDigits")
        else:
            FeatureVector.append("hasNotDigits")

        if len(drug_n_feature) > 0:
            FeatureVector.append("isaDrugN")
        else:
            FeatureVector.append("isNotaDrugN")

        """if s[i][0] in drugs:
            FeatureVector.append("isaDrug")
        elif s[i][0] in brands:
            FeatureVector.append("isaBrand")
        elif s[i][0] in groups:
            FeatureVector.append("isaGroups")
        else:
            FeatureVector.append("isNothing")"""
        
        """if i < len(s)-1:
            if s[i+1][0] in drugs:
                FeatureVector.append("nextisaDrug")
            elif s[i+1][0] in brands:
                FeatureVector.append("nextisaBrand")
            elif s[i+1][0] in groups:
                FeatureVector.append("nextisaGroups")
            else:
                FeatureVector.append("nextisNothing")
        else:
            FeatureVector.append("_EoS_")
        
        if i > 0:
            if s[i-1][0] in drugs:
                FeatureVector.append("previsaDrug")
            elif s[i-1][0] in brands:
                FeatureVector.append("previsaBrand")
            elif s[i-1][0] in groups:
                FeatureVector.append("previsaGroups")
            else:
                FeatureVector.append("previsNothing")
        else:
            FeatureVector.append("_BoS_")"""

        listFeatureVectors.append(FeatureVector)
    return listFeatureVectors
