import math
#set names here
task1_name = "Prime Number Check"
task2_name = "Task 2 name"
task3_name = "Task 3 name"
task4_name = "Task 4 name"

def main():
    print_menu()
    user_input = input("Pick a number: ")
    while user_input != "5":
        if user_input == "1":
            task1()
        elif user_input == "2":
            task2()
        elif user_input == "3":
            task3()
        elif user_input == "4":
            task4()

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

def task2():
    print(f"{task2_name} answer")

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

def task4():
    print(f"{task4_name} answer")

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
