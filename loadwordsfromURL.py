#***************************************************************
#*                                                             *
#*                  load a URL of XML                          *
#*                                                             *
#***************************************************************
import urllib
import nltk
#import xml
import xml.dom.minidom

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


def get_term_list(hwid = 'abk0887'):    
    f = urllib.urlopen('http://rd-preview-ws01/taxonomymetadataservice/hw/' + hwid + '?stack=approved')
    s = f.read()
    f.close()
    daXML = xml.dom.minidom.parseString(s)
    sb = daXML.getElementsByTagName('SearchBuckets')
    do = sb.item(0) #this should be the "SearchBuckets" element
    term_list = []
    for da_e in do.childNodes:
        for da_dos in da_e.childNodes:
            if da_dos.hasChildNodes:
                for da_du in da_dos.childNodes:
                    if da_du.nodeType == da_du.ELEMENT_NODE:
                        da_text = da_du.getAttribute('code')
                        if da_text != '':
                            term_list.append(da_text)
                     
                    if da_du.hasChildNodes:
                        for da_da in da_du.childNodes:
                            
                            if da_da.nodeType == da_da.TEXT_NODE:
                                da_text = da_da.nodeValue
                                term_list.append(da_text)   
    return term_list

def Get_text(corpus_root = '/release/', hwid = 'abk0887'):    
    #wordlists = PlaintextCorpusReader(corpus_root, '.*')
    #wordlists = XMLCorpusReader(corpus_root, file_IDs)
    s = ''
    da_terms = get_term_list(hwid)
    for t in da_terms:
        s = s + t + ' '
        
    print "processing " + hwid
    #raw = wordlists.raw()
    #print "corpus rawed ..."
    tokens = nltk.word_tokenize(s)
    #print "corpus tokenized ..."
    text = nltk.Text(tokens)
    #print "corpus textified ..."
    
    simple_md = [word.lower() for word in text if word.isalpha()]
    #print "corpus lowercased and alphafied ..."
    simple_md = [word for word in simple_md if word != 'source']
    #print "keyword *source* removed ..."
    print "DONE!"
    return simple_md

