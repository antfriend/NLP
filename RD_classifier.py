#Load Features from RD documents
import os
import nltk
import loadwords
import loadwordsfromURL

CSV_Field_Separator = '|'
CSV_Filename = 'RD_classes.csv'
File_List_of_Documents_to_Classify = 'alldocs.txt'

word_features = []

#iterate a list of facet classes
da_Facet_Dir = 'RDs/'
#da_Facet_Dir = 'new_FacetValues/'
#da_Facet_Dir = 'FacetValues/'

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
        #hwid = massage_techdocs_path_string(hwid)
        print da_FacetValue + ':' + hwid
        #iterate hwids
        words = loadwordsfromURL.Get_text('kb_xml/', hwid)
        all_words = all_words + words
    f.close()
    
all_words = nltk.FreqDist(words)
word_features = all_words.keys()[:1000]

#daStuff = nltk.FreqDist(word_features)

def document_features(da_document):
    #need to load the document and iterate it's words
    document_words = loadwords.Get_text('kb_xml/', da_document)
    features = {}
    
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
        #features['contains word'] = word
        #add more features here like
        #features['doctype'] = doctype
       
    return features

def URLdocument_features(da_hwid):
    #need to load the document and iterate it's words
    document_words = loadwordsfromURL.Get_text('kb_xml/', da_hwid)
    features = {}
    
    for word in word_features:
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
            #hwid = massage_techdocs_path_string(hwid)
            print da_FacetValue + ':' + hwid
            more_features = URLdocument_features(hwid)
            featuresets.append((more_features, da_FacetValue)) 
        f.close()

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
    f = open(File_List_of_Documents_to_Classify, 'r')
    o = open(CSV_Filename, 'w')
    for test_hwid in f.read().split('\n'):        
            print test_hwid
            
            print 'classified as '
            da_classification = this_is(test_hwid)
            o.write(chr(34) + test_hwid + chr(34) + CSV_Field_Separator + chr(34) + da_classification + chr(34) + chr(10))        
            print da_classification
            print ' '
    f.close()
    o.close()
    
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

