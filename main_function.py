
# Main function copied from the slides of the presentation
from tokenize_function import tokenize
from extract_entities_function import extract_entities
from os import listdir
from xml.dom.minidom import parse
import sys
#from eval import evaluator

datadir = sys.argv[1]
outfile = sys.argv[2]

with open(outfile, 'w') as output:
    # process each file in directory
    for f in listdir(datadir):
        # parse XML file , obtaining a DOM tree
        tree = parse(datadir + "/" + f)
        # process each sentence in the file
        sentences = tree.getElementsByTagName("sentence")
        for s in sentences:
            sid = s.attributes["id"].value  # get sentence id
            stext = s.attributes["text"].value  # get sentence text
            # tokenize text
            tokens = tokenize(stext)
            # extract entities from tokenized sentence text
            entities = extract_entities(tokens)
            # print sentence entities in format requested for evaluation
            if(len(entities)>0):
                for e in entities:
                        print(sid + "|" + e["offset"] + "|" + e["name"] + "|" + e["type"], file=output)
    # print performance score
    #evaluator.evaluate("NER", datadir, outfile)