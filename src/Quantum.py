import sys
import math
import Complex as com
import sympy as sp
import fractions
import matplotlib.pyplot as plt
import Matrix as m

"""Dado un ket (vector) v, cual es la probabilidad de hallar una particula en i"""
def probParticle(v,p):
    ket = v.m
    sumatoria = 0
    for i in range(v.I):
        for j in range(v.J):
            sumatoria=sumatoria+(math.pow(ket[i][j].modulo(),2))
    
    if (v.I ==1):
        posc = math.pow(ket[0][p].modulo(),2)
    if (v.J ==1):
        posc = math.pow(ket[p][0].modulo(),2)
    return posc/sumatoria

def amplitudDeTransicion(a,b):
    a = a.normalize()
    b = b.normalize()
    r =b.productoInterno(a).m[0][0]
    d = a.norma()*b.norma()
    return r.sDivide(d)

def identidadEsperada(I,es):
    id = m.identidad(I)
    for i in range(I):
        id.m[i][i]=id.m[i][i].multiply(es)
    return id
