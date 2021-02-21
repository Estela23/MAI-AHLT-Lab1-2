def extract_entities(s):
    """
    Task :
    Given a tokenized sentence , identify which tokens (or groups of
    consecutive tokens ) are drugs
    Input :
    s: A tokenized sentence ( list of triples (word , offsetFrom , offsetTo ) )
    Output :
    A list of entities . Each entity is a dictionary with the keys 'name ', '
    offset ', and 'type '.
    Example :
     extract_entities ([(" Ascorbic " ,0 ,7) , (" acid " ,9 ,12) , (" ," ,13 ,13) , ("
    aspirin " ,15 ,21) , (" ," ,22 ,22) , (" and " ,24 ,26) , (" the " ,28 ,30) , (" common
    " ,32 ,37) , (" cold " ,39 ,42) , ("." ,43 ,43) ])
    [{" name ":" Ascorbic acid ", " offset ":"0 -12" , " type ":" drug
    """

    suffixeslengthfive=['azole', 'idine', 'amine', 'mycin', 'tinib', 'iptin', 'asone', 'bicin']
    listofentities=[]
    file = open("resources/HSDB.txt", "r")
    HSDB=file.read()
    HSDB=HSDB.split("\n")
    for i in s:
        if(i[0].isupper()):
            thisdict={}
            thisdict["name"]=i[0]
            thisdict["offset"]=str(i[1])+" -"+str(i[2])
            thisdict["type"]="brand"
            listofentities.append(thisdict)
        elif(i[0][-5:] in ['azole', 'idine', 'amine', 'mycin', 'tinib', 'iptin', 'asone', 'bicin'] ):
            thisdict = {}
            thisdict["name"] = i[0]
            thisdict["offset"] = str(i[1]) + " -" + str(i[2])
            thisdict["type"] = "drug"
            listofentities.append(thisdict)
        elif(i[0][-8:] in ['phylline', 'thiazide'] ):
            thisdict = {}
            thisdict["name"] = i[0]
            thisdict["offset"] = str(i[1]) + " -" + str(i[2])
            thisdict["type"] = "drug"
            listofentities.append(thisdict)
        elif(i[0][:4] in ['ceph', 'pred', 'sulf', 'tret']):
            thisdict = {}
            thisdict["name"] = i[0]
            thisdict["offset"] = str(i[1]) + " -" + str(i[2])
            thisdict["type"] = "drug"
            listofentities.append(thisdict)
        elif(i[0] in HSDB):
            thisdict = {}
            thisdict["name"] = i[0]
            thisdict["offset"] = str(i[1]) + " -" + str(i[2])
            thisdict["type"] = "drug"
            listofentities.append(thisdict)
        else:
            i=0
    return listofentities
