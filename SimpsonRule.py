#This program calculates and graphs the Simpson rule for approximating an integral

from matplotlib import pyplot as plt
from matplotlib.pyplot import xlabel, ylabel

l = []

def simp(h, x0, x):
    f_x0 = func(x0)
    f_x = func(x)

    m = (x-x0)/h
    s1 = sum1(m, h, x0)
    s2 = sum2(m, h, x0)

    s_g = f_x0 + f_x + s1 + s2

    s_erg = (h/6)*s_g

    return s_erg

def simpplot():
    x_val = [x[0] for x in l]
    y_val = [x[1] for x in l]

    plt.xticks([x*5 for x in range(20)])
    plt.plot(x_val, y_val)
    plt.ylim(80, 120)
    plt.ylabel("Integralarea", fontsize = 14, color = "red")
    plt.xlabel("1/h", fontsize = 14, color = "red")
    plt.show()


def sum1(m, h, x0):
    s = 0
    x0 = x0 + h
    for i in range(1, int(m)):
        f = func(x0)
        x0 = x0 + h
        s = s + f
    return 2*s

def sum2(m, h, x0):
    s = 0
    x0 = x0
    for i in range(0, int(m)):
        f = func((x0 + (h/2)))
        x0 = x0 + h
        s = s + f
    return 4*s

#The function for which the integral is calculated
def func(x):
    s = (1)/((x-0.5)*(x-0.5)+(1/1000))
    return s


for i in range(1, 101):
    g = simp(1/i, 0, 1)
    print("Approximation of the integral for h = {}/{}   : {}".format(1, i, g))
    l.append((i, g))

simpplot()
