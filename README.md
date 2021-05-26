# Waiter Helper

## User Stories

- As a User I want to be able to see the menu in a formatted way, so that I can order my meal.


- As a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

- As a user, I want to have my order read back to me in formatted way so I know what I ordered.

### First Iteration

In this iteration, I solved the three user stories, exceeding the second one by giving the user the option to quit at will, rather than after a fixed number of items are ordered:

Initially, I created a class called ```OrderHelper``` This will encapsulate all methods associated with taking an order. The object will be initialised with an empty list of the order contents, and a boolean indicating that the order is active:

```python
class OrderHelper:

    def __init__(self):
        self.order_active = True
        self.order_contents = []
```

For user story 1, I created a function called ```show_menu``` in ```OrderHelper```. This function simply prints out the menu list (which I have added as a global variable in my main code.). The reasoning for having this in a separate method was that several methods might need to show the menu, minimising code duplication:

```python
    def show_menu(self):
        #print out the available items. Will later show the number key as well for easier user selection.
        for item in menu.values():
            print(item)
```

In iteration one, I simply want to be able to repeatedly add items to the order. For this, I wrote a method called ```add_item```, which shows the menu, asks the user to type the item they want, and adds it to the order if it is on the menu:

```python
    def add_item(self):
        #add an item to the order, after showing the menu. Eventually add functionality to select number from dictionary.
        print("Here's what's on the menu")
        self.show_menu()

        item = input("Please type which item you would like to add to your order. Type 'nothing' to add nothing: ")
        if item in menu.values():
            self.order_contents.append(item)
            print(f"{item} added to order.")

        else:
            print("input not recognised, please try again")
            return
```

These methods are tied together using a method called ```take_order```, which I have shown below:

```python
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
```
The method will ask the user if they want to add items, complete their order, or cancel the process. Based on their response, either the ```add_item``` function will be called, the order cancelled and the list of order contents cleared, or the order completed by showing the user their final order contents (in line with user story 3).

The method actually exceeds user story 2, which asks for 3 opportunities to order. I could achieve this by dropping out of my ordering process once the number of items in the order equals or exceeds three, but as I am about to show, I believed this could be better achieved by giving the user the option to drop out of the ordering process when they prefer. This means user story 2 can be met by selecting "done" when three items have been added, but it is also possible to order more or fewer items.

If the input is not one of the keywords, the loop will repeat.

A second iteration should feature the ability to remove items, and perhaps a smoother way of taking inputs (I have already packaged menu into a dictionary, with numbered keys, which should help with this.)