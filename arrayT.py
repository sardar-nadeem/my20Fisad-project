# Initialize an empty array
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

# Main loop for the array operations
while True:
    print("\nArray Operations:")
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Select Element")
    print("4. Exit")
    
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
