#set names here
task1_name = "Task 1 name"
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
        print("\n\n")
        print_menu()
        user_input = input("Pick an option: ")
    print("Exiting")

def task1():
    print(f"{task1_name} answer")

def task2():
    print(f"{task2_name} answer")

def task3():
    print(f"{task3_name} answer")

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
