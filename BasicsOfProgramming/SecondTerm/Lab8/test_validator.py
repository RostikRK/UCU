import validator
from unittest import TestCase, main

valid = validator.Validator()


class TestValidator(TestCase):
    def test_name_surname_valid(self):
        self.assertEqual(valid.validate_name_surname(
            "Elvis Presley forever"), False)
        self.assertEqual(valid.validate_name_surname("Elvis P"), False)
        self.assertEqual(valid.validate_name_surname("El1vis Presley"), False)

    def test_age_valid(self):
        self.assertEqual(valid.validate_age("20"), True)
        self.assertEqual(valid.validate_age("98"), True)
        self.assertEqual(valid.validate_age("20a"), False)
        self.assertEqual(valid.validate_age("7"), False)

    def test_country_valid(self):
        self.assertEqual(valid.validate_country("USA"), True)
        self.assertEqual(valid.validate_country("USA34"), False)

    def test_region_valid(self):
        self.assertEqual(valid.validate_region("Lviv1"), True)
        self.assertEqual(valid.validate_region("lviv1"), False)

    def test_living_place_valid(self):
        self.assertEqual(valid.validate_living_place(
            "Koselnytska st. 2a"), True)
        self.assertEqual(valid.validate_living_place(
            "koselnytska sat. 2a"), False)

    def test_index_valid(self):
        self.assertEqual(valid.validate_index("79000"), True)
        self.assertEqual(valid.validate_index("79000e"), False)

    def test_phone_valid(self):
        self.assertEqual(valid.validate_phone("+380951234567"), True)
        self.assertEqual(valid.validate_phone("-380951234567"), False)
        self.assertEqual(valid.validate_phone("+38 (095) 123-45-67"), True)

    def test_email_valid(self):
        self.assertEqual(valid.validate_email(
            "username+usersurname@domain.com"), True)
        self.assertEqual(valid.validate_email("username@ucu.edu.ua"), True)
        self.assertEqual(valid.validate_email("username@domain.aaa"), False)

    def test_id_valid(self):
        self.assertEqual(valid.validate_id("011111"), True)
        self.assertEqual(valid.validate_id("123456"), False)
        self.assertEqual(valid.validate_id("123006"), False)

    def test_data_valid(self):
        self.assertEqual(valid.validate(
            "Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"), True)
        self.assertEqual(valid.validate(
            "Elvis Presley, 7, Ukrai5ne, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"), False)


if __name__ == "__main__":
    main()
