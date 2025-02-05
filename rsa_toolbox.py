import math
# set names here
task1_name = "Prime Number Check"
task2_name = "Extended Euclidean Algorithm"
task3_name = "Calculate phi(N)"
task4_name = "Calculate modular inverse"

# Helper function that gives greatest common divisor
def gcd(a,b):
    while b > 0:
        if a < b: # ensure a is bigger than b
            a, b = b, a

        # prepare for the next round of calculation
        rest = a % b
        a = b
        b = rest
    return a

# Helper function that checks if numbers is relatively prime
def is_relatively_prime(a, b):
    if gcd(a,b) == 1:
        return True
    return False

# Ensures the user inputs a valid integer
def get_valid_number(user_input):
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Task 1
# Function that checks if given number is prime
def is_prime(n):
    # Numbers less than two are not prime
    if n < 2:
        return False
    # Divosors from 2 to sqrt(n) + 1 are checked
    for i in range(2, int(math.sqrt(n)) + 1):
        # if the division is 0, then the number is not prime
        if n % i == 0:
            return False
    return True

# Task 2
def extended_euclidean_algorithm(a, b):
    if is_relatively_prime(a, b):
        # calculate modular inverse
        print(f"The numbers {a} and {b} are relatively prime. \nInverse is: {calculate_modular_inverse(a, b)}")
    else:
        # if the numbers aren't relatively prime, the modular inverse
        # can't be calculated
        print("The numbers are not relatively prime.\nUnable to \
              calculate inverse.")
        
# Task 3
def eulers_totient_function(n):
    # Eulers totients function returns the counts from 0 to n that 
    # are relatively prime to n. We do this by looping through all 
    # the numbers from 0 to n and check if the gcd of this number 
    # is = 1. If it is, we know that this is relatively prime to n 
    # and add a 1 to our count. 
    count = 0
    for i in range(1, n):
        if is_relatively_prime(i, n):
            count += 1
    return count

# Task 4
def calculate_modular_inverse(e, n):
    phi_n = eulers_totient_function(n)
    if not is_relatively_prime(e, phi_n):
        # if the numbers aren't relatively prime, the modular inverse
        # can't be calculated
        print(f"e: {e} is not valid (no modular inverse exists).")
        return None

    a, b = e, phi_n
    x, x1 = 1, 0

    # Loop until b is 0 (base case)
    while b != 0:
        quotient = a // b
        a, b = b, a - quotient * b
        x, x1 = x1, x - quotient * x1

    # After base case is reached, a=1 indicates that a modular 
    # inverse exists
    if a != 1:  
        return None

    # x=e**(-1)
    # d = e**(-1) mod phi(N)
    d = x % phi_n  
    print(f"The modular inverse is: {d}")

    return d


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

def main():
    print_menu()
    user_input = input("Pick a number: ")
    while user_input != "5":
        if user_input == "1":
            n = get_valid_number("Enter a number to check if it's prime: ")
            print(f"Prime: {is_prime(n)}")
        elif user_input == "2":
            a = get_valid_number("Enter a number as e: ")
            b = get_valid_number("Enter a number as N: ")
            extended_euclidean_algorithm(a, b)
        elif user_input == "3":
            n = get_valid_number("N = p * q\nEnter N: ")
            print(f"Number of coprimes to N: {eulers_totient_function(n)}")
        elif user_input == "4":
            e = get_valid_number("Enter the e: ")
            n = get_valid_number("N = p * q\nEnter N: ")
            calculate_modular_inverse(e, n)

        #back to menu
        input("\nPress Enter to continue")
        print("\n\n")
        print_menu()
        user_input = input("Pick an option: ")
    print("Exiting")
    
if __name__ == "__main__":
    main()


'''
---------------------------------------
Question 1: What makes an asymmetric scheme like RSA slower than 
its symmetric alternatives such as AES? Explain. Also, what 
information in the RSA key generator, encryption and decryption 
algorithms an attacker may have access to?

RSA is slower than symmetric encryption alternatives like AES due 
to the computational complexity involved in its operations. RSA 
encryption and decryption rely on modular exponentiation with 
large numbers, which requires multiple expensive multiplications, 
making it significantly slower than AES, which operates on 
fixed-size blocks using efficient bitwise operations and 
substitution-permutation networks. Additionally, RSA keys need to 
be much larger than AES keys to provide equivalent security, 
further increasing the computational cost. In practice, RSA is 
mainly used for key exchange and authentication, while AES is used 
for encrypting large amounts of data efficiently. An attacker can 
access the public key (e, N), which is openly shared, and may 
intercept ciphertexts, but decrypting them is infeasible without 
the private key due to the difficulty of factoring N into its 
prime components.
---------------------------------------

Question 2: How many numbers from 1 to n should be tested before 
deciding if n is prime or not? Why?

To determine if a number n is prime, we only need to test 
divisibility up to square root of n, instead of checking all 
numbers from 1 to n. The reason is if n is not prime, it can be 
factored as n = a x b, where at least one of the factors must be 
less than or equal with the squareroot of n. This means that if n 
had a factor larger than the squareroot of n, then the other 
factor must be smaller. So if we can't find any divisors up to the 
squareroot of n, then n is prime.
---------------------------------------

Question 3: Alice wants to send m=15 to Bob. She gets Bob’s public 
key pk=(19,77) by visiting a public repository. If she decides to 
use RSA for encryption, what would the resulting cipher text be? 
(Show your calculation)

m = 15, e = 19, N = 77

Φ(N) = Φ(77) = Φ(11 x 7) = (11-1)(7-1) = 10 x 6 = 60
GCD(e, Φ(N)) = 1 → GCD(19, 60) = 1

c = m^e mod N → c = 15^19 mod 77

ALTERNATIV 1:
15^2 = 225 
225 mod 77 = 225 - (77 x 2) = 225 - 154 = 71

15^4 = (15^2)^2 = 71^2 = 5041 
5041 mod 77 = 5041 - (77 x 65) = 5041 - 5005 = 36

15^8 = (15^4)^2 = 36^2 = 1296 
1296 mod 77 = 1296 - (77 x 16) = 1296 - 1232 = 64

15^16 = (15^8)^2 = 64^2 = 4096 
4096 mod 77 = 4096 - (77 x 53) = 4096 - 4081 = 15

15^19 mod 77 = (15^16 x 15^2 x 15) mod 77 = (15 x 71 x 15) mod 77 = 
15975 mod 77 = 15975 - (77 x 207) = 15975 - 15939 = 36
→ c = 36 

ALTERNATIV 2:
(15^2 x 15^2 x 15^2 x 15^2 x 15^2 x 15^2 x 15^2 x 15^2 x 15^2 x 15)
mod 77 →
(71 x 71 x 71 x 71 x 71 x 71 x 71 x 71 x 71 x 15) mod 77 →
(36 x 36 x 36 x 36 x 71 x 15) mod 77 →
(64 x 64 x 71 x 15) mod 77 →
(15 x 64) mod 77 →
36 mod 77 →
c = 36
---------------------------------------
'''
