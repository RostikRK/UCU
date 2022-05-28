def dyvo_insert(sentence, flag):
    """
    
    (str, str) -> str
    Inserts word "диво" before every word that starts with flag.
    if word not starts with flag it just lefts the same
    
    >>> dyvo_insert("Диво кіт","кі")
    'диво дивокіт'
    """
    sentence = sentence.lower()
    empty_list = []
    for i in sentence.split(" "):
        if not i.startswith(flag):
            empty_list.append(i)
        elif i.startswith(flag):
            i = "диво" + i
            empty_list.append(i)
    res=" ".join(empty_list)
    return res