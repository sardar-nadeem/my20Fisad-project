def main_menu():
    while True:
        print("Main Menu:")
        print("1. Lists")
        print("2. Stack")
        print("3. Queue")
        print("4. Linked List")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            lists_menu()
        elif choice == '2':
            stack_menu ()
        elif choice == '3':
            queue_menu()
        elif choice == '4':
            linked_list_menu()
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def lists_menu():
    while True:
        print("Lists Menu:")
        print("1. Introduction")
        print("2. Examples")
        print("3. Algorithms")
        print("0. Back")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print("Introduction to Lists")
        elif choice == '2':
            examples_menu()
        elif choice == '3':
            algorithms_menu()
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def examples_menu():
    while True:
        print("Examples Menu:")
        print("1. Search")
        print("2. Sort")
        print("3. Insertion")
        print("4. Deletion")
        print("0. Back")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print("Examples for Searching")
        elif choice == '2':
            sort_examples()
        elif choice == '3':
            insertion_examples()
        elif choice == '4':
            print("Examples for Deletion")
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def sort_examples():
    while True:
        print("Sort Examples:")
        print("1. Bubble Sort")
        print("2. Quick Sort")
        print("3. Merge Sort")
        print("4. Selection Sort")
        print("5. Insertion Sort")
        print("6. Heap Sort")
        print("7. Radix Sort")
        print("0. Back")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print("Example for Bubble Sort")
        elif choice == '2':
            print("Example for Quick Sort")
        # Add more sort examples here
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def insertion_examples():
    while True:
        print("Insertion Examples:")
        print("1. Push")
        print("2. Pop")
        print("0. Back")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print("Example for Push")
        elif choice == '2':
            print("Example for Pop")
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
