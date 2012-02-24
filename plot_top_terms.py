import loadmd
import nltk

#md = loadmd.Get_MD_text()
md = loadmd.Get_MD_text('kb_xml/hwxml/xml/aa10')
#md = loadmd.Get_MD_text('kb_xml/hwxml/categories')

fdist = nltk.FreqDist(md)
min_md = [w for w in md if len(w) > 3 and fdist[w] > 700]
fdist1 = nltk.FreqDist(min_md)
fdist1.plot()
