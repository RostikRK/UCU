"""
Names
"""
import io
def find_names(file_path):
    """
    Works with file from path and return tuple with 3 values
    >>> ":-)" == ":-)"
    True
    """
    lst =[]
    with io.open(file_path, encoding='utf-8') as fil:
        for line in fil:
            lst.append(line)
    lst = lst[1:]
    nlst = []
    dell = "\n()"
    for ellem in lst:
        for char in dell:
            ellem = ellem.replace(char, "")
        nlst.append(ellem)
    diict = {}
    for eleem in nlst:
        koe = eleem.split(" \t")
        diict[koe[0]] = int(koe[1])
    top_3 = sorted(diict, key=diict.get, reverse=True)[:3]
    top_3 = set(top_3)
    points = 0
    single_names = set()
    for kkey, val in diict.items():
        if val == 1:
            points += 1
            single_names.add(kkey)
    letter_lst = ["А", "Я", "Ч", "С", "М", "Т", "Б", "Ю", "Ф", "І", \
"В", "П", "Р", "О", "Л", "Д", "Ж", "Й", "Ц", "У", "К", "Е", "Н", "Г" \
"Ш", "Щ", "З", "Х"]
    count_letters = {}
    for lett in letter_lst:
        point = 0
        for kkeey in diict.keys():
            if kkeey.startswith(lett):
                point += 1
        count_letters[lett] = point
    sec_t = (points, single_names)
    main_let = sorted(count_letters, key=count_letters.get, reverse=True)[0]
    count_names = 0
    count_children = 0
    for kkkey, valllue in diict.items():
        if kkkey.startswith(main_let):
            count_names += 1
            count_children += valllue
    thir_t = (main_let, count_names, count_children)
    ans = (top_3, sec_t, thir_t)
    return ans
