import unittest
import kmath

class TestKMath(unittest.TestCase):
    def test_factorial(self):
        f = kmath.factorial
        self.assertRaises(ValueError, f, -1)
        self.assertEqual(f(0), 1)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 2)
        self.assertEqual(f(3), 6)
        self.assertEqual(f(4), 24)
        self.assertRaises(ValueError, f, 4.5)
        self.assertEqual(f(5), 120)
        self.assertEqual(f(6), 720)
        self.assertEqual(f(7), 5040)
        self.assertEqual(f(8), 40320)
        self.assertEqual(f(9), 362880)
        self.assertEqual(f(10), 3628800)
        
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
    
    def test_GCF(self):
        f = kmath.GCF
        self.assertEqual(f(1920, 1080), 120)
        self.assertEqual(f(120, 240), 120)
        self.assertEqual(f(50, 60), 10)
        self.assertEqual(f(10, 5), 5)
    
    def test_get_largest_prime_factor(self):
        f = kmath.get_largest_prime_factor
        self.assertEqual(f(28), 7)
        self.assertEqual(f(29), 29)
        self.assertEqual(f(100), 5)
        self.assertEqual(f(13195), 29)
       
    def test_get_n_digits(self):
        f = kmath.get_n_digits
        self.assertEqual(f(-100), 3)
        self.assertEqual(f(0), 1)
        self.assertEqual(f(99), 2)    
        
    def test_get_nth_fibonacci(self):
        f = kmath.get_nth_fibonacci
        self.assertRaises(ValueError, f, 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertRaises(ValueError, f, 4.5)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(6), 8)
        self.assertEqual(f(7), 13)
        self.assertEqual(f(8), 21)
        self.assertEqual(f(9), 34)
        self.assertEqual(f(10), 55)
 
    def test_get_smallest_prime_factor(self):
        f = kmath.get_smallest_prime_factor
        self.assertEqual(f(28), 2)
        self.assertEqual(f(29), 29)
        self.assertEqual(f(100), 2)
        self.assertEqual(f(13195), 5)
     
    def test_is_palindrome(self):
        f = kmath.is_palindrome
        self.assertFalse(f(-1))
        self.assertTrue(f(0))
        self.assertTrue(f(4.4)) 
        self.assertFalse(f(4.5))
        self.assertTrue(f(5))
        self.assertFalse(f(15))
        self.assertTrue(f(66))
        self.assertTrue(f(232))
        self.assertTrue(f(1001))
        self.assertFalse(f(1031))
    
    def test_is_phone_number(self):
        test_cases = ('800-555-1212',
                      '800 555 1212',
                      '800.555.1212',
                      '(800) 555-1212',
                      '1-800-555-1212',
                      '80055512121234',
                      '800-555-1212-1234',
                      '800-555-1212x1234',
                      '800-555-1212 ext. 1234',
                      'work 1-(800) 555.1212 #1234')
        for test_case in test_cases:
            self.assertTrue(kmath.is_phone_number(test_case))

    def test_is_prime(self):
        f = kmath.is_prime
        self.assertRaises(ValueError, f, -1)
        self.assertFalse(f(0))
        self.assertFalse(f(1))
        self.assertTrue(f(2))
        self.assertTrue(f(3))
        self.assertFalse(f(4))
        self.assertRaises(ValueError, f, 4.5)
        self.assertTrue(f(5))
        self.assertFalse(f(6))
        self.assertTrue(f(7))
        self.assertFalse(f(8))
        self.assertFalse(f(9))
        self.assertFalse(f(10))
        self.assertTrue(f(11)) 
        
    def test_is_roman(self):
        f = kmath.is_roman
        self.assertFalse(f('MMDMCLIXV'))
        self.assertTrue(f('MMMDCCCLXXXVIII'))
        
    def test_LCM(self):
        f = kmath.LCM
        self.assertEqual(f(3, 4), 12)
        self.assertEqual(f(4, 6), 12)
        self.assertEqual(f(6, 8), 24)
        self.assertEqual(f(8, 12), 24)
        self.assertEqual(f(12, 15), 60)
        self.assertEqual(f(15, 20), 60)
        self.assertEqual(f(20, 30), 60)
                          
    def test_reduce_fraction(self):
        f = kmath.reduce_fraction
        self.assertEqual(f(1920, 1080), (16, 9))
        self.assertEqual(f(120, 240), (1, 2))
        self.assertEqual(f(50, 60), (5, 6))
        self.assertEqual(f(10, 5), (2, 1))
                   
    def test_to_roman(self):
        test_cases = ((1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (31, 'XXXI'),
                     (50, 'L'),
                     (100, 'C'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (500, 'D'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1000, 'M'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))
        for integer, numeral in test_cases:
            self.assertEqual(kmath.to_roman(integer), numeral)            
        
if __name__ == '__main__':
    unittest.main()