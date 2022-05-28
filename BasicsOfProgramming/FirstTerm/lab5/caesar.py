def caesar_encode(message, key):
    """
    (str, int) -> str
    Codes caesar code
    >>> 5 == 4
    False
    """
    code=[]
    key = key % 26
    for i in message:
        if i.isalpha():
            posit=ord(i)
            posit2=posit + key
            if posit2>122:
                posit2 = posit-(26-(key))
                code.append(chr(posit2))
            elif posit2<=122:
                code.append(chr(posit2))
        else:
            code.append(i)
    res = "".join(code)
    return res
def caesar_decode(message, key):
    """
    (str, int) -> str
    DeCodes caesar code
    >>> 5==6
    False
    """
    code=[]
    key = key % 26
    for i in message:
        if i.isalpha():
            posit=ord(i)
            posit2=posit - key
            if posit2<97:
                posit2 = posit+(26-(key))
                code.append(chr(posit2))
            elif posit2>=97:
                code.append(chr(posit2))
        else:
            code.append(i)
    res = "".join(code)
    return res