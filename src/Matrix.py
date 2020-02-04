import sys
import math
import Complex as com
#import numpy as np

class Matrix:
    def __init__(self,m):
        self.m= m # la matriz
        self.I=len(m) #imaginaro
        self.J=len(m[0])

    # Este metodo devuelve la suma de esta matriz con la matriz dada
    # @param b Matrix otra matriz
    # @return Matrix la suma de las matrices
    def suma(self,b):

        if (self.I!= b.I or self.J != b.J):
            raise ValueError("Error en dimensiones de las matrices")
            sys.exit()

        r=[[com.Complex(0,0) for x in range (self.J)] for y in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                r[i][j]=self.m[i][j].suma(b.m[i][j])
        return Matrix(r)

    # Este metodo devuelve la resta de esta matriz con la matriz dada
    # @param b Matrix otra matriz
    # @return Matrix la resta de las matrices
    def resta(self,b):
        if (self.I!= b.I or self.J != b.J):
            raise ValueError("Error en dimensiones de las matrices")
            sys.exit()
        r=[[com.Complex(0,0) for x in range (self.J)] for y in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                r[i][j]=self.m[i][j].resta(b.m[i][j])
        return Matrix(r)


    # Este metodo devuelve la multiplicacion (producto cruz) de esta matriz o vector con la matriz o vector dado
    # @param b Matrix/vector otra matriz
    # @return Matrix la multiplicacion de las matrices
    def multiply(self,b):
        if(self.J==1 and b.J==1 and self.I == b.I):
            print(b.I)
            print(b.J)
            r =com.Complex(0,0)
            for i in range(self.I):
                for j in range(self.J):

                    r=r.suma(self.m[i][j].multiply(b.m[i][j]))
            return r
        elif(self.J == b.I):
            p = [[com.Complex(0,0) for i in range(b.J)] for j in range(self.I)]
            for i in range(self.I):
                for j in range(b.J):

                    sum=com.Complex(0,0)
                    for z in range(self.J):
                        sum=sum.suma(self.m[i][z].multiply(b.m[z][j]))

                    p[i][j]=sum

            return Matrix(p)
        else:
            raise ValueError("Error en dimensiones de las matrices")
            sys.exit()


    # Este metodo devuelve la matriz inversa de la matriz actual
    # @return matrix la inversa
    def inverse(self):
        p = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                p[i][j] =self.m[i][j].inversa()
        return Matrix(p)

    # Este metodo devuelve la transpuesta de la la matriz actual
    # @return matrix la transpuesta
    def transpuesta(self):
        p = [[com.Complex(0,0) for i in range(self.I)] for j in range(self.J)]
        for i in range(self.I):
            for j in range(self.J):
                p[j][i] =self.m[i][j]
        return Matrix(p)


    # Este metodo devuelve la matriz conjugada de la matriz actual
    # @return MAtrix la conjugada
    def conjugada(self):
        p = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                p[i][j] =self.m[i][j].conjugado()
        return Matrix(p)

    # Este metodo devuelve la matriz adjunta (conjugda y transpuesta) de la matriz actual
    # @return MAtrix la adjunta
    def adjunta(self):
        return self.transpuesta().conjugada()

    # Este metodo devuelve la traza de una matriz, la matriz debe ser cuadrada
    # @return Complex la traza de esta matriz
    def trace(self):
        if(self.I!=self.J):
            raise ValueError("Matriz no cuadrada")
        r=com.Complex(0,0)
        for i in range (self.I):
            r=r.suma(self.m[i][i])
        return r

    # Este metodo devuelve la norma de esta matriz sqrt(Traza(At*A))
    # @return double la norma de la matriz
    def norma(self):
        c =self.adjunta()
        d = c.multiply(self)
        return round(math.sqrt(d.trace().real),4)

    # Este metodo devuelve la distancia entre 2 matrices
    # @return double la distancia entre las matrices
    def distancia(self,b):
        return (self.resta(b).norma())


    # Este metodo devuelve un booleano indicando si esta matriz es unitaria (A*At=I)
    # @return boolean Indica si esta matriz es unitaria
    def unitaria(self):
        c = self.multiply(self.adjunta())
        for i in range (c.I):
            for j in range(c.J):
                if (i==j and (c.m[i][j].real!=1 or c.m[i][j].imag!=0 )):
                    return False
                elif(i!=j and (c.m[i][j].real!=0 or c.m[i][j].imag!=0)):
                    return False
        return True

    # Este metodo devuelve un booleano indicando si esta matriz es hermetian (A=At)
    # @return boolean Indica si esta matriz es hermetian
    def hermetian(self):
        if(self.I!=self.J):
            return False
        d = self.adjunta()
        for i in range(self.I):
            for j in range(self.J):
                if ( self.m[i][j].real!= d.m[i][j].real or self.m[i][j].imag!= d.m[i][j].imag):
                    return False
        return True

    def multiplyS(self,d):
        k = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                k[i][j]=self.m[i][j].sMultiply(d)
        return Matrix(k)


    def escalarMultiply(self,c):
        k = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                k[i][j]=self.m[i][j].multiply(c)
        return Matrix(k)

    # Este metodo devuelve el producto tensor entre 2 matrices
    # @param la otra matriz
    # @return Matrix el producto tensor
    def productoTensor(self,b):
        I2 = b.I
        J2 = b.J
        tpc =  [[com.Complex(0,0) for i in range(self.J*J2)] for j in range(self.I*I2)]
        g=0
        h=0
        for i in range(self.I):
            for j in range(self.J):
                r = b.escalarMultiply(self.m[i][j])
                tpc=self.llenar(tpc,r,g,h)
                h+=1
            h=0
            g+=1
        return Matrix(tpc)

    #filler es matriz, og no
    def llenar(self,og,filler,vecesI,vecesJ):
        iF = filler.I;
        jF = filler.J;
        inicialI = iF*vecesI; #la fila desde donde se comenzara a llenar la og
        inicialJ = jF*vecesJ; # la columna desde donde se comenzara a llenar la og
        itI =0;
        itJ =0;
        for a in range(inicialI,inicialI+iF):
            for b in range(inicialJ,inicialJ+jF):
                og[a][b]=filler.m[itI][itJ]
                itJ=itJ+1
            itJ=0
            itI=itI+1
        return og




        # def vectorPropio(self):
        #     r  = [[0 for i in range(self.J)] for j in range(self.I)]
        #     i = [[0 for i in range(self.J)] for j in range(self.I)]
        #     for i in range(self.I):
        #         for j in range(self.J):
        #             r[i][j]=self.m[i][j].real
        #             i[i][j] = self.m[i][j].imag
        #     R =1j*i
        #     R+=r
        #     r2 =np.vectorize(complex)(r, i)
        #     k = np.linalg.eig(r2)
        #     k2 = np.linalg.eig(r,R)
        #     print(k2)
            














    def print(self):
        s = ""
        for i in range(0,self.I):
            for j in range(0,self.J):
                s+=self.m[i][j].printS()
            print(s)
            s=""


    def equals(self,b):
        if (self.I!= b.I or self.J != b.J):
            raise ValueError("Matriz dada es de dimensiones erradas")
            sys.exit()
        for i in range(self.I):
            for j in range(self.J):
                if(self.m[i][j].real != b.m[i][j].real or self.m[i][j].imag != b.m[i][j].imag):
                    return False
                    sys.exit()
        return True






