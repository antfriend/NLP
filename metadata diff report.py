"""
**********************************************************
*     compare the codes and keywords in 9.2 and 9.3      *
**********************************************************
"""

import os
import re

#da_source_folder = '9_3_PIs/'
da_source_folder = '9_2_PIs/'
da_result_file_name = da_source_folder + 'icd9codes.csv'
da_list_of_hwids_file_name = '9_3_PIs/PI_ICD10.txt'

#regex_string = r'<indexing\.item code=(.{1,}?)</indexing\.item>'
#regex_string = r'<indexing\.item code=(.{1,}?)relevance="(.)'
regex_string = r'type="ICD9CM">.{1,}?code=(.{1,}?) relevance="(.)".{1,}?</meta-data'

da_version = '9.3'

def find_all_codes_in_list_of_docs():
    
    result_file = open(da_result_file_name, 'w')
    result_file.write('hwid|icd9cm|relevance' + chr(10))
    
    f = open(da_list_of_hwids_file_name, 'r')
    for hwid in f.read().split('\n'):
        hwid = da_source_folder + hwid.lstrip('.../')
        if os.path.exists(hwid):
            pi = open(hwid, 'r')
            hwid = hwid.rstrip('.xml')
            hwid = hwid.split('/')[4]
            matches = re.findall(regex_string, pi.read())
            result_string = ''
            for m in matches:
                da_matching_string = ''
                for l in m:
                    da_matching_string = da_matching_string + '|' + l   
                #result_string = da_version + '|' + hwid + da_matching_string
                result_string = hwid + da_matching_string
                print result_string
            if result_string != '':
                result_file.write(result_string + chr(10))    
            pi.close()                    
        else:
            hwid = hwid.rstrip('.xml')
            hwid = hwid.split('/')[4]
            print '************************ ' + hwid
            result_file.write(hwid + '|"na"|0' + chr(10))
            
            
    f.close()
    result_file.close()
 
find_all_codes_in_list_of_docs()

