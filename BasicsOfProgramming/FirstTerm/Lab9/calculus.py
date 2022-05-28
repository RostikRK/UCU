"""
Ya krasavchik
"""

def find_max_1(functi, points):
    """
    (function or str, list(number)) -> (number)
    Find and return maximal value of function f in points.
    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    if type(functi) == str:
        pointr_list = list(map(lambda x: eval(functi), points))
    else:
        pointr_list = list(map(functi, points))
    res = max(pointr_list)
    return res

def find_max_2(functi, points):
    """
    (function or str, list(number)) -> (number)
    Find and return list of points where function f has the maximal value.
    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    rest = []
    maxim = find_max_1(functi, points)
    if type(functi) == str:
        for indss in points:
            res = (lambda x: eval(functi))(indss)
            if res == maxim:
                rest.append(indss)
    else:
        for indss in points:
            res = functi(indss)
            if res == maxim:
                rest.append(indss)
    return rest

def compute_limit(seq):
    """
    (function or str) -> (number)
    Compute and return limit of a convergent sequence.
    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.00
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.00
    """
    lst = []

    i = 0
    if type(seq) == str:
        while True:
            n = 10 ** i
            lst.append(eval(seq)) # adding new element
            if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
                res = round(lst[i], 2)
                break
            i += 1
    else:
        while True:
            n = 10 ** i
            sedd = seq(n)
            lst.append(sedd)
            # check the difference between elements
            if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
                res =round(lst[i], 2)
                break
            i += 1
    return res

print(compute_limit(lambda n: (n ** 2 + n) / n ** 2))
def compute_derivative(functi, x_0):
    """
    (function or str, number) -> (number)
    Compute and return derivative of function f in the point x_0.
    >>> compute_derivative('x ** 2 + x', 2)
    5.00
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.00
    """

    aprox = []

    i = 0

    if type(functi) == str:
        while True:
            dx = 10 **-i
            x = x_0 + dx
            dF = eval(functi)
            x = x_0
            dF -= eval(functi)
            der = dF / dx
            aprox.append(der)
            if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
                res =  round(aprox[i], 2)
                break
            i += 1
    else:
        while True:
            dx =  10 ** -i
            x = x_0 + dx
            sedd = functi(x)
            dF = sedd
            x = x_0
            dF -= functi(x)
            der = dF / dx
            aprox.append(der)
            if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
                res =  round(aprox[i], 2)
                break
            i += 1
    return res

def get_tangent(functi, x_0):
    """
    (function or str, number) -> (str)
    Compute and return tangent line to function f in the point x_0.
    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x - 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x + 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    if type(functi) == str:
        func = lambda x: eval(functi)
        fvix = float(func(x_0))
        koe = compute_derivative(functi, x_0)
        koef = round(float(koe), 1)
        besh = float(fvix) - float(koef) * x_0
        if koef >= 0:
            if besh < 0:
                res = str(koef) + (" * x ")  + " - " + str(abs(besh))
            if besh > 0:
                res = str(koef) + (" * x ")  + " + " + str(abs(besh))
            if besh == 0:
                res = str(koef) + (" * x ")
        if koef < 0:
            if besh < 0:
                res = "- " + str(abs(koef)) + (" * x ")  + " - " + str(abs(besh))
            if besh > 0:
                res = "- " + str(abs(koef)) + (" * x ")  + " + " + str(abs(besh))
            if besh == 0:
                res = "- " + str(abs(koef)) + (" * x ")
    else:
        fvix = float(functi(x_0))
        koe = compute_derivative(functi, x_0)
        koef = round(float(koe), 1)
        besh = float(fvix) - float(koef) * x_0
        if koef >= 0:
            if besh < 0:
                res = str(koef) + (" * x ")  + " - " + str(abs(besh))
            if besh > 0:
                res = str(koef) + (" * x ")  + " + " + str(abs(besh))
            if besh == 0:
                res = str(koef) + (" * x ")
        if koef < 0:
            if besh < 0:
                res = "- " + str(abs(koef)) + (" * x ")  + " - " + str(abs(besh))
            if besh > 0:
                res = "- " + str(abs(koef)) + (" * x ")  + " + " + str(abs(besh))
            if besh == 0:
                res = "- " + str(abs(koef)) + (" * x ")
    return res

def get_root(ffff, aaa, bbbb):
    """
    (function or str, number, number) -> (number)
    Compute and return root of the function f in the interval (a, b).
    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    ghsjdg= type(bbbb)
    sdfh = type(aaa)
    jafdsja = type(ffff)
    res = 0.0
    return res
    