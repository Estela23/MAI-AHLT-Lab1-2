import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier as DTC


file = open("train.feat", "r")
data_init = file.readlines()
data = [x.strip().split("\t") for x in data_init]

X_provisional = [data[i][5:] for i in range(len(data))]
Y_provisional = [data[j][4] if len(data[j]) > 4 else '' for j in range(len(data))]

listaauxiliar = []
X = []
for i in range(len(X_provisional)):
    if len(X_provisional) > i:
        if len(X_provisional[i]) > 1:
            listaauxiliar.extend(X_provisional[i])
        else:
            X.append(listaauxiliar)
            listaauxiliar = []

listaauxiliar = []
Y = []
for i in range(len(Y_provisional)):
    if(Y_provisional[i]) != '':
        listaauxiliar.extend([Y_provisional[i] for j in range(len(X_provisional[i]))])
    else:
        Y.append(listaauxiliar)
        listaauxiliar = []

df_prov = pd.DataFrame(X_provisional, columns=["feat1", "feat2", "feat3", "feat4", "feat5", "feat6", "feat7", "feat8"])
df_prov["class"] = Y_provisional
# TODO OJO! En este dataframe hay filas que son todo "None", por cuando se cambia de frase
print("finished")
