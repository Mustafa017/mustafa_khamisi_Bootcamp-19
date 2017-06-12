import unittest
from find_primes import find_prime_numbers

class test_if_its_prime(unittest.TestCase):
    def test_input_accepts_integers(self):
        self.assertEqual(find_prime_numbers("m"),"Argument should be an integer")
    def test_no_prime_less_than_2(self):
        self.assertEquals(find_prime_numbers(1),"there are no prime numbers less than 2")
    def test_correct_output(self):
        self.assertEquals(find_prime_numbers(11),[2,3,5,7,11],msg="correct output")
    def test_output_upto_n(self):
        self.assertEquals(find_prime_numbers(13),[2,3,5,7,11,13],msg="n is inclusive if it is prime")
    def test_2_is_prime(self):
        self.assertEquals(find_prime_numbers(2),[2],msg="2 is the only prime number that is even")

if __name__ == "__main__":
    unittest.main()