class DataStructureApp:
    def __init__(self):
        self.data_structures = {
            1: self.array_section,
            2: self.stack_section,
            3: self.queue_section,
            4: self.link_list_section,
            0: self.exit_app,
        }

        def run(self):
            while True:
                self.display_main_menu()
                choise = int(input("enter your choise: "))
                if choise in self.data_structures:
                    self.data_structures[choise]()

        def display_main_menu(self):
            print("Main Menu: ")
            print("1. Array")
            print("2. Stack")
            print("3. queue")
            print("4. Link List")
            print("0. Exit")

        def array_section(self):
            while True:
                self.display_main_menu()
                choice = int(input("enter your choice (0 to go back): "))
                if choice == 0:
                    break
                elif choice == 1:
                    self.introduce_array()
                elif choice == 2:
                    self.show_array_example()
                elif choice == 3:
                    self.show_sort_example()

        def display_array_menu(self):
            print("Array menu: ")
            print("1. introduce array ")
            print("2. show array example")
            print("3.show sort example")
            print("0. go back")

            def introduce_array(self):
                print("An array is a data structure that stores a collection of elements of the same type in a contiguous memory location.")

            def show_array_example(self):
                print("example ")
            def show_sort_exaple(self):
                print("show eample")

            def exit_app(self):
                print("exiting the application") 
                exit()



if __name__ == "__main__":
    app = DataStructureApp()
    app.run()

