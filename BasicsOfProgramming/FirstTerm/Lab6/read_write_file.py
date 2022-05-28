"""
high level support for doing this and that.
"""

from typing import List
import urllib.request

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    Return list of strings lists from url
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/m\
aster/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/m\
aster/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+',\
 '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    empty_list = []
    line_list = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode( 'utf-8' )
            line = line.split()
            for j in line:
                if j == "наказу":
                    line_list.append(line[0])
                    line_list.append(" ".join(line[1:4]))
                    line_list.append('+')
                    line_list.append(line[6])
                if j == "Рекомендовано":
                    line_list.append(line[0])
                    line_list.append(" ".join(line[1:4]))
                    line_list.append('+')
                    line_list.append(line[6])
                if j == "Середній":
                    line_list.append(line[5])
                if len(line_list)==5:
                    if len(empty_list)<number:
                        empty_list.append(line_list)
                    line_list = []
    return empty_list


def write_csv_file(url: str):
    """
    Writes the txt file into the csv
    >>> 4 == 5
    False
    """
    prelist = read_input_file(url, 10000)
    with open('total.csv', 'w') as fille:
        fille.write("№,ПІБ,Д,Заг.бал,С.б.док.осв.\n")
        for row in prelist:
            for elem in row:
                fille.write(str(elem) + ',')
            if row != prelist[-1]:
                fille.write('\n')
            elif row == prelist[-1]:
                fille.write('')
