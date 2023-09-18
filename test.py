# Define a function to display the main menu
def display_main_menu():
    print("Welcome to the Data Structures and Algorithms Explorer")
    print("1. Data Structures")
    print("2. Algorithms")
    print("3. Exit")

# Define a function to display the data structures menu
def display_data_structures_menu():
    print("\nData Structures:")
    print("1. Array")
    print("2. Stack")
    print("3. Queue")
    print("4. Linked List")
    print("5. Go back to the main menu")

# Define a function to display information about the Array data structure
def display_array_info():
    print("\nArray:")
    print("1. Introduction to Arrays")
    print("2. Example")
    print("3. user-defined example")
    print("4. Go back to the data structures menu")

# Define a function to display an example of an Array
def display_array_example():
    print("\nArray Example:")
    print("Here's an example of an array in JavaScript:")
    print("var fruits = ['apple', 'banana', 'cherry'];")
    print("console.log(fruits[0]); // Output: 'apple'")
    print("console.log(fruits.length); // Output: 3")
    print("console.log(fruits.indexOf('banana')); // Output: 1")
    print("console.log(fruits.pop()); // Output: 'cherry'")
    print("console.log(fruits); // Output: ['apple', 'banana']")
  
# about array
my_array = []

# Function to display the current array
def display_array():
    print("Current Array:", my_array)

# Function to add an element to the array
def add_element():
    element = input("Enter the element to add: ")
    my_array.append(element)
    print(element, "has been added to the array.")
    display_array()

# Function to remove an element from the array
def remove_element():
    if not my_array:
        print("The array is empty.")
        return
    
    display_array()
    index = int(input("Enter the index of the element to remove: "))
    
    if 0 <= index < len(my_array):
        removed_element = my_array.pop(index)
        print(removed_element, "has been removed from the array.")
    else:
        print("Invalid index. Element not removed.")

# Function to select an element from the array
def select_element():
    if not my_array:
        print("The array is empty.")
        return
    
    display_array()
    index = int(input("Enter the index of the element to select: "))
    
    if 0 <= index < len(my_array):
        selected_element = my_array[index]
        print("Selected element:", selected_element)
    else:
        print("Invalid index. Element not found.")
# array end  
    
def arry_user_example():
    print("\nArray Operations:")
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Select Element")
    print("4. Exit")  

# stack section 
# Initialize an empty stack
my_stack = []

# Function to display the current stack
def display_stack():
    print("Current Stack:", my_stack)

# Function to introduce stacks
def introduce_stack():
    print("\nStack:")
    print("A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.")
    print("The last element added to the stack is the first one to be removed.")
    print("Key operations on a stack include push (add an element) and pop (remove the top element).")

# Function to provide an example of a stack
def stack_example():
    print("\nStack Example:")
    print("Consider a stack of plates. You can add a plate to the top (push) or remove the top plate (pop).")
    print("The last plate you add is the first one you remove.")

# Function to add an element to the stack
def push_element():
    element = input("Enter the element to push onto the stack: ")
    my_stack.append(element)
    print(element, "has been pushed onto the stack.")
    display_stack()

# Function to remove the top element from the stack
def pop_element():
    if not my_stack:
        print("The stack is empty.")
        return
    
    popped_element = my_stack.pop()
    print(popped_element, "has been popped from the stack.")
    display_stack()
    
def ata_struct_choice():
    print("\nStack Operations:")
    print("1. Introduce Stack")
    print("2. Stack Example")
    print("3. Push Element")
    print("4. Pop Element")
    print("5. Exit")
    
    # queue section
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
# queue section end

# link list section start
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
                    display_array_info()
                    array_choice = input("Enter your choice: ")

                    if array_choice == "1":
                        # Display introduction to Arrays
                        print("An array is a collection of elements, each identified by an index or a key.")
                        print("It is a fundamental data structure in many programming languages.")
                    
                    elif array_choice == "2":
                        # Display user-defined example of Arrays
                        display_array_example()
                        
                    elif array_choice == "3":
                        arry_user_example()
                        choice = input("Enter your choice: ")
    
                        if choice == "1":
                            add_element()
                        elif choice == "2":
                            remove_element()
                        elif choice == "3":
                            select_element()
                        elif choice == "4":
                            print("Exiting the program. Goodbye!")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    elif array_choice == "4":
                        break  # Go back to the data structures menu

                    else:
                        print("Invalid choice. Please try again.")

            elif data_struct_choice == "2":
                while True:
                    
                       print("\nStack Operations:")
                       print("1. Introduce Stack")
                       print("2. Stack Example")
                       print("3. Push Element")
                       print("4. Pop Element")
                       print("5. Exit")
                    
                       choice = input("Enter your choice: ")
                       if choice == "1":
                           introduce_stack()
                       elif choice == "2":
                           stack_example()
                       elif choice == "3":
                           push_element()
                       elif choice == "4":
                           pop_element()
                       elif choice == "5":
                           print("Exiting the program. Goodbye!")
                           break
                       else:
                           print("Invalid choice. Please try again.")
    
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
                              
            elif data_struct_choice == "4":
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
                        break
                    # Go back to the data structures menu
                    else:
                     print("Invalid choice. Please try again.")                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                                    
              
                  
                                          
                              
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
