# Define a function to display the main menu
def display_main_menu():
    print("Welcome to the Data Structures and Algorithms Explorer")
    print("1. Data Structures")
    print("2. Algorithms")
    print("3. Exit")

# ... (rest of the code)

# Define a function to display the linked list menu
def display_linked_list_menu():
    print("\nLinked List:")
    print("1. Introduction to Linked Lists")
    print("2. Example of Linked List")
    print("3. User-Defined Example of Linked List")
    print("4. Go back to the data structures menu")

# Define a function to display information about Linked Lists
def display_linked_list_info():
    print("\nIntroduction to Linked Lists:")
    print("A linked list is a linear data structure where each element is a separate object,")
    print("called a node, that consists of two parts: data and a reference (link) to the next node.")
    print("Linked lists allow dynamic memory allocation and efficient insertions and deletions.")

# Define a function to display an example of a Linked List
def display_linked_list_example():
    print("\nExample of Linked List:")
    print("Consider a singly linked list with the following elements:")
    print("1 -> 2 -> 3 -> 4 -> 5")

# Define a function to display a user-defined example of a Linked List
def display_linked_list_user_example():
    print("\nUser-Defined Example of Linked List:")
    print("Let's create a linked list of names:")
    linked_list = []

    while True:
        name = input("Enter a name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        linked_list.append(name)

    print("Linked List of Names:")
    for name in linked_list:
        print(name)

# ... (Rest of the code remains the same)

# Main loop for the application
while True:
    display_main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            display_data_structures_menu()
            data_struct_choice = input("Enter your choice: ")

            if data_struct_choice == "1":
                while True:
                    display_linked_list_menu()
                    linked_list_choice = input("Enter your choice: ")

                    if linked_list_choice == "1":
                        # Display introduction to Linked Lists
                        display_linked_list_info()

                    elif linked_list_choice == "2":
                        # Display an example of a Linked List
                        display_linked_list_example()

                    elif linked_list_choice == "3":
                        # Display a user-defined example of a Linked List
                        display_linked_list_user_example()

                    elif linked_list_choice == "4":
                        break  # Go back to the data structures menu

                    else:
                        print("Invalid choice. Please try again.")

            elif data_struct_choice == "2":
                # Add code to display information about other data structures (Queue, Stack) here
                print("Information about other data structures coming soon!")

            elif data_struct_choice == "5":
                break  # Go back to the main menu

            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            display_stack_menu()
            stack_choice = input("Enter your choice: ")

            if stack_choice == "1":
                # Display introduction to Stacks
                print("\nIntroduction to Stacks:")
                print("A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle.")
                print("Key operations on a stack include push (add an element), pop (remove the top element), and peek (view the top element).")

            elif stack_choice == "2":
                # Push an element onto the stack
                push_element()

            elif stack_choice == "3":
                # Pop an element from the stack
                pop_element()

            elif stack_choice == "4":
                # Peek at the top element of the stack
                peek_element()

            elif stack_choice == "5":
                break  # Go back to the data structures menu

            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
