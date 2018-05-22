import unittest
import seuif97
from Region3h_pt2v import *

class Unittest_3h(unittest.TestCase):
    def setUp(self):
        print('start!')
        self.T0=273.15

        # IF97-dev,   p,   T,  v
        self.test3h=[[23.6,652,0.002651081407],
                     [24.0,654,0.002967802335]]

    def test_3h_pt2v(self):
        
         for item in  self.test3h:
                self.assertAlmostEqual(seuif97.pt2v(item[0], item[1]-self.T0),Backward3h_v_PT(item[0], item[1]))
                
    def test_in_region3h(self):   
         for item in  self.test3h:
                self.assertAlmostEqual(Backward3h_v_PT(item[0],item[1]),item[2])
   
    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Unittest_3h("test_3h_pt2v"))
    suite.addTest(Unittest_3h("test_in_region3h"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    