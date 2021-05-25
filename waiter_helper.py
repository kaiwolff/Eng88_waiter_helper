class OrderHelper:

    def __init__(self):
        self.order_active = True
        self.order_contents = []


    def show_menu(self):
        #print out the available items
        for item in menu.values():
            print(item)

    def add_item(self):
        #add an item to the order, after showing the menu
        print("Here's what's on the menu")
        self.show_menu()

        item = input("Please type which item you would like to add to your order. Type 'nothing' to add nothing: ")
        if item in menu.values():
            self.order_contents.append(item)
            print(f"{item} added to order.")

        else:
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
                next_step = input("Type 'add' to add an item, or 'remove' to remove an item. To place your order, type 'done', or 'exit' to quit the order process: ")

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
                #if remove, run remove_item
                #if exit, empty list and quit order process
                if next_step == "exit":
                    clear(order)
                    print("order cancelled")
                    self.order_active = Fal




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