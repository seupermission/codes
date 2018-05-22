
import unittest
import Region3h_pt2v

class Unittest_3h(unittest.TestCase):
    def setUp(self):
        print('start!')
        self.P = (23.6,24)
        self.T = (652,654)
        self.V = ()
 
    def test_3h_pt2v(self):
        print('test1')

        self.V = (Region3h_pt2v(self.P[0],self.T[0])._Backward3h_v_PT(),
                  Region3h_pt2v(self.P[1],self.T[1])._Backward3h_v_PT())
        self.assertAlmostEqual(self.V[0],0.00265081407)
        self.assertAlmostEqual(self.V[1],0.002967802335)
    
    def test_inregion3h(self):
        self.P = (23.6,24)
        self.T = (652,654)
        print('test2')
        try:
            Region3h_pt2v(self.P[0],self.T[0])._Backward3h_v_PT()
        except Exception as e:
            print('RegionError:',e)
        
        try:
            Region3h_pt2v(self.P[1],self.T[1])._Backward3h_v_PT()
        except Exception as e:
            print('RegionError:',e)

    
    
if __name__ == '__main__':
    unittest.main() 