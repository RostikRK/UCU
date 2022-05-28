"""
Coollllll
"""

def find_film_keywords(film_keywords: dict, film_name: str):
    """
    (dict, str) -> (set)
    Finds all keywords which film has
    >>> find_film_keywords({'aa':['abc'], 'ab':['abc'], 'ac':['abb']}, 'abb')
    {'ac'}
    """
    res = set()
    for kee,vvel in film_keywords.items():
        for elemm in vvel:
            if elemm == film_name:
                res.add(kee)
    return res


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Returns the first n films with the largest amount of keywords
    >>> find_films_with_keywords({'aa':['abc'], 'ab':['abc'], 'ac':['abb']}, 1)
    [('abc', 2)]
    """
    res_list = []
    nnew_set = set()
    for veel in film_keywords.values():
        for eleem in veel:
            ssset = find_film_keywords(film_keywords, eleem)
            count = len(ssset)
            name = eleem
            tuup = (name, count)
            nnew_set.add(tuup)
    list_of_tuples = list(nnew_set)
    list_of_tuples.sort(key=lambda x:x[1], reverse = True)
    for i in range(0,num_of_films):
        res_list.append(list_of_tuples[i])
    if num_of_films == 0:
        res_list = []
    return res_list
