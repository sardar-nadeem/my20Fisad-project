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

# Main loop for stack operations
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
