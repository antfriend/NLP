"""
**********************************************************
*     compare the codes and keywords in 9.2 and 9.3      *
**********************************************************
"""

import os
import re

#da_source_folder = '9_3_PIs/'
#da_source_folder = '9_2_PIs/'

#regex_string = r'<indexing\.item code=(.{1,}?)</indexing\.item>'
#regex_string = r'<indexing\.item code=(.{1,}?)relevance="(.)'
regex_string_outer = r'type="ICD9CM"(>.{1,}?<)/meta-data'
regex_string_inner = r'code=(.{1,}?) relevance="(.)">(.{1,}?)<'

def find_all_codes_in_list_of_docs():
    da_result_file_name = da_source_folder + 'icd9codes.csv'
    da_list_of_hwids_file_name = '9_3_PIs/PI_ICD10.txt'
    
    result_file = open(da_result_file_name, 'w')
    result_file.write('hwid|icd9cm|relevance|description' + chr(10))
    
    f = open(da_list_of_hwids_file_name, 'r')
    for hwid in f.read().split('\n'):
        hwid = da_source_folder + hwid.lstrip('.../')
        if os.path.exists(hwid):
            pi = open(hwid, 'r')
            hwid = hwid.rstrip('.xml')
            hwid = hwid.split('/')[4]
            matches = re.findall(regex_string_outer, pi.read())
            result_string = ''
            for m in matches:
                inner_matches = re.findall(regex_string_inner, m)
                for inner_tuples in inner_matches:
                    da_matching_string = ''
                    result_string = ''
                    for l in inner_tuples:
                        da_matching_string = da_matching_string + '|' + l   
                        result_string = hwid + da_matching_string                       
                    if result_string != '':
                        print result_string
                        result_file.write(result_string + chr(10))    
            pi.close()                    
        else:
            hwid = hwid.rstrip('.xml')
            hwid = hwid.split('/')[4]
            print '************************ ' + hwid
            result_file.write(hwid + '|"na"|0' + chr(10))
            
            
    f.close()
    result_file.close()

da_source_folder = '9_2_PIs/'
find_all_codes_in_list_of_docs()
da_source_folder = '9_3_PIs/'
find_all_codes_in_list_of_docs()

