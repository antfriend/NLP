import os
import re

CSV_Field_Separator = '|'
CSV_Filename = 'Symptom_Facets.csv'

File_List = [] #emptied and populated in 'Get_all_file_paths()' and 'walk_dirs()'

def Get_all_file_paths(Starting_Directory = 'store'):
    File_List = [] #global list
    walk_dirs(Starting_Directory)    
    return File_List

def walk_dirs(the_dir_path):
    temp_path = ''
    all_file_paths = {}
    all_file_paths = os.listdir(the_dir_path)
    for da_Dir in all_file_paths:       
        temp_path = the_dir_path + '/' + da_Dir
        if os.path.isfile(temp_path):
            File_List.append(temp_path)
        else:
            walk_dirs(temp_path)

def has_male(the_file):
    da_pattern = r'( man| male|boy)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def has_female(the_file):
    da_pattern = r'(female|woman|girl|preg)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def has_age(the_file):
    da_pattern = r'(age|old)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def is_nauseating(the_file):
    da_pattern = r'(vomit|naus)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def is_about_fever(the_file):
    da_pattern = r'(fever|temperature)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def is_about_heart_condition(the_file):
    da_pattern = r'(heart|cardi)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def has_a_severity_question(the_file):
    da_pattern = r'(severe|scale)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def has_a_pain(the_file):
    da_pattern = r'(pain|hurt)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False

def checks_for_shock(the_file):
    da_pattern = r'(shock|shiver)'
    m = re.search(da_pattern, the_file.lower())
    if m != None:
        return True
    else:
        return False



Get_all_file_paths()#populates the list variable, 'File_List'

da_Total = 0

o = open(CSV_Filename, 'w')
o.write(chr(34) + 'ITEM ID' + chr(34) + CSV_Field_Separator + chr(34) + 'FACET NAME' + chr(34) + CSV_Field_Separator + chr(34) + 'VALUE' + chr(34) + chr(10)) 
for item_id in File_List:
    #print ' '
    print item_id + ' #############################'
    f = open(item_id, 'r')
    
    da_Total = da_Total + 1
    the_string = f.read()       

    facet_name = 'has_male'
    result_value = has_male(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
                    
    facet_name =  'has_female'
    result_value = has_female(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
          
    facet_name = 'has_age'
    result_value = has_age(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
        
    facet_name = 'is_nauseating'
    result_value = is_nauseating(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
        
    facet_name = 'is_about_fever'
    result_value = is_about_fever(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
        
    facet_name = 'is_about_heart_condition'
    result_value = is_about_heart_condition(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
        
    facet_name = 'has_a_severity_question'
    result_value = has_a_severity_question(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
        
    facet_name = 'has_a_pain'
    result_value = has_a_pain(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)
        
    facet_name = 'checks_for_shock'
    result_value = checks_for_shock(the_string)
    o.write(chr(34) + item_id + chr(34) + CSV_Field_Separator + chr(34) + facet_name + chr(34) + CSV_Field_Separator + chr(34) + str(result_value) + chr(34) + chr(10))
    print facet_name + ':' + str(result_value)

    f.close()
    
#o.write(chr(34) + str(da_Total) + chr(34) + chr(10))

o.close()
    
print ' '
print 'Total  : ' + str(da_Total)
print ' '

