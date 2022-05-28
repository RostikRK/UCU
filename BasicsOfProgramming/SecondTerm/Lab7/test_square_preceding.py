from unittest import TestCase, main
from square_preceding import square_preceding


class TestSquare(TestCase):
    def test_square_preceding(self):
        L = [1, 2, 3, 4]
        square_preceding(L)
        self.assertEqual(L, [0, 1, 4, 9])


if __name__ == "__main__":
    main()
