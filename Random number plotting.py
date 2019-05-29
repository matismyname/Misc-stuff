import secrets
import matplotlib.pyplot as plt

#This program generates a sample of random whole numbers and counts the occurence of each number
#The total number of occurences for each random number are plotted

def main():
    
    numbers = []
    xis = []
    ysis = []
    limit = 100         #Generate 100 random numbers
    counter = 0

    while counter < limit:
        num = secrets.randbelow(11)         #Each number should be below 11
        numbers.append(num)
        counter += 1
    
    a = 0
    while a < 11:
        p = 0
        xis.append(a)
        for item in numbers:
            if(item == a):
                p += 1
        ysis.append(p)
        print("Count of number {}: {}".format(a, p))
        a += 1

    plt.bar(xis,ysis, label="Numbers", color = "g")

    plt.xlabel("Numbers")
    plt.ylabel("Frequencies")
    plt.title("Numbers frequencies")
    plt.legend()
    plt.show()

main()