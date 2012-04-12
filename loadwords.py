#***************************************************************
#*                                                             *
#*                  load a folder of content                   *
#*                                                             *
#***************************************************************

import nltk
#from nltk.corpus import PlaintextCorpusReader
from nltk.corpus.reader import XMLCorpusReader 
print "*****************************************"
print "********** Content Loader *************"
print "*****************************************"
print "usage..."
print "import nltk"
print "md = loadcontent.Get_text()"
print "  ~ or ~ "
print "cats = loadcontent.Get_text('kb_xml/hwxml/categories')"
print " "
print " "

def Get_text(corpus_root = '/release/', file_IDs = '.*'):    
    #wordlists = PlaintextCorpusReader(corpus_root, '.*')
    wordlists = XMLCorpusReader(corpus_root, file_IDs)
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

