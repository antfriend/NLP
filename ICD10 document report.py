#find the PIs with ICD-10 codes

import os
import re

def find_all_ICD10_XML_docs():
    i = 0
    result_file = open('9_3_PIs/result_file.txt', 'w')
    f = open('9_3_PIs/PI_ICD10.txt', 'r')
    for hwid in f.read().split('\n'):
        hwid = '9_3_PIs/' + hwid.lstrip('.../')
        pi = open(hwid, 'r')
        m = re.search('ICD10PCS', pi.read())
        #change 'ICD10PCS' to 'ICD10CM' 
        if m != None:
            hwid = hwid.rstrip('.xml')
            hwid = hwid.split('/')[4]
            print hwid
            
            result_file.write(hwid + chr(10))
            i = i + 1
        pi.close()        
    f.close()
    print 'count = ' + str(i)
    result_file.close()

def find_all_ICD10_HTML_docs():
    i = 0
    result_file = open('9_3_PIs/result_file.txt', 'w')
    f = open('9_3_PIs/PI_ICD10.txt', 'r')
    for hwid in f.read().split('\n'):
        hwid = hwid.lstrip('.../')
        hwid = hwid.rstrip('.xml')
        hwid = hwid.split('/')[3]
        
        pi = open('9_3_PIs/html/content/' + hwid + 'en-us.htm', 'r')
        m = re.search('ICD-10', pi.read())
        if m != None:            
            print hwid            
            result_file.write(hwid + chr(10))
            i = i + 1
        pi.close()        
    f.close()
    print 'count = ' + str(i)
    result_file.close()
   
#find_all_ICD10_XML_docs()
find_all_ICD10_HTML_docs()
