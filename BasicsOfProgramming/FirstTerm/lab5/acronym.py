def create_acronym(message):
    """
    (str) -> str
    Creates the acronyms from phrases
    >>> 5 == 4
    False
    """
    sentence_list = message.split("\n")
    acron=[]
    res=[]
    for i in sentence_list:
        word = []
        for x in i.upper().split():
            word.append(x[0])
        acron.append("".join(word))
    for i in range (len(sentence_list)):
        if i != len(sentence_list):
            a = acron[i] + " - " + sentence_list[i] + "\n"
        elif i== len(sentence_list):
            a = acron[i] + " - " + sentence_list[i]
        res.append(a)
    result = "".join(res)
    return result