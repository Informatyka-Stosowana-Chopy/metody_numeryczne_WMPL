

import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
import pandas as pd
import math

def get_diff_table(X,Y):
    """
         Get the market insert
    """
    n=len(X)
    A=np.zeros([n,n])
    
    for i in range(0,n):
        A[i][0] = Y[i]
    
    for j in range(1,n):
        for i in range(j,n):
            A[i][j] = (A[i][j-1] - A[i-1][j-1])/(X[i]-X[i-j])
    
    return A


def newton_interpolation(X,Y,x):
    """
         Calculate the interpolation of x points
    """
    sum=Y[0]
    temp=np.zeros((len(X),len(X)))
         # 
    for i in range(0,len(X)):
        temp[i,0]=Y[i]
    temp_sum=1.0
    for i in range(1,len(X)):
                 #x polynomial
        temp_sum=temp_sum*(x-X[i-1])
                 # 
        for j in range(i,len(X)):
            temp[j,i]=(temp[j,i-1]-temp[j-1,i-1])/(X[j]-X[j-i])
        sum+=temp_sum*temp[i,i] 
    return sum

f = open("")

# def liniowa(X)
# for _ range ()
#     Y.append(5*X[_]+3)

# Y=[-20,-12,1,15,4,21,41]
# A = get_diff_table(X,Y)
# df = pd.DataFrame(A)
# df

# xs=np.linspace(np.min(X),np.max(X),1000,endpoint=True)
# ys=[]
# for x in xs:
#     ys.append(newton_interpolation(X,Y,x))

# plt.title("newton_interpolation")
# plt.plot(X,Y,'s',label="original values")#blue dot indicates the original value
# plt.plot(xs,ys,'r',label='interpolation values')#Interpolation curve
# plt.xlabel('x')  
# plt.ylabel('y')  
# plt.legend(loc=4)# specifies the position of the legend in the lower right corner
# plt.show()







##################################################################################





# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([-1, 0, 1, 2]) # x coordinates in space
# y = np.array([1, 1, 2, 0]) # f(x)

# def getNDDCoeffs(x, y):
#     """ Creates NDD pyramid and extracts coeffs """
#     n = np.shape(y)[0]
#     pyramid = np.zeros([n, n]) # Create a square matrix to hold pyramid
#     pyramid[::,0] = y # first column is y
#     for j in range(1,n):
#         for i in range(n-j):
#             # create pyramid by updating other columns
#             pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
#     return pyramid[0] # return first row

# coeff_vector = getNDDCoeffs(x, y)
# print(coeff_vector)

# # ...
# # create as many polynomials as size of coeff_vector
# final_pol = np.polynomial.Polynomial([0.]) # our target polynomial
# n = coeff_vector.shape[0] # get number of coeffs
# for i in range(n):
#     p = np.polynomial.Polynomial([1.]) # create a dummy polynomial
#     for j in range(i):
#         # each vector has degree of i
#         # their terms are dependant on 'x' values
#         p_temp = np.polynomial.Polynomial([-x[j], 1.]) # (x - x_j)
#         p = np.polymul(p, p_temp) # multiply dummy with expression
#     p *= coeff_vector[i] # apply coefficient
#     final_pol = np.polyadd(final_pol, p) # add to target polynomial

# p = np.flip(final_pol[0].coef, axis=0)
# print(p)

# # ...
# # Evaluate polynomial at X axis and plot result
# x_axis = np.linspace(0, 10, num=5000)
# y_axis = np.polyval(p, x_axis)

# plt.plot(x_axis, y_axis)
# plt.show()







##################################################################################








# from copy import copy
# from math import pi
#
# print("----Zadanie 3 ----")
#
# ####################################
# # CONSTANT
# ####################################
# wezel_przykladowy = [-2, -1, 0, 2, 4]
# y_przykladowy = [-1, 0, 5, 99, -55]
# rzad = []  # tutaj będą zapisywane tablice w każdym rzędzie i rząd[i] to będzie tablica
# x_global = []
# y_global = []
#
#
# ####################################
# # FUNCTIONS
# ####################################
# def wczytaj_wezel():
#     # to potem (może)
#     x_global.append(input("Podaj pierwszy węzeł: "))
#
#
# def funkcja_wielomianowa(x, y, n):  # x, y - wiadomo n - ilość węzłów
#     # interpolacyjny
#     pom = []
#     global rzad
#     # dla 1 rzędu
#     for i in range(n - 1):
#         pom.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
#     rzad.append(copy(pom))
#     pom.clear()
#     # dla kolejnych rzędów
#     for _ in range(n - 2):
#         for i in range(n - 2 - _):
#             pom.append((rzad[_][i + 1] - rzad[_][i]) / (x[i + 2 + _] - x[i]))
#         rzad.append(copy(pom))
#         pom.clear()
#
#     # wypisanie wyniku
#     s = f"W(x) = {y[0]}"
#     f = f""
#     for i in range(n - 1):
#         for j in range(i + 1):
#             if x[j] < 0:
#                 f += f"(x + {abs(x[j])})"
#             else:
#                 f += f"(x - {x[j]})"
#
#         s += f" + {rzad[i][0]}{copy(f)}"
#         f = f""
#
#     return s
#
#
# def funckja_liniowa(x):
#     pass
#
#
# def funkcja_trygonometryczna(n):
#     if n % 2 == 0:
#         p = 0.5 * n
#     else:
#         p = 0.5 * (n - 1)
#
#     a = []
#     b = []
#
#     for k in range(n):
#         x_global.append((2 * k * pi) / (n + 1))
#
#     for i in range(p):
#         a.append((2 / (n + 1)) * sum())
#         if i > 0:
#             b.append(2 / (n + 1))  # TODO
#
#
# def funkcja_modul(x):
#     pass
#
#
# ####################################
# # MAIN
# ####################################
# # print(funkcja_wielomianowa(wezel_przykladowy, y_przykladowy))
# funkcja_trygonometryczna(4)
