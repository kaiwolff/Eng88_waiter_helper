class OrderHelper:

    def __init__(self):
        self.order_active = True
        self.order_contents = []


    def show_menu(self):
        #print out the available items. Will later show the number key as well for easier user selection.
        for item in menu.keys():
            print(f"{item}.  {menu[item]}")

    def add_item(self):
        #add an item to the order, after showing the menu. Eventually add functionality to select number from dictionary.
        print("Here's what's on the menu")
        self.show_menu()

        item = input("Please type the number of the item you would like to add to your order. Otherwise, hit enter to continue: ")
        try:
            item = int(item)

        except:
            return

        if int(item) in menu.keys():
            added_item = menu.get(int(item))
            self.order_contents.append(added_item)
            print(f"{added_item} added to order.")

        else:
            print("number not recognised, please try again")
            return


    def take_order(self):
        #this function will add or remove items to an order until the customer states they are happy with their order, or abort the order process
        while self.order_active:
            if self.order_contents == False:
                print("You are currently ordering nothing. Type 'add' to add items, or 'exit' to exit: ")
            else:
                print("Here is your current order:")
                for item in self.order_contents:
                    print(item)
                next_step = input("Type 'add' to add an item. To place your order, type 'done', or 'exit' to quit the order process: ")

                #Have now taken input. Next is to take appropriate action with list.
                #if done, set order_active to False and print out order.
                if next_step == "done":
                    print("\nThank you for your order. Here is a summary:")
                    for item in self.order_contents:
                        print(item)
                    self.order_active = False
                #if add, run add_item
                elif next_step == "add":
                    print("add selected")
                    self.add_item()
                #if remove, run remove_item. Additional feature once user stories done.
                #if exit, empty list and quit order process
                elif next_step == "exit":
                    clear(self.order_contents)
                    print("order cancelled")
                    self.order_active = False
                else:
                    print("input not recognised")
                    continue




#Set up a menu for usage
menu = {
    1 : "Burger",
    2 : "Milkshake",
    3 : "Fries",
    4 : "Sweet Potato Fries",
    5 : "Beer",
}

my_order = OrderHelper()
my_order.take_order()