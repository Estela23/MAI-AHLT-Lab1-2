# Main function copied from the slides of the presentation
from tokenize_function import tokenize
from extract_entities_function import extract_entities



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
        for e in entities:
            print(sid + "|" + e["offset"] + "|" + e["text"] + "|" + e["type"], file=outf)
# print performance score
evaluator.evaluate("NER", datadir, outfile)
