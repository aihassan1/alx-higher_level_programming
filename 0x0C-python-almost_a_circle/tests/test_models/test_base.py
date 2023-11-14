import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_object_creation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b_15 = Base(15)
        self.assertEqual(b_15.id, 15)


if __name__ == "__main__":
    unittest.main()
