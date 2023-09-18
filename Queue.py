# Define a function to display the data structures menu
def display_data_structures_menu():
    print("\nData Structures:")
    print("1. Array")
    print("2. Stack")
    print("3. Queue")
    print("4. Linked List")
    print("5. Go back to the main menu")

# Define a function to display information about the Queue data structure
def display_queue_info():
    print("\nQueue:")
    print("A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.")
    print("In a queue, elements are added at the rear (enqueue) and removed from the front (dequeue).")
    print("Common operations include enqueue, dequeue, and checking if the queue is empty.")

# Define a function to add an element to the Queue
def enqueue(queue, element):
    queue.append(element)

# Define a function to remove an element from the Queue
def dequeue(queue):
    if not queue:
        print("The queue is empty.")
        return None
    return queue.pop(0)

# Function to display the current Queue
def display_queue(queue):
    print("Current Queue:", queue)

# Main loop for the Queue operations
while True:
    display_data_structures_menu()
    data_struct_choice = input("Enter your choice: ")

    if data_struct_choice == "1":
        # Code for Array operations (add, remove, select elements) here
        print("Array operations coming soon!")

    elif data_struct_choice == "2":
        # Code for Stack operations (push, pop, peek) here
        print("\nStack:")
        print("A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.")
        print("In a stack, elements are added and removed from the top.")
        print("Common operations include push, pop, and checking if the stack is empty.")
        # You can add more code for stack operations here

    elif data_struct_choice == "3":
        while True:
            print("\nQueue Operations:")
            print("1. Introduce")
            print("2. Example")
            print("3. User-Defined Example")
            print("4. Go back to the data structures menu")

            queue_choice = input("Enter your choice: ")

            if queue_choice == "1":
                # Display introduction to Queue
                display_queue_info()

            elif queue_choice == "2":
                # Display an example of Queue
                print("\nQueue Example:")
                print("Consider a queue of people waiting in line.")
                print("The first person to arrive is the first to leave (FIFO).")
                print("Queue operations: enqueue (add to the end), dequeue (remove from the front).")

            elif queue_choice == "3":
                # Display a user-defined example of Queue
                my_queue = []
                print("\nUser-Defined Queue Example:")
                print("Let's simulate a queue for customers at a store.")
                while True:
                    print("\nQueue Operations:")
                    print("1. Enqueue (add customer to the queue)")
                    print("2. Dequeue (serve the next customer)")
                    print("3. Show Queue")
                    print("4. Exit")
                    queue_op = input("Enter your choice: ")
                    if queue_op == "1":
                        customer = input("Enter customer name: ")
                        enqueue(my_queue, customer)
                        print(f"{customer} has been added to the queue.")
                    elif queue_op == "2":
                        served_customer = dequeue(my_queue)
                        if served_customer is not None:
                            print(f"{served_customer} has been served.")
                        display_queue(my_queue)
                    elif queue_op == "3":
                        display_queue(my_queue)
                    elif queue_op == "4":
                        print("Exiting the user-defined queue example.")
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif queue_choice == "4":
                break  # Go back to the data structures menu

            else:
                print("Invalid choice. Please try again.")

    elif data_struct_choice == "4":
        # Add code for Linked List operations here
        print("Linked List operations coming soon!")

    elif data_struct_choice == "5":
        break  # Go back to the main menu

    else:
        print("Invalid choice. Please try again.")
# ============================================================================


