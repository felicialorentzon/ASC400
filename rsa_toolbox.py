import math
#set names here
task1_name = "Prime Number Check"
task2_name = "Extended Euclidean Algorithm"
task3_name = "Calculate phi(n)"
task4_name = "Get secret key"

def main():
    print_menu()
    user_input = input("Pick a number: ")
    while user_input != "5":
        if user_input == "1":
            task1()
        elif user_input == "2":
            extendedEuclideanAlgorithm()
        elif user_input == "3":
            n = input()
            print("N = p * q\nEnter N: " + n)
            eulers_totient_function(n)
        elif user_input == "4":
            e = input()
            print("Enter the e: " + e)
            n = input()
            print("N = p * q\nEnter N: " + n)
            task4(e, n)

        #back to menu
        input("\npress Enter to continue")
        print("\n\n")
        print_menu()
        user_input = input("Pick an option: ")
    print("Exiting")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def task1():
    n = int(input("Enter a number to check if it's prime: "))
    print(f"Prime: {is_prime(n)}")

def extendedEuclideanAlgorithm(): #TODO: check if != 0 and numbers
    a = int(input("write the first number: "))
    b = int(input("write the second number: "))
    
    if realtivelyPrime(a,b):
        #inverse
        print("relatively prime")
    else:
        print("The numbers are not relatively prime.\nUnable to calculate inverse.")


def realtivelyPrime(a,b):
    if GCD(a,b) == 1:
        return True
    return False

def GCD(a,b):
    while b > 0:
        if a < b: # ensure a is bigger than b
            temp = a
            a = b
            b = temp

        #prepare for the next round of calculation
        rest = a % b
        a = b
        b = rest
    return a
        

def eulers_totient_function(n):
    # Eulers totients function returns the counts from 0 to n that are 
    # relatively prime to n.
    # We do this by looping through all the numbers from 0 to n and
    # check if the gcd of this number is = 1. If it is, we know that this
    # is relatively prime to n and add a 1 to our count. 
    count = 0
    for i in range(1, n):
        if GCD(i, n) == True:
            count += 1
    print(f"Number of coprimes to n: {count}")

def task4(e, n):
    # this function calculates the secret key my getting the value e and the modulus.
    # the function then verifies this by comparing the encryption a message 2350 and decrpting it
    phi_n = eulers_totient_function(n)
    isvalid_e = realtivelyPrime(e, phi_n)
    if(isvalid_e):
        print(f"{e} is valid. Will continue to calculate the secret key...")
        e_inverse = 1 / e
        d = e_inverse % phi_n
    else:
        print(f"{e} is not valid")


def print_menu():
    menu = ("________________________\n"+
            "          Menu          \n"+
            "                        \n"+
            "Available functions:    \n"+
            f"1. {task1_name}        \n"+
            f"2. {task2_name}        \n"+
            f"3. {task3_name}        \n"+
            f"4. {task4_name}        \n"+
            "5. Quit                 \n"+
            "________________________\n")
    
    print(menu)
    

if __name__ == "__main__":
    main()
