def main():
    p = 10      #Up until which number starting from 0 you want to "test" the Collatz Conjecture
    a = 2       #Starting number, 0 and 1 are trivial
    s = 0       #Variable which checks the number of elements in the dictionary d
    l = 0       #Saves the whole number for which the most steps are needed until 1
    d = []      #Saves the number of steps taken for the number a

    while a < p:
        n = a
        #print("{}.) ".format(a), end = " ")            #Uncomment this if you want to print out each step for each number
        while n > 1:
            if(n%2==0):
                #print("{}".format(int(n)), end=" ")    #Uncomment this if you want to print out each step for each number
                n = n/2
                d.append(n)

                #Adds 1 to the dic
                if(n==1):
                    #print("{}".format(int(n)), end=" ")
                    d.append(n)
            else:
                #print("{}".format(int(n)), end=" ")    #Uncomment this if you want to print out each step for each number
                n = 3*n+1
                d.append(n)

        #Compares the last saved length of dic with the length of the new dic
        b = len(d)
        if(s < b):
            s = b
            l = a
        else:
            pass
        del d[:]
        #print(" ")                                     #Uncomment this if you want to print out each step for each number
        a += 1
    print("""\nMost steps required until reaching 1: {}
Most steps required for the whole number: {}""".format(s, l))

    
if __name__ == "__main__":
    main()