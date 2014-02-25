from problems import Problems
import unittest

class TestEuler(unittest.TestCase):
    def test_001(self):
        self.assertEqual(Problems.problem_001(2, 3, 10), 32)
        self.assertEqual(Problems.problem_001(3, 5, 9), 14)
        self.assertEqual(Problems.problem_001(3, 5, 10), 23)
        
    def test_001_alt(self):
        self.assertEqual(Problems.problem_001_alt(2, 3, 10), 32)
        self.assertEqual(Problems.problem_001_alt(3, 5, 9), 14)
        self.assertEqual(Problems.problem_001_alt(3, 5, 10), 23)
    
    def test_002(self):
        self.assertEqual(Problems.problem_002(10), 10)
        self.assertEqual(Problems.problem_002(100), 44)
        
    def test_003(self):
        self.assertEqual(Problems.problem_003(100), 5)
        self.assertEqual(Problems.problem_003(13195), 29)
    
    def test_004(self):
        self.assertEqual(Problems.problem_004(1), 9)
        self.assertEqual(Problems.problem_004(2), 9009)        
        
    def test_005(self):
        self.assertEqual(Problems.problem_005(5), 60)
        self.assertEqual(Problems.problem_005(10), 2520)
        
    def test_006(self):
        self.assertEqual(Problems.problem_006(1), 1)       
        self.assertEqual(Problems.problem_006(10), 2640)
        
    def test_007(self):
        self.assertEqual(Problems.problem_007(1), 2)
        self.assertEqual(Problems.problem_007(2), 3)
        self.assertEqual(Problems.problem_007(3), 5)
        self.assertEqual(Problems.problem_007(4), 7)
        self.assertEqual(Problems.problem_007(5), 11)
        self.assertEqual(Problems.problem_007(6), 13)
        
    def test_008(self):
        self.assertEqual(Problems.problem_008(1, 1), 1)
        
    def test_009(self):
        self.assertEqual(Problems.problem_009(12), 60)
        self.assertEqual(Problems.problem_009(30), 780)        
        
    def test_010(self):
        self.assertEqual(Problems.problem_010(10), 17)
        self.assertEqual(Problems.problem_010(20), 77)
        
if __name__ == '__main__':
    unittest.main()