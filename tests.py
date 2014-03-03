from problems import Problems
import unittest

class TestEuler(unittest.TestCase):
    def test_001(self):
        f = Problems._001
        self.assertEqual(f(2, 3, 10), 32)
        self.assertEqual(f(3, 5, 9), 14)
        self.assertEqual(f(3, 5, 10), 23)
        
    def test_001_alt(self):
        f = Problems._001_alt
        self.assertEqual(f(2, 3, 10), 32)
        self.assertEqual(f(3, 5, 9), 14)
        self.assertEqual(f(3, 5, 10), 23)
    
    def test_002(self):
        f = Problems._002
        self.assertEqual(f(10), 10)
        self.assertEqual(f(100), 44)
        
    def test_003(self):
        f = Problems._003
        self.assertEqual(f(28), 7)
        self.assertEqual(f(29), 29)
        self.assertEqual(f(100), 5)
        self.assertEqual(f(13195), 29)
    
    def test_004(self):
        f = Problems._004
        self.assertEqual(f(1), 9)
        self.assertEqual(f(2), 9009)        
        
    def test_005(self):
        f = Problems._005
        self.assertEqual(f(5), 60)
        self.assertEqual(f(10), 2520)
        
    def test_006(self):
        f = Problems._006
        self.assertEqual(f(1), 1)       
        self.assertEqual(f(10), 2640)
        
    def test_007(self):
        f = Problems._007
        self.assertEqual(f(1), 2)
        self.assertEqual(f(2), 3)
        self.assertEqual(f(3), 5)
        self.assertEqual(f(4), 7)
        self.assertEqual(f(5), 11)
        self.assertEqual(f(6), 13)
        
    def test_008(self):
        f = Problems._008
        self.assertEqual(f(1, 1), 1)
        self.assertEqual(f(299792458, 2), 81)       # speed of light
        self.assertEqual(f(149597870700, 3), 504)   # astronomical unit
        
    def test_009(self):
        f = Problems._009
        self.assertEqual(f(12), 60)
        self.assertEqual(f(30), 780)
        self.assertEqual(f(56), 4200)
        
    def test_010(self):
        f = Problems._010
        self.assertEqual(f(10), 17)
        self.assertEqual(f(20), 77)
        
if __name__ == '__main__':
    unittest.main()