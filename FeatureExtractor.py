#Feature Extractor to train this shit
import os
import nltk
import loadwords

word_features = []

#iterate a list of facet classes
#da_FacetValues = os.listdir('FacetValues')
da_Facet_Dir = 'lil_FacetValues/'
#da_Facet_Dir = 'FacetValues/'
da_FacetValues = os.listdir(da_Facet_Dir)

print '*********************************'
print '********* Collecting ***********'
print '*********************************'

for da_FacetValue in da_FacetValues:
    f = open(da_Facet_Dir+da_FacetValue, 'r')
    for hwid in f.read().split('\n'):
        print da_FacetValue.rstrip('.txt') + ':' + hwid
        #iterate hwids
        words = loadwords.Get_text('kb_xml', hwid)
        all_words = nltk.FreqDist(words)
        the_features = all_words.keys()[:2000]
        word_features = word_features + the_features
    f.close()

daStuff = nltk.FreqDist(word_features)


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

print '*********************************'
print '********* Classifying ***********'
print '*********************************'

featuresets = []
for da_FacetValue in da_FacetValues:
    f = open(da_Facet_Dir + da_FacetValue, 'r')
    for hwid in f.read().split('\n'):
        print da_FacetValue.rstrip('.txt') + ':' + hwid
        d = 'kb_xml' + hwid
        c = da_FacetValue
        featuresets = featuresets + [document_features(d), c] 
    f.close()
print '*********************************'
print '********* Classified! ***********'
print '*********************************'

train_set, test_set = featuresets[5:], featuresets[:5]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print '*** blab! ***'

print nltk.classify.accuracy(classifier, test_set)

