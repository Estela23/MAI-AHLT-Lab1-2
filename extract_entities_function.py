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
    HSDB = file.readlines()
    HSDB = [x[:-2].lower() for x in HSDB]
    # TODO: Supongo que para el HSDB deberíamos tener en cuenta las mayúsculas y eso
    file2 = open("resources/DrugBank.txt", "r")
    DrugBank = file2.read()
    DrugBank = DrugBank.split("\n")
    DrugBank = [x.lower() for x in DrugBank]
    drugs=[]
    brands=[]
    groups=[]
    number_drugs=0
    actual_drug=""
    starting_character=0
    ending_character=0
    for line in DrugBank:
        drugorbrand=line.split("|")
        if(len(drugorbrand)>1):
            if drugorbrand[1]=="drug":
                drugs.append(drugorbrand[0])
            elif drugorbrand[1]=="brand":
                brands.append(drugorbrand[0])
            elif drugorbrand[1]=="group":
                groups.append(drugorbrand[0])


    listofentities = []
    for i in s:
        if i[0].isupper():
            if number_drugs == 0:
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "brand"}
                listofentities.append(thisdict)
            elif number_drugs > 0:
                thisdict = {"name": actual_drug, "offset": starting_character + "-" + ending_character, "type": "drug"}
                listofentities.append(thisdict)
                number_drugs = 0
                actual_drug = ""
                starting_character=0
                ending_character=0
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "brand"}
                listofentities.append(thisdict)
        elif i[0][-4:] in suffixes_4:
            if number_drugs == 0:
                actual_drug = actual_drug + i[0]
                number_drugs = number_drugs + 1
                starting_character=str(i[1])
                ending_character=str(i[2])
            elif number_drugs > 0:
                actual_drug = actual_drug + " " + i[0]
                number_drugs = number_drugs + 1
                ending_character = str(i[2])
        elif i[0][-5:] in suffixes_5:
            if number_drugs == 0:
                actual_drug = actual_drug + i[0]
                number_drugs = number_drugs + 1
                starting_character = str(i[1])
                ending_character = str(i[2])
            elif number_drugs > 0:
                actual_drug = actual_drug + " " + i[0]
                number_drugs = number_drugs + 1
                ending_character = str(i[2])
        elif i[0][-6:] in suffixes_6:
            if number_drugs == 0:
                actual_drug = actual_drug + i[0]
                number_drugs = number_drugs + 1
                starting_character = str(i[1])
                ending_character = str(i[2])
            elif number_drugs > 0:
                actual_drug = actual_drug + " " + i[0]
                number_drugs = number_drugs + 1
                ending_character = str(i[2])
        elif i[0][:4] in prefixes_4:
            if number_drugs == 0:
                actual_drug = actual_drug + i[0]
                number_drugs = number_drugs + 1
                starting_character = str(i[1])
                ending_character = str(i[2])
            elif number_drugs > 0:
                actual_drug = actual_drug + " " + i[0]
                number_drugs = number_drugs + 1
                ending_character = str(i[2])
        elif (i[0].lower() in HSDB):
            if number_drugs == 0:
                actual_drug = actual_drug + i[0]
                number_drugs = number_drugs + 1
                starting_character = str(i[1])
                ending_character = str(i[2])
            elif number_drugs > 0:
                actual_drug = actual_drug + " " + i[0]
                number_drugs = number_drugs + 1
                ending_character = str(i[2])
        elif i[0].lower() in drugs:
            if number_drugs == 0:
                actual_drug = actual_drug + i[0]
                number_drugs = number_drugs + 1
                starting_character = str(i[1])
                ending_character = str(i[2])
            elif number_drugs > 0:
                actual_drug = actual_drug + " " + i[0]
                number_drugs = number_drugs + 1
                ending_character = str(i[2])
        elif i[0].lower() in brands:
            if number_drugs == 0:
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "brand"}
                listofentities.append(thisdict)
            elif number_drugs > 0:
                thisdict = {"name": actual_drug, "offset": starting_character + "-" + ending_character, "type": "drug"}
                listofentities.append(thisdict)
                number_drugs = 0
                actual_drug = ""
                starting_character=0
                ending_character=0
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "brand"}
                listofentities.append(thisdict)
        elif i[0].lower() in groups:
            if number_drugs == 0:
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "group"}
                listofentities.append(thisdict)
            elif number_drugs > 0:
                thisdict = {"name": actual_drug, "offset": starting_character + "-" + ending_character, "type": "drug"}
                listofentities.append(thisdict)
                number_drugs = 0
                actual_drug = ""
                starting_character=0
                ending_character=0
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "group"}
                listofentities.append(thisdict)
        elif any(map(str.isdigit, i[0])):
            if number_drugs == 0:
                thisdict={"name": i[0], "offset": str(i[1])+ "-" +str(i[2]), "type": "drug_n"}
                listofentities.append(thisdict)
            elif number_drugs > 0:
                thisdict = {"name": actual_drug, "offset": starting_character + "-" + ending_character, "type": "drug"}
                listofentities.append(thisdict)
                number_drugs = 0
                actual_drug = ""
                starting_character=0
                ending_character=0
                thisdict = {"name": i[0], "offset": str(i[1]) + "-" + str(i[2]), "type": "drug_n"}
                listofentities.append(thisdict)
        else:
            if number_drugs>0:
                thisdict = {"name": actual_drug, "offset": starting_character + "-" + ending_character, "type": "drug"}
                listofentities.append(thisdict)
                number_drugs=0
                actual_drug=""
                starting_character = 0
                ending_character = 0
    return listofentities
