#This program checks wether a given string is an anagram
#Execute this program in cmd

def main():
    name = input("Input the string you want to check: ")
    name_list = []
    name_list2 = []

    bool = check(name, name_list, name_list2)

    if bool:
        print("The word is an anagram!")
    else:
        print("The word is not an anagram!")


def check(name, name_list, name_list2):
    for letter in name:
        name_list.append(letter)

    name_list = list(reversed(name_list))
    name_list2 = "".join(name_list)

    if name_list2.lower() == name.lower():
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()