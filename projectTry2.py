# Define a function to display the main menu
def display_main_menu():
    print("Welcome to the Data Structures and Algorithms Explorer")
    print("1. Data Structures")
    print("2. Algorithms")
    print("3. Exit")

# Define a function to display the data structures menu
def display_data_structures_menu():
    print("\nData Structures:")
    print("1. Array (import from JavaScript)")
    print("2. Stack")
    print("3. Queue")
    print("4. Linked List")
    print("5. Go back to the main menu")

# Main loop for the application
while True:
    display_main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            display_data_structures_menu()
            data_struct_choice = input("Enter your choice: ")

            if data_struct_choice == "1":
                # Display information about arrays imported from JavaScript
                print("Arrays in JavaScript are...")
                # Add more information here

            elif data_struct_choice == "2":
                # Display information about stacks
                print("A stack is...")
                # Add more information here

            elif data_struct_choice == "3":
                # Display information about queues
                print("A queue is...")
                # Add more information here

            elif data_struct_choice == "4":
                # Display information about linked lists
                print("A linked list is...")
                # Add more information here

            elif data_struct_choice == "5":
                break  # Go back to the main menu

            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        # Add code to display information about algorithms here
        print("Algorithms information coming soon!")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        
        # this is array section 
        
        
