#Feature Extractor to train this shit
import os
import nltk
import loadwords

word_features = []

#iterate a list of facet classes
da_FacetValues = os.listdir('FacetValues')

for da_FacetValue in da_FacetValues:
    f = open('FacetValues/'+da_FacetValue, 'r')
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




