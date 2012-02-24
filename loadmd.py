#***************************************************************
#*                                                             *
#*           load a metadata 'release' folder                  *
#*                                                             *
#***************************************************************

import nltk
from nltk.corpus import PlaintextCorpusReader
print "*****************************************"
print "********** Meta Data Loader *************"
print "*****************************************"
print "usage..."
print "import nltk"
print "md = loadmd.Get_MD_text()"
print "  ~ or ~ "
print "cats = loadmd.Get_MD_text('kb_xml/hwxml/categories')"
print " "
print " "

def Get_MD_text(corpus_root = '/release/'):    
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    print "corpus read from " + corpus_root + " ..."
    raw = wordlists.raw()
    print "corpus rawed ..."
    tokens = nltk.word_tokenize(raw)
    print "corpus tokenized ..."
    text = nltk.Text(tokens)
    print "corpus textified ..."
    simple_md = [word.lower() for word in text if word.isalpha()]
    print "corpus lowercased and alphafied ..."
    simple_md = [word for word in simple_md if word != 'source']
    print "keyword *source* removed ..."
    print "DONE!"
    return simple_md

