import unittest
import kmath

class TestKMath(unittest.TestCase):
    def test_fibonacci_gen(self):
        gen = kmath.fibonacci_gen()
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 5)
        self.assertEqual(next(gen), 8)
        self.assertEqual(next(gen), 13)
        self.assertEqual(next(gen), 21)
        self.assertEqual(next(gen), 34)
        self.assertEqual(next(gen), 55)                
        
    def test_get_nth_fibonacci(self):
        self.assertRaises(ValueError, kmath.get_nth_fibonacci, 0)
        self.assertEqual(kmath.get_nth_fibonacci(1), 1)
        self.assertEqual(kmath.get_nth_fibonacci(2), 1)
        self.assertEqual(kmath.get_nth_fibonacci(3), 2)
        self.assertEqual(kmath.get_nth_fibonacci(4), 3)
        self.assertRaises(ValueError, kmath.get_nth_fibonacci, 4.5)
        self.assertEqual(kmath.get_nth_fibonacci(5), 5)
        self.assertEqual(kmath.get_nth_fibonacci(6), 8)
        self.assertEqual(kmath.get_nth_fibonacci(7), 13)
        self.assertEqual(kmath.get_nth_fibonacci(8), 21)
        self.assertEqual(kmath.get_nth_fibonacci(9), 34)
        self.assertEqual(kmath.get_nth_fibonacci(10), 55)        
    
    def test_factorial(self):
        self.assertRaises(ValueError, kmath.factorial, -1)
        self.assertEqual(kmath.factorial(0), 1)       
        self.assertEqual(kmath.factorial(1), 1)
        self.assertEqual(kmath.factorial(2), 2)
        self.assertEqual(kmath.factorial(3), 6)
        self.assertEqual(kmath.factorial(4), 24)
        self.assertRaises(ValueError, kmath.factorial, 4.5)
        self.assertEqual(kmath.factorial(5), 120)
        self.assertEqual(kmath.factorial(6), 720)
        self.assertEqual(kmath.factorial(7), 5040)
        self.assertEqual(kmath.factorial(8), 40320)
        self.assertEqual(kmath.factorial(9), 362880)
        self.assertEqual(kmath.factorial(10), 3628800)        
	
    def test_GCF(self):
        self.assertEqual(kmath.GCF(1920, 1080), 120)
        self.assertEqual(kmath.GCF(120, 240), 120)
        self.assertEqual(kmath.GCF(50, 60), 10)
        self.assertEqual(kmath.GCF(10, 5), 5)
        
    def test_LCM(self):
        self.assertEqual(kmath.LCM(3, 4), 12)
        self.assertEqual(kmath.LCM(4, 6), 12)
        self.assertEqual(kmath.LCM(6, 8), 24)
        self.assertEqual(kmath.LCM(8, 12), 24)
        self.assertEqual(kmath.LCM(12, 15), 60)
        self.assertEqual(kmath.LCM(15, 20), 60)
        self.assertEqual(kmath.LCM(20, 30), 60)
        
    def test_is_prime(self):
        self.assertRaises(ValueError, kmath.is_prime, -1)
        self.assertFalse(kmath.is_prime(0))
        self.assertFalse(kmath.is_prime(1))        
        self.assertTrue(kmath.is_prime(2))
        self.assertTrue(kmath.is_prime(3))
        self.assertFalse(kmath.is_prime(4))
        self.assertRaises(ValueError, kmath.is_prime, 4.5)
        self.assertTrue(kmath.is_prime(5))
        self.assertFalse(kmath.is_prime(6))
        self.assertTrue(kmath.is_prime(7))
        self.assertFalse(kmath.is_prime(8))
        self.assertFalse(kmath.is_prime(9))
        self.assertFalse(kmath.is_prime(10))
        self.assertTrue(kmath.is_prime(11))    
        
    def test_is_palindrome(self):
        self.assertFalse(kmath.is_palindrome(-1))
        self.assertTrue(kmath.is_palindrome(0))        
        self.assertTrue(kmath.is_palindrome(4.4)) 
        self.assertFalse(kmath.is_palindrome(4.5))
        self.assertTrue(kmath.is_palindrome(5))        
        self.assertFalse(kmath.is_palindrome(15))
        self.assertTrue(kmath.is_palindrome(66))
        self.assertTrue(kmath.is_palindrome(232))
        self.assertTrue(kmath.is_palindrome(1001))
        self.assertFalse(kmath.is_palindrome(1031))        
        
    def test_reduce_fraction(self):
        self.assertEqual(kmath.reduce_fraction(1920, 1080), (16, 9))
        self.assertEqual(kmath.reduce_fraction(120, 240), (1, 2))
        self.assertEqual(kmath.reduce_fraction(50, 60), (5, 6))
        self.assertEqual(kmath.reduce_fraction(10, 5), (2, 1))        

        
if __name__ == '__main__':
    unittest.main()