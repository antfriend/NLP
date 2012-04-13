#Feature Extractor to train this shit
import os
import nltk
import loadwords
import logging

word_features = []

# create logger with 'spam_application'
logger = logging.getLogger('feature_extraction')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('features.log')


#iterate a list of facet classes
#da_FacetValues = os.listdir('FacetValues')
#da_Facet_Dir = 'lil_FacetValues/'
da_Facet_Dir = 'FacetValues/'

def define_facetvalues():
    f_facets = os.listdir(da_Facet_Dir)
    r_facets = []
    for da_f in f_facets:
        da_f = da_f.split('.')[0]
        r_facets.append(da_f)
    return r_facets

da_FacetValues = define_facetvalues()

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
        print da_FacetValue + ':' + hwid
        #iterate hwids
        words = loadwords.Get_text('kb_xml', hwid)
        all_words = all_words + words
    f.close()
    
all_words = nltk.FreqDist(words)
word_features = all_words.keys()[10000:]
#daStuff = nltk.FreqDist(word_features)

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

print '*********************************'
print '********* Classifying ***********'
print '*********************************'

def get_featuresets():
    featuresets = []
    for da_FacetValue in da_FacetValues:
        f = open(da_Facet_Dir + da_FacetValue + '.txt', 'r')
        for hwid in f.read().split('\n'):
            print da_FacetValue + ':' + hwid
            #d = 'kb_xml' + hwid
            #c = da_FacetValue
            
            featuresets.append((document_features('kb_xml' + hwid), da_FacetValue)) 
        f.close()
    #featuresets[(document_features(d), c) for (d,c) in documents]   
    print '*********************************'
    print '********* Classified! ***********'
    print '*********************************'
    return featuresets

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

def this_is(xml_doc_path):
    doc_features = document_features(xml_doc_path)
    the_class = classy.classify(doc_features)
    
    return the_class

def get_classifier():
    return classy
   
def test_all_documents():
    f = open('alldocs.txt', 'r')
    for hwid in f.read().split('\n'):
        da_message = this_is(hwid)
        if da_message == 'Educational':
            pass
        else:
            print this_is(hwid)
        
#now run on all docs
test_all_documents()        

