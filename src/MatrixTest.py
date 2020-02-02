import unittest
import Complex as com
import Matrix as m


class TestComplexMatrix(unittest.TestCase):

    def testSumaMatriz(self):
        v1 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)], [com.Complex(1, 2), com.Complex(1, 1)]])
        v2 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)], [com.Complex(1, 2), com.Complex(1, 1)]])
        s  = m.Matrix([[com.Complex(2, 2), com.Complex(2, 2)], [com.Complex(2, 4), com.Complex(2, 2)]])
        p = v1.suma(v2)
        
        self.assertTrue(s.equals(p))

    def testInversaMatriz(self):
        v1 = m.Matrix([[com.Complex(1.5, 1), com.Complex(10, -11)], [com.Complex(1, 2.3), com.Complex(-1, 1)]])

        s = m.Matrix([[com.Complex(-1.5, -1), com.Complex(-10, 11)], [com.Complex(-1, -2.3), com.Complex(1, -1)]])
        p = v1.inverse()
        self.assertTrue(p.equals(s))

    def testMatrixMultiply(self):
        v1 = m.Matrix( [[com.Complex(1, 0), com.Complex(0, 0)], [com.Complex(1, 0), com.Complex(0, 0)]])
        v2 = m.Matrix( [[com.Complex(1, 2), com.Complex(2, 1)], [com.Complex(1, 3), com.Complex(3, 1)]])
        s =  m.Matrix([[com.Complex(1, 2), com.Complex(2, 1)], [com.Complex(1, 2), com.Complex(2, 1)]])
        p = v1.multiply(v2)
        self.assertTrue(p.equals(s))
        try:
            v1 = m.Matrix( [[com.Complex(1, 0), com.Complex(0, 0)], [com.Complex(1, 0), com.Complex(0, 0)]])
            v2 = m.Matrix( [[com.Complex(1, 2), com.Complex(2, 1)], [com.Complex(1, 3), com.Complex(3, 1)],[com.Complex(1, 3), com.Complex(3, 1)]])
        except ValueError as e:
            self.assertEqual(e,"Error en dimensiones de las matrices")

    
    def testMultiplicacionMatrices(self):
        try:
            v1 = m.Matrix([[com.Complex(1, 1),com.Complex(-2,1.6)], [com.Complex(-4.8,5),com.Complex(1, 5)]])
            v2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
            c = m.Matrix([[com.Complex(-8.8,1.2)],[com.Complex(-32.6,13.4)]])
            s = v1.multiply(v2)
            self.assertTrue(c.equals(s))
            v1 = m.Matrix([[com.Complex(1, 1),com.Complex(-2,1.6)], [com.Complex(-4.8,5),com.Complex(1, 5)]])
            v2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
            s = v1.multiply(v2)

        except ValueError as e:
            self.assertEqual(e,"Error en dimensiones de las matrices")
    def testMatrizTranspuesta(self):
        v2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
        v1  = m.Matrix([[com.Complex(2, 2), com.Complex(2,3)]])
        s =v2.transpuesta()
        self.assertTrue(s.equals(v1))



    # def test_matrix_transpose(self):
    #     m = [[com.Complex(6, -3), com.Complex(2, 12), com.Complex(0, -19)], [
    #         com.Complex(0, 0), com.Complex(5, 2.1), com.Complex(17, 0)], [
    #         com.Complex(1, 0), com.Complex(2, 5), com.Complex(3, -4)]]
    #     s = [[com.Complex(6, -3), com.Complex(0, 0), com.Complex(1, 0)], [
    #         com.Complex(2, 12), com.Complex(5, 2.1), com.Complex(2, 5)], [
    #         com.Complex(0, -19), com.Complex(17, 0), com.Complex(3, -4)]]
    #     p = Matrix.transpose(m)
    #     for i in range(len(p)):
    #         for j in range(len(p[0])):
    #             self.assertEqual(s[i][j].real, p[i][j].real)
    #             self.assertEqual(s[i][j].imag, p[i][j].imag)

    # def test_matrix_conjugate(self):
    #     m = [[com.Complex(6, -3), com.Complex(2, 12), com.Complex(0, -19)], [
    #         com.Complex(0, 0), com.Complex(5, 2.1), com.Complex(17, 0)], [
    #         com.Complex(1, 0), com.Complex(2, 5), com.Complex(3, -4)]]
    #     s = [[com.Complex(6, 3), com.Complex(2, -12), com.Complex(0, 19)], [
    #         com.Complex(0, 0), com.Complex(5, -2.1), com.Complex(17, 0)], [
    #         com.Complex(1, 0), com.Complex(2, -5), com.Complex(3, 4)]]
    #     p = Matrix.conjugate(m)
    #     for i in range(len(p)):
    #         for j in range(len(p[0])):
    #             self.assertEqual(s[i][j].real, p[i][j].real)
    #             self.assertEqual(s[i][j].imag, p[i][j].imag)

  


    # def test_matrix_adjoint(self):
    #     m = [[com.Complex(6, -3), com.Complex(2, 12), com.Complex(0, -19)], [
    #         com.Complex(0, 0), com.Complex(5, 2.1), com.Complex(17, 0)], [
    #         com.Complex(1, 0), com.Complex(2, 5), com.Complex(3, -4)]]
    #     s = [[com.Complex(6, 3), com.Complex(0, 0), com.Complex(1, 0)], [
    #         com.Complex(2, -12), com.Complex(5, -2.1), com.Complex(2, -5)], [
    #         com.Complex(0, 19), com.Complex(17, 0), com.Complex(3, 4)]]
    #     p = Matrix.adjoint(m)
    #     for i in range(len(p)):
    #         for j in range(len(p[0])):
    #             self.assertEqual(s[i][j].real, p[i][j].real)
    #             self.assertEqual(s[i][j].imag, p[i][j].imag)

    # def test_matrix_norm(self):
    #     m = [[com.Complex(3, 0), com.Complex(5, 0)], [
    #         com.Complex(2, 0), com.Complex(3, 0)]]
    #     s = math.sqrt(47)
    #     p = Matrix.norm(m)
    #     self.assertEqual(s, p)

    # def test_matrix_distance(self):
    #     m1 = [[com.Complex(3, 0), com.Complex(5, 0)], [
    #         com.Complex(2, 0), com.Complex(3, 0)]]
    #     m2 = [[com.Complex(0, 0), com.Complex(1, 0)], [
    #         com.Complex(-1, 0), com.Complex(0, 0)]]
    #     s= com.Complex(6.557438524302, 0.0)
    #     p= Matrix.distance(m1,m2)
    #     self.assertEqual(s.real,p.real)
    #     self.assertEqual(s.imag,p.imag)

    # def test_matrix_unitary(self):
    #     m = [[com.Complex(1/2, 1/2), com.Complex(0, 1/(math.sqrt(3))), com.Complex(3/(2*math.sqrt(15)), 1/(2*math.sqrt(15)))], [
    #         com.Complex(-1/2, 0), com.Complex(1/(math.sqrt(3)), 0), com.Complex(4/(2*math.sqrt(15)), 3/(2*math.sqrt(15)))], [
    #         com.Complex(1/2, 0), com.Complex(0, -1/(math.sqrt(3))), com.Complex(0, 5/(2*math.sqrt(15)))]]
    #     p = Matrix.unitary(m)
    #     self.assertTrue(p)

    # def test_matrix_hermitian(self):
    #     m = [[com.Complex(5, 0), com.Complex(4, 5), com.Complex(6, -16)], [
    #         com.Complex(4, -5), com.Complex(13, 0), com.Complex(7, 0)], [
    #         com.Complex(6, 16), com.Complex(7, 0), com.Complex(-2.1, 0)]]
    #     p = Matrix.hermitian(m)
    #     self.assertTrue(p)

    # def test_matrix_tensorProduct(self):
    #     a = [[com.Complex(3, 0), com.Complex(2, 0)], [
    #         com.Complex(-1, 0), com.Complex(0, 0)]]
    #     b = [[com.Complex(6, 0), com.Complex(5, 0)], [
    #         com.Complex(3, 0), com.Complex(2, 0)]]
    #     s = [[com.Complex(18, 0), com.Complex(15, 0), com.Complex(12, 0), com.Complex(10, 0)], [
    #         com.Complex(9, 0), com.Complex(6, 0), com.Complex(6, 0), com.Complex(4, 0)], [
    #         com.Complex(-6, 0), com.Complex(-5, 0), com.Complex(0, 0), com.Complex(0, 0)], [
    #         com.Complex(-3, 0), com.Complex(-2, 0), com.Complex(0, 0), com.Complex(0, 0)]]
    #     p = Matrix.tensorProduct(a, b)
    #     for i in range(len(s)):
    #         for j in range(len(s[0])):
    #             self.assertEqual(s[i][j].real, p[i][j].real)
    #             self.assertEqual(s[i][j].imag, p[i][j].imag)


if __name__ == '__main__':
    unittest.main()