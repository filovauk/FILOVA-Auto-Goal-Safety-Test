import unittest

from calc import add, mul, sub


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


class TestMul(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(4, 3), 12)

    def test_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            mul(4, "3")


if __name__ == "__main__":
    unittest.main()
