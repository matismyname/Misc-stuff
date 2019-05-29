#This program calculates the fibonacci numbers up to steps

def main():
    #steps = input("How many steps? ")
    steps = 100
    fib_nums = fibonacci(steps)
    i = 1
    for e in fib_nums:
        print("Fibonacci number {}: {}".format(i,e))
        i += 1

def fibonacci(steps):
    fibs = [1,1]
    steps -= 2
    a = 0
    b = 1
    while steps > 0:
        fibs.append(fibs[b] + fibs[a])
        a += 1
        b += 1
        steps -= 1
    
    return fibs

if __name__ == "__main__":
    main()