import string
from nltk.stem import WordNetLemmatizer


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
    lemmatizer = WordNetLemmatizer()

    listFeatureVectors = []
    for i in range(len(s)):
        FeatureVector = []
        FeatureVector.append("form=" + s[i][0])
        FeatureVector.append("suf5=" + s[i][0][-5:])
        #FeatureVector.append("suf6=" + s[i][0][-6:])
        FeatureVector.append("pref4=" + s[i][0][:4])
        #FeatureVector.append("lemma=" + lemmatizer.lemmatize(s[i][0]))

        if s[i][0][-1] == "s":
            FeatureVector.append("endsWithS")
        else:
            FeatureVector.append("None")

        '''if s[i][0].isupper():
            FeatureVector.append("isCapitalized")
        else:
            FeatureVector.append("None")'''
        if s[i][1] == 0:
            FeatureVector.append("prev=_BoS_")
        else:
            FeatureVector.append("prev=" + previous)
        previous = s[i][0]
        '''if i<(len(s)-1):
            FeatureVector.append("next="+s[i+1][0])
            FeatureVector.append("nextsuf5=" + s[i+1][0][-5:])
            #FeatureVector.append("nextpref4=" + s[i+1][0][:4])
        else:
            FeatureVector.append("next=_EoS_")
            FeatureVector.append("None")
            #FeatureVector.append("None")
'''
        '''if s[i][0] in string.punctuation:
            FeatureVector.append("punct")
        else:
            FeatureVector.append("None")
        '''
        '''if any(map(str.isdigit, s[i][0])):
            FeatureVector.append("hasDigits")
        else:
            FeatureVector.append("None")
'''
        listFeatureVectors.append(FeatureVector)
    return listFeatureVectors
