import unittest
import Complex as com
import Matrix as m
import Quantum as q
import math

class QuantumTest(unittest.TestCase):

    
    def testNormalizar(self):
        v1 = m.Matrix([[com.Complex(2, -3), com.Complex(1, 2)]])
        v2 = v1.normalize()

    def testHallarParticulaProb(self):
        v1 = m.crearR(1,2,[(3,-4),(7,2)])

    


    def testQuiz3_1(self):
        v=m.crearR(10,1,[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)])
        print(q.probParticle(v,7))
        for i in range(10):
            print(" p"+str(i)+" :"+str(q.probParticle(v,i)))
        v2 =m.crearR(10,1,[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)])
        print("------")
        print("amp trans : "+str(q.amplitudDeTransicion(v,v2).printS()))
        
        m1 = m.crearR(2,2,[(2,0),(1,1),(1,-1),(3,0)])
        v3 = m.crearR(2,1,[(1/math.sqrt(2),0),(0,1/math.sqrt(2))])
        v3m= m1.multiply(v3)
        vEsperado=v3m.productoInterno(v3).m[0][0]
        iEsp = q.identidadEsperada(2,vEsperado)
        delta = m1.resta(iEsp)
        dfo = delta.multiply(delta)
        varianzaIzq=dfo.multiply(v3)
        var = varianzaIzq.productoInterno(v3)
        var.print()

        






if __name__ == '__main__':
    unittest.main()