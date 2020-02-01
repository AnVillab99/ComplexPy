import sys
import math
import Complex as Complex

class Matrix:
    def __init__(self,m): 
        self.m= m # la matriz
        self.I=len(m) #imaginaro
        self.J=len(m[0])


    def suma(self,b):
        if (self.I!= len(b) or self.J != len(b[0])):
            
            


    def print(self):
        s = ""
        for i in range(0,self.I):
            for j in range(0,self.J):
                s+=self.m[i][j].printS()
            print(s)
            s=""

                                
                
    

    
