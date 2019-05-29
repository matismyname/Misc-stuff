#This program calculates the fibonacci numbers up to steps

#lru_cache caches the previously calculated results up to a maxsize of 1000
#If that isn't done, then this programm would be slow because the fib function has to call itself over and over and over...
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

steps = 100
for i in range(1,steps+1):
    print("Fibonacci number {}: {}".format(i, fib(i)))