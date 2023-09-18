class DataStructureApp:
    def __init__(self):
        self.data_structures = {
            1: self.array_section,
            2: self.stack_section,
            3: self.queue_section,
            4: self.linked_list_section,
            0: self.exit_app,
        }

    def run(self):
        while True:
            self.display_main_menu()
            choice = int(input("Enter your choice: "))
            if choice in self.data_structures:
                self.data_structures[choice]()

    def display_main_menu(self):
        print("Main Menu:")
        print("1. Array")
        print("2. Stack")
    def array_section(self):
        while True:
            self.display_array_menu()
            choice = int(input("Enter your choice (0 to go back): "))
            if choice == 0:
                break
            elif choice == 1:
                self.introduce_array()
            elif choice == 2:
                self.show_array_example()
            elif choice == 3:
                self.show_search_example()
            elif choice == 4:
                self.show_sort_examples()
            elif choice == 5:
                self.show_insertion_example()
            elif choice == 6:
                self.show_deletion_example()

    def display_array_menu(self):
        print("Array Menu:")
        print("1. Introduce Array")
        print("2. Show Array Example")
        print("3. Show Search Example")
        print("4. Show Sort Examples")
        print("5. Show Insertion Example")
        print("6. Show Deletion Example")
        print("0. Go back")

    def stack_section(self):
        while True:
            self.display_stack_menu()
            choice = int(input("Enter your choice (0 to go back): "))
            if choice == 0:
                break
            # Implement stack section options here

    def display_stack_menu(self):
        print("Stack Menu:")
        # List stack section options here
        print("0. Go back")

    def queue_section(self):
        while True:
            self.display_queue_menu()
            choice = int(input("Enter your choice (0 to go back): "))
            if choice == 0:
                break
            # Implement queue section options here

    def display_queue_menu(self):
        print("Queue Menu:")
        # List queue section options here
        print("0. Go back")

    def linked_list_section(self):
        while True:
            self.display_linked_list_menu()
            choice = int(input("Enter your choice (0 to go back): "))
            if choice == 0:
                break
            # Implement linked list section options here

    def display_linked_list_menu(self):
        print("Linked List Menu:")
        # List linked list section options here
        print("0. Go back")

    def introduce_array(self):
        print("An array is a data structure that stores a collection of elements of the same type in a contiguous memory location.")

    def show_array_example(self):
        print("Example: ")
        # Provide an example of using an array

    def show_search_example(self):
        print("Example for searching in an array: ")
        # Provide an example of searching in an array

    def show_sort_examples(self):
        print("Sorting Algorithms:")
        # List different sorting algorithms (e.g., bubble sort, quicksort, etc.)

    def show_insertion_example(self):
        print("Example for inserting elements into an array: ")
        # Provide an example of inserting elements into an array

    def show_deletion_example(self):
        print("Example for deleting elements from an array: ")
        # Provide an example of deleting elements from an array

    def exit_app(self):
        print("Exiting the application.")
        exit()


if __name__ == "__main__":
    app = DataStructureApp()
    app.run()
