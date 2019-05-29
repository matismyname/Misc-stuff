#This program calculates and plots a mean-variance function for a portfolio
#The idea is based upon the work of Markowitz

from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel, ylabel
from math import *

def calc(m1, s1, m2, s2, r12):
    l = []
    mpf = 0
    spf = 0
    minvar = 0
    omega = 0
    #Caclulates all the mean-variance points ((x, y) points) for each omega += 0.01 starting from 0
    for i in range(100):
        mpf = omega*m1+(1-omega)*m2
        spf = (omega*omega*s1*s1)+(1-omega)*(1-omega)*s2*s2+2*omega*(1-omega)*s1*s2*r12
        spf = sqrt(spf)
        minvar = 2*omega*s1*s1-s2*s2+(2-4*omega)*s1*s2*r12
        l.append((spf, mpf, omega, minvar))
        omega += 0.01

    return l

g = calc(0.04, 0.03, 0.06, 0.05, 0.2)
x_val = [x[0] for x in g]
y_val = [x[1] for x in g]
plt.plot(x_val, y_val)
plt.ylabel("Mean", fontsize = 14, color = "red")
plt.xlabel("Variance", fontsize = 14, color = "red")
plt.show()