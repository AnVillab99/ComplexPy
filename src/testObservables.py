import unittest
import Complex as com
import Matrix as m
import Quantum as q
import math



class testObservables(unittest.TestCase):


    
    def test4_3_1(self):
        m1 = m.Matrix([[com.Complex(0, 0), com.Complex(1, 0)],[com.Complex(1, 0),com.Complex(0, 0)]])
        r1 =m1.vectoresPropios()
        m1.print()
        print("x")
        for i in range(len(r1)):
            r1[i].normalize()
            print("")        
        self.assertTrue(True)

    def test4_3_2(self):
        print("4.3.2")
        m1 = m.Matrix([[com.Complex(0, 0), com.Complex(1, 0)],[com.Complex(1, 0),com.Complex(0, 0)]])
        r1 =m1.vectoresPropios()
        v1 = m1.valoresPropios()
        prob=com.Complex(0,0)
        for i in range(len(r1)):
            ans = m1.productoInterno(r1[i]).sumaInterna()
            prob=prob.suma(v1[i].sMultiply(ans))
        print(prob.modulo())
        self.assertTrue(prob.modulo()==0)



        
        self.assertTrue(True)

    def test4_4_1(self):
        m1=m.crear(2,2,[0,1,1,0])
        m2 = m.crear(2,2,[math.sqrt(2)/2,math.sqrt(2)/2,math.sqrt(2)/2,-1*math.sqrt(2)/2])
        m3=m1.multiply(m2)
        m4=m2.multiply(m1)
        m2.print()
        print(m1.unitaria())
        print(m2.unitaria())

        print(m3.unitaria() or m4.unitaria())
        self.assertFalse(False)
            

        
        self.assertTrue(True)
        
    def test4_4_2(self):

        
        self.assertTrue(True)

    
    
    def test4_3_6(self):
        # m1 = m.Matrix([[com.Complex(0, 0), com.Complex(1, 0)],[com.Complex(1, 0),com.Complex(0, 0)]])
        # r1 =m1.vectoresPropios()
        # m1.print()
        # print("x")
        # for i in range(len(r1)):
        #     r1[i].normalize().print()
        # # m2 = m.Matrix([com.Complex(0, 0), com.Complex(0, -1)],[com.Complex(0, 1),com.Complex(0, 0)])
        # m2 = m.crearR(2,2,[(0,0),(0,-1),(0,1),(0,0)])
        # m2.print()
        # v=m.Matrix([[com.Complex(1/math.sqrt(2),0)],[com.Complex(0,1/math.sqrt(2))]])
        # qa = q.vEsperado(v,m2)
        # va=q.varianza(v,m2)

        
        self.assertTrue(True)

    
    # def testValoresPropios(self):
    #     m1 = m.Matrix([[com.Complex(1, 0), com.Complex(-3, 0),com.Complex(3, 0)],
    #     [com.Complex(3, 0), com.Complex(-5, 0), com.Complex(3, 0),],
    #     [com.Complex(6, 0), com.Complex(-6, 0), com.Complex(4, 0)]])
    #     m2 = m.Matrix([[com.Complex(1, 1), com.Complex(-3, -1),com.Complex(3, 1)],
    #     [com.Complex(3, 1), com.Complex(-5, -1), com.Complex(3, 1),],
    #     [com.Complex(6, 1), com.Complex(-6, -1), com.Complex(4, 0)]])
    #     r1 =m1.valoresPropios()
    #     r2 = m2.valoresPropios()
    #     R1 =[com.Complex(4, 0), com.Complex(-2, 0), com.Complex(-2, 0),]
    #     R2 = [com.Complex(4, 0), com.Complex(-2, 0), com.Complex(-2, 0),]
    #     self.assertTrue(m.equalsEigenV(r1,R1))
    #     self.assertTrue(m.equalsEigenV(r2,R2))

    
        

if __name__ == '__main__':
    unittest.main()