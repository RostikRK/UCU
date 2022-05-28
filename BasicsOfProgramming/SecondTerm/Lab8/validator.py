"""Validator"""

import re


class Validator:
    """
    Validates different data
    """

    def validate_name_surname(self, name_surname: str):
        """
        Checks the Name and Surname pattern
        >>> valid = Validator()
        >>> valid.validate_name_surname("Elvis Presley")
        True
        """
        if re.match('[A-Z][a-z]{1,29}\s[A-Z][a-z]{1,29}$', name_surname) == None:
            return False
        else:
            return True

    def validate_age(self, age: str):
        """
        Checks the age pattern
        >>> valid = Validator()
        >>> valid.validate_age("20")
        True
        """
        if re.match('(1[6-9])|([2-9][0-9])$', age) == None:
            return False
        else:
            return True

    def validate_country(self, country: str):
        """
        Checks the country pattern
        >>> valid = Validator()
        >>> valid.validate_country("Ukraine")
        True
        """
        if re.match('[A-Z][A-Za-z]{1,9}$', country) == None:
            return False
        else:
            return True

    def validate_region(self, region: str):
        """
        Checks the Name and Surname pattern
        >>> valid = Validator()
        >>> valid.validate_region("lviv")
        True
        """
        if re.match('[A-Z]\w{1,9}$', region) == None:
            return False
        else:
            return True

    def validate_living_place(self, living_place: str):
        """
        Checks the living place pattern
        >>> valid = Validator()
        >>> valid.validate_living_place("Koselnytska st. 2a")
        True
        """
        if re.match('[A-Z][A-Za-z]{2,19}\s(st|av|prosp|rd)\.\s[1-9][1-9a-z]$',\
        living_place) == None:
            return False
        else:
            return True

    def validate_index(self, index: str):
        """
        Checks the index pattern
        >>> valid = Validator()
        >>> valid.validate_index("79000")
        True
        """
        if re.match('\d{5}$', index) == None:
            return False
        else:
            return True

    def validate_phone(self, phone: str):
        """
        Checks the phone pattern
        >>> valid = Validator()
        >>> valid.validate_phone("+380951234567")
        True
        """
        if re.match('\+((\d{9,12})|(\d{2}\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}))$',\
        phone) == None:
            return False
        else:
            return True

    def validate_email(self, email: str):
        """
        Checks the email pattern
        >>> valid = Validator()
        >>> valid.validate_email("username@domain.com")
        True
        """
        if re.match('(\w|[!#$%&\'*\+-\/=?^_`{\|}~])(\w|[!#$%&\'*\+-\/=?^_`{\|}~|\.]){1,62}?(\w|[!#$%&\'*\+-\/=?^_`{\|}~])?@(\w|[!#$%&\'*\+-\/=?^_`{\|}~|\.]){1,251}\.(com|org|ua|edu|gov|net)$', email) == None:
            return False
        else:
            return True

    def validate_id(self, id: str):
        """
        Checks the id pattern
        >>> valid = Validator()
        >>> valid.validate_id("123450")
        True
        """
        if re.match('(0[1-9]{5}|[1-9]0[1-9]{4}|[1-9]{2}0[1-9]{3}|[1-9]{3}0[1-9]{2}|[1-9]{4}0[1-9]|[1-9]{5}0)$', id) == None:
            return False
        else:
            return True

    def validate(self, data: str):
        """
        Checks the whole data pattern
        >>> valid = Validator()
        >>> valid.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska", \
        "st. 2a, 79000, +380951234567, username@domain.com, 123450")
        True
        """
        data_temp = re.split(r'[,;]', data)
        data_list = []
        for elem in data_temp:
            if elem.startswith(" ") == True:
                data_list.append(elem[1:])
            else:
                data_list.append(elem)
        for count, line in enumerate(data_list):
            if count == 0:
                data_list[count] = self.validate_name_surname(line)
            elif count == 1:
                data_list[count] = self.validate_age(line)
            elif count == 2:
                data_list[count] = self.validate_country(line)
            elif count == 3:
                data_list[count] = self.validate_region(line)
            elif count == 4:
                data_list[count] = self.validate_living_place(line)
            elif count == 5:
                data_list[count] = self.validate_index(line)
            elif count == 6:
                data_list[count] = self.validate_phone(line)
            elif count == 7:
                data_list[count] = self.validate_email(line)
            else:
                data_list[count] = self.validate_id(line)
        if data_list.count(True) == 9:
            return True
        else:
            return False
