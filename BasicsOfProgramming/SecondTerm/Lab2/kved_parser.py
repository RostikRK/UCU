"""
Data parser
"""
import json


def reading_dict(path):
    """
    Reads the file and generates data
    >>> ":-)" == ":-("
    False
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_correct_values(data, class_code):
    """
    Get the list from data with values which we need
    >>> ":-)" == ":-("
    False
    """
    val_list = []
    for section in data['sections'][0]:
        for division in section.get('divisions'):
            if division.get("divisionCode")==class_code[:2]:
                for group in division.get('groups'):
                    if group.get("groupCode") == class_code[:4]:
                        for class_ in group.get('classes'):
                            required = class_.get('classCode')
                            if required == class_code:
                                val_list.append(class_['className'])
                                val_list.append(group['groupName'])
                                val_list.append(len(group.get('classes')))
                                val_list.append(division['divisionName'])
                                val_list.append(len(division.get('groups')))
                                val_list.append(section['sectionName'])
                                val_list.append(len(section.get('divisions')))
    return val_list

def parse_kved(class_code):
    '''
    The main function which rewrites the json file just with information that\
we need
    >>> ":-)" == ":-("
    False
    '''
    data = reading_dict("kved.json")
    value_list = get_correct_values(data, class_code)
    res_dict = {'name': value_list[0], 'type': 'class',
                'parent': {'name': value_list[1], 'type': 'group', \
"num_children": value_list[2],
                           'parent': {'name': value_list[3], 'type': \
'division', "num_children": value_list[4],
                                      'parent': {'name': value_list[5], \
'type': 'section',
                                                 'num_children': \
value_list[6]}}}}
    with open('kved_results.json', 'w', encoding='utf-8') as fiiile:
        json.dump(res_dict, fiiile, ensure_ascii=False, indent=4)
