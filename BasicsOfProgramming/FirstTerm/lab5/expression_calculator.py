def calculate_expression(expression):
    """
    (str) -> int
    Makes form an expressin a formula and calculates it
    
    >>> calculate_expression("Скільки буде 14 поділити на -2 додати 11 мінус -3?")
    7
    >>> calculate_expression("Скільки буде 10 поділити на -2 11 мінус -3?")
    'Неправильний вираз!'
    """
    expression = expression.replace("?", "")
    expression = expression.replace(",", "")
    expression = expression.replace(".", "")
    expression = expression.replace("!", "")
    empty_list=expression.split(" ")
    res_list=[]
    for i in empty_list:
        if i.isnumeric():
            res_list.append(i)
        elif i=="додати" or i=="плюс":
            res_list.append("+")
        elif i=="відняти" or i=="мінус":
            res_list.append("-")
        elif i=="помножити":
            res_list.append("*")
        elif i=="поділити":
            res_list.append("/")
        elif i.startswith("-"):
            res_list.append(i)
    if ('-' in res_list) or ('+' in res_list) or ('*' in res_list) or ('/' in res_list):
        for j in range(len(res_list)-1):
            first_sum = res_list[j]
            next_sum = res_list[j+1]
            if (first_sum.isnumeric()==True) and ((next_sum.isnumeric()==True) or (next_sum.startswith("-")==True)):
                res = "Неправильний вираз!"
            else:
                    res_str = " ".join(res_list)
                    res = int(eval(res_str))
    elif len(res_list)==1 and res_list[0].isnumeric:
        res = "Неправильний вираз!"
    else:
        res = "Неправильний вираз!"
    return res
