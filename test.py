import unittest
import four

class TestString(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(four.greeter(''), 'Hello, Mr Nobody!')

    def test_name(self):
        self.assertEqual(four.greeter('Bob'), 'Hello, Bob!')


if __name__ == '__main__':
    unittest.main()
