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

    suffixes_4 = ["afil", "cort", "pril", "trel"]
    suffixes_5 = ["amine", "asone", "azine", "azole", "bicin", "bital", "caine", "fenac", "idine", "iptan", "iptin", "isone",
                  "micin", "mycin", "nacin", "olone", "onide", "parin", "plase", "tinib", "terol", "urane", "zepam",
                  "zolam", "zosin"]
    suffixes_6 = ["azepam", "cillin", "clovir", "curium", "dazole", "dipine", "iazide", "iclyne", "igmine", "kinase",
                  "lamide", "nazole", "oxacin", "profen", "ridone", "ronate", "ronium", "ropium", "sartan", "semide",
                  "setron", "sonide", "statin", "tadine", "tyline", "ustine", "vudine", "ylline", "zodone"]

    prefixes_4 = ["ceph", "pred", "sulf", "tret"]

    file = open("resources/HSDB.txt", "r")
    HSDB = file.read()
    HSDB = HSDB.split("\n")
    # TODO: Supongo que para el HSDB deberíamos tener en cuenta las mayúsculas y eso

    listofentities = []
    for i in s:
        if i[0].isupper():
            thisdict = {"name": i[0], "offset": str(i[1]) + " -" + str(i[2]), "type": "brand"}
            listofentities.append(thisdict)
        elif i[0][-4:] in suffixes_4:
            thisdict = {"name": i[0], "offset": str(i[1]) + " -" + str(i[2]), "type": "drug"}
            listofentities.append(thisdict)
        elif i[0][-5:] in suffixes_5:
            thisdict = {"name": i[0], "offset": str(i[1]) + " -" + str(i[2]), "type": "drug"}
            listofentities.append(thisdict)
        elif i[0][-6:] in suffixes_6:
            thisdict = {"name": i[0], "offset": str(i[1]) + " -" + str(i[2]), "type": "drug"}
            listofentities.append(thisdict)
        elif i[0][:4] in prefixes_4:
            thisdict = {"name": i[0], "offset": str(i[1]) + " -" + str(i[2]), "type": "drug"}
            listofentities.append(thisdict)
        elif i[0] in HSDB:
            thisdict = {"name": i[0], "offset": str(i[1]) + " -" + str(i[2]), "type": "drug"}
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
            i = 0
    return listofentities
