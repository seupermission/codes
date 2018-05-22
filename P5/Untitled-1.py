
import unittest
import seuif97

class Region3Test (unittest.TestCase):

    def setUp(self):
         self.T0=273.15

         # IF97-dev,Table33  Page 32 : p,t(K),h,s
         self.test3h=[ [0.255837018e2, 650, 0.1863430e4, 0.405427273e1],
                     [0.222930643e2, 650, 0.2375124e4, 0.485438792e1],
                     [0.783095639e2, 750, 0.2258688e10, 0.446971906e1]]
    def testSpecificEnthalpyPT(self):
        places = 6
        for item in  self.test3h:
            self.assertAlmostEqual(seuif97.pt(item[0], item[1]-self.T0,4),item[2],places)
    def testSpecificEntropyPT(self):
        places = 8
        for item in  self.tes3h:
            self.assertAlmostEqual(seuif97.pt(item[0], item[1]-self.T0,5),item[3],places)      

if __name__ == '__main__':
    unittest.main()       
    suite = unittest.TestSuite()
    suite.addTest(Region3Test("testSpecificEnthalpyPT"))
    suite.addTest(Region3Test("testSpecificEntropyPT"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)