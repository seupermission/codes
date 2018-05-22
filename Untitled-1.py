import unittest
from math import log

import Region3h_pt2v

#from Region3h import *



class Region3h_pt2v():

    def __init__(self, P, T):
        """
        Parameters
        ----------
        T : float
            Temperature [K]
        P : float
            Pressure [MPa]
        V : float
            Specific volume [m³/kg]
        region : char
            Region 3 subregion code
       
        References
        ----------
        """
        self.P = P
        self.T = T
        self.V = None
        self.region = None
        
        
    def _P23_T(self):
        """Define the boundary between Region 2 and 3, P=f(T)
        """

        n = [0.34805185628969e3, -0.11671859879975e1, 0.10192970039326e-2]

        return n[0]+n[1]*self.T+n[2]*self.T**2


    def _tab_P(self):
        """Define the boundary between Region 3g-3h, T=f(P)
        """
        I = [0, 1, 2, 3 ,4]
        n = [-0.249284240900418e5, 0.428143584791546e4, -0.269029173140130e3,
             0.751608051114157e1, -0.787105249910383e-1]

        Pr = self.P/1
        T = 0
        for i, ni in zip(I, n):
            T += ni * log(Pr)**i
        return T


    def _Backward3h_v_PT(self):
        """Backward equation for region 3, v=f(P,T)        
        """
        if self.P > 25 and self.T >= self._tab_P() and self.P >= self._P23_T():
            self.region = "h"
        else:
            raise NotImplementedError("Incoming out of 3h-region")

        return self._Backward3h_v_PT()


    def _Backward3h_v_PT(self):
        """Backward equation for region 3h, v=f(P,T)
        """
        par = [0.0032, 25, 660, 0.898, 0.983, 1, 1, 4]

        I = [-12, -12, -10, -10, -10, -10, -10, -10, -8, -8, -8, -8, -8, -6, -6,
             -6, -5, -5, -5, -4, -4, -3, -3, -2, -1, -1, 0, 1, 1, ]

        J = [8, 12, 4, 6, 8, 10, 14, 16, 0, 1, 6, 7, 8, 4, 6, 8, 2, 3, 4, 2, 4,
             1, 2, 0, 0, 2, 0, 0, 2]

        n = [0.561379678887577e-1, 0.774135421587083e10, 0.111482975877938e-8,
             -0.143987128208183e-2, 0.193696558764920e4, -0.605971823585005e9,
             0.171951568124337e14, -0.185461154985145e17, 0.387851168078010e-16,
             -0.395464327846105e-13, -0.170875935679023e3, -0.212010620701220e4,
             0.177683337348191e8, 0.110177443629575e2, -0.234396091693313e6,
             -0.656174421999594e7, 0.156362212977396e-4, -0.212946257021400e1,
             0.135249306374858e2, 0.177189164145813, 0.139499167345464e4,
             -0.703670932036388e-2,-0.152011044389648, 0.98191692299113e-4,
             0.147199658618076e-2, 0.202618487025578e2, 0.899345518944240,
             -0.211346402240858,0.249971752957491e2]

        v_, P_, T_, a, b, c, d, e = par

        Pr = self.P/P_
        Tr = self.T/T_
        suma = 0
        for i, j, ni in zip(I, J, n):
            suma += ni * (Pr-a)**(c*i) * (Tr-b)**(j*d)
            
        self.V = v_*suma**e 
        return v_*suma**e


if __name__ == '__main__':
    a = Region3h_pt2v(24,654)
    a._Backward3h_v_PT()
    print(a.P, a.T, a.V, a.region)


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
        self.assertAlmostEqual(self.V[0],0.002651081407)
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
