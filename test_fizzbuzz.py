import fizzbuzz
import unittest

class TestFb(unittest.TestCase):
    """
    Test the fb function from the fizzbuzz library
    """

    def test_num(self):
        """
        Test that it prints the number when not divisible by 3 nor by 5
        """
        result = fizzbuzz.fb(1)
        self.assertEqual(result, 1)

    def test_fizz(self):
        """
        Test that it prints 'Fizz' when divisible by 3
        """
        result = fizzbuzz.fb(3)
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        """
        Test that it prints 'Buzz' when divisible by 5
        """
        result = fizzbuzz.fb(5)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        """
        Test that it prints 'FizzBuzz' when divisible by 3 and by 5
        """
        result = fizzbuzz.fb(15)
        self.assertEqual(result, 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
