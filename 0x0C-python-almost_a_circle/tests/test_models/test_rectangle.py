import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_diminsions(self):
        rec6 = Rectangle(4, 5)
        self.assertEqual(rec6.width, 4)
        self.assertEqual(rec6.height, 5)

    def test_cordintations(self):
        rec7 = Rectangle(3, 4, 10, 20)
        self.assertEqual(rec7.x, 10)
        self.assertEqual(rec7.y, 20)

    def test_getter(self):
        rec = Rectangle(5, 6, 7, 8)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 6)
        self.assertEqual(rec.x, 7)
        self.assertEqual(rec.y, 8)

    def test_setters(self):
        rec8 = Rectangle(5, 6, 0, 0, 12)
        rec8.width = 10
        rec8.height = 15
        self.assertEqual(rec8.width, 10)
        self.assertEqual(rec8.height, 15)

    def test_check_for_positve(self):
        with self.assertRaises(ValueError):
            rec_9 = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            rec_9 = Rectangle(0, -2)

        with self.assertRaises(ValueError):
            rec_9 = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            rec = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            rec_a = Rectangle(1, 2, -3, 4)

        with self.assertRaises(ValueError):
            rec_b = Rectangle(1, 2, 3, -4)

    def test_check_type(self):
        with self.assertRaises(TypeError):
            rec = Rectangle("a", 5)

        with self.assertRaises(TypeError):
            rec = Rectangle(6, '5')

        with self.assertRaises(TypeError):
            rec = Rectangle(6, 3, "S", 5, 1)

        with self.assertRaises(TypeError):
            rec = Rectangle(6, 3, 6, "w", 1)

        with self.assertRaises(TypeError):
            rec = Rectangle(None, 3, 6, 2, 1)

    def test_area(self):
        rec = Rectangle(5, 6)
        self.assertEqual(rec.area(), 30)

        rec = Rectangle(5, 6, 3, 4, 12)
        self.assertEqual(rec.area(), 30)

        rec = Rectangle(5, 6, 3, 4)
        self.assertEqual(rec.area(), 30)

    def test_display_area(self):
        rec = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            rec.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_display_rec_with_coordintations(self):
        rec = Rectangle(2, 2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            rec.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update_args(self):
        rec = Rectangle(5, 6, 7, 8, 9)
        rec.update(1, 2, 3, 4, 5)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)

    def test_update_kwargs(self):
        rec = Rectangle(5, 6, 7, 8, 9)
        rec.update(width=1)
        self.assertEqual(rec.width, 1)

        rec.update(height=2)
        self.assertEqual(rec.height, 2)

        rec.update(x=3)
        self.assertEqual(rec.x, 3)

        rec.update(y=4)
        self.assertEqual(rec.y, 4)

        rec.update(id=12)
        self.assertEqual(rec.id, 12)

        with self.assertRaises(AttributeError):
            rec.update(FAKE=12)


if __name__ == '__main__':
    unittest.main()
