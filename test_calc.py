import unittest

from calc import add, sub


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            add("2", 3)


class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            sub(5, "3")


if __name__ == "__main__":
    unittest.main()
