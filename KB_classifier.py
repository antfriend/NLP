#Feature Extractor to train this shit
import os
import nltk
import loadwords
import logging

word_features = []

#iterate a list of facet classes
#da_Facet_Dir = 'wee_facets/'
da_Facet_Dir = 'new_FacetValues/'

# create logger with 'spam_application'
logger = logging.getLogger('feature_extraction')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('features.log')

def define_facetvalues():
    f_facets = os.listdir(da_Facet_Dir)
    r_facets = []
    for da_f in f_facets:
        da_f = da_f.split('.')[0]
        r_facets.append(da_f)
    return r_facets

da_FacetValues = define_facetvalues()

def massage_techdocs_path_string(da_path_and_hwid):
    da_path_and_hwid = da_path_and_hwid.lstrip('../')
    da_path_and_hwid = 'hwxml/' + da_path_and_hwid    
    return da_path_and_hwid

print '*********************************'
print '********* Facets ***********'
print '*********************************'

for da_FacetValue in da_FacetValues:
    #da_FacetValue = da_FacetValue.split('.')[0]
    print da_FacetValue

    
print '*********************************'
print '********* Collecting ***********'
print '*********************************'
all_words = []
for da_FacetValue in da_FacetValues:
    f = open(da_Facet_Dir+da_FacetValue + '.txt', 'r')
    for hwid in f.read().split('\n'):
        hwid = massage_techdocs_path_string(hwid)
        print da_FacetValue + ':' + hwid
        #iterate hwids
        words = loadwords.Get_text('kb_xml/', hwid)
        all_words = all_words + words
    f.close()
    
all_words = nltk.FreqDist(words)
word_features = all_words.keys()[:1000]

#daStuff = nltk.FreqDist(word_features)

def document_features(da_document):
    #need to load the document and iterate it's words
    #da_document = massage_techdocs_path_string(da_document)
    print 'path is ' + da_document
    document_words = loadwords.Get_text('kb_xml/', da_document)
    features = {}
    #print document_words
    
    for word in word_features:
        #print word
        features['contains(%s)' % word] = (word in document_words)
        #features['contains word'] = word
        #add more features here like
        #features['doctype'] = doctype
       
    return features

print '*********************************'
print '********* Classifying ***********'
print '*********************************'

def get_featuresets():
    featuresets = []
    for da_FacetValue in da_FacetValues:
        f = open(da_Facet_Dir + da_FacetValue + '.txt', 'r')
        for hwid in f.read().split('\n'):
            hwid = massage_techdocs_path_string(hwid)
            print da_FacetValue + ':' + hwid
            #d = 'kb_xml' + hwid
            #c = da_FacetValue
            more_features = document_features(hwid)
            featuresets.append((more_features, da_FacetValue)) 
        f.close()
    #featuresets[(document_features(d), c) for (d,c) in documents]   
    print '*********************************'
    print '********* Classified! ***********'
    print '*********************************'
    return featuresets

def this_is(xml_doc_path):
    xml_doc_path = massage_techdocs_path_string(xml_doc_path)
    doc_features = document_features(xml_doc_path)
    the_class = classy.classify(doc_features)
    
    return the_class

def get_classifier():
    return classy
   
def test_all_documents():
    f = open('alldocs.txt', 'r')
    for test_hwid in f.read().split('\n'):        
            print test_hwid
            print 'classified as '
            print this_is(test_hwid)
            print ' '

featuresets2 = get_featuresets()
print '*** got features! ***'
size = int(len(featuresets2) * 0.5)
train_set, test_set = featuresets2[size:], featuresets2[:size]
print '*** sets trained! ***'
classifier = nltk.NaiveBayesClassifier.train(train_set)
print '*** classified! ***'
print nltk.classify.accuracy(classifier, test_set)
print classifier.labels()

classy = nltk.NaiveBayesClassifier.train(featuresets2)

        
#now run on all docs
test_all_documents()        

