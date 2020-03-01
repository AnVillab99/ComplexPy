import unittest
import Complex as com
import Matrix as m


class TestComplexVector(unittest.TestCase):

    def testBooleanMatrix(self):
        m1 = m.crear(6,6,[False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False])
        
        v1 = m.crear(6,1,[6,2,1,5,3,10])
        r = m1.multiply(v1)
        R = m.crear(6,1,[0,0,12,5,1,9])
        self.assertTrue(r.equals(R))
    
    def testRendijaProbabilistica(self):
        m1=m.empty(12,12)
        m1.fix(1,0,1)
        m1.fix(2,1,1/3)
        m1.fix(3,1,1/3)
        m1.fix(4,1,1/3)
        m1.fix(5,2,1/3)
        m1.fix(6,2,1/3)
        m1.fix(7,2,1/3)
        m1.fix(7,3,1/3)
        m1.fix(8,3,1/3)
        m1.fix(9,3,1/3)
        m1.fix(9,4,1/3)
        m1.fix(10,4,1/3)
        m1.fix(11,4,1/3)



if __name__ == '__main__':
    unittest.main()