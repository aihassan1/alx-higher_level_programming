import unittest
from io import StringIO
from unittest.mock import patch

from models.square import Square


class TestSquareCase(unittest.TestCase):

    def test_diminsions(self):
        square6 = Square(5)
        self.assertEqual(square6.width, 5)
        self.assertEqual(square6.height, 5)

    def test_cordintations(self):
        square7 = Square(6, 10, 20)
        self.assertEqual(square7.x, 10)
        self.assertEqual(square7.y, 20)

    def test_getter(self):
        square = Square(7, 7, 8)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_setters(self):
        square8 = Square(10, 0, 0)
        square8.width = 10
        self.assertEqual(square8.width, 10)
        self.assertEqual(square8.height, 10)

    def test_check_for_positve(self):
        with self.assertRaises(ValueError):
            square_9 = Square(-2)

        with self.assertRaises(ValueError):
            square_a = Square(3, -3, 4)

        with self.assertRaises(ValueError):
            square_b = Square(6, 3, -4)

    def test_check_type(self):
        with self.assertRaises(TypeError):
            square = Square("a")

        with self.assertRaises(TypeError):
            square = Square('5')

        with self.assertRaises(TypeError):
            square = Square(6, 3, "S", 5)

        with self.assertRaises(TypeError):
            square = Square(6, 6, "w")

        with self.assertRaises(TypeError):
            square = Square(None, 3, 6, 2)

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

        square = Square(0)
        self.assertEqual(square.area(), 0)

        with self.assertRaises(TypeError):
            square = Square('s')

    def test_display_area(self):
        square = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            square.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_display_square_with_coordintations(self):
        square = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            square.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update_args(self):
        square = Square(6, 7, 8, 9)
        square.update(1, 3, 4, 5)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_update_kwargs(self):
        square = Square(5, 6, 7, 8)
        square.update(width=1)
        self.assertEqual(square.width, 1)

        square.update(height=2)
        self.assertEqual(square.height, 2)

        square.update(x=3)
        self.assertEqual(square.x, 3)

        square.update(y=4)
        self.assertEqual(square.y, 4)

        square.update(id=12)
        self.assertEqual(square.id, 12)

        with self.assertRaises(AttributeError):
            square.update(FAKE=12)


if __name__ == '__main__':
    unittest.main()
