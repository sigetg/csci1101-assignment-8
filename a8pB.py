# Write a program to simulate a simple inventory system.  The program will
# support 5 commands from the user: new, add, remove, list, and quit.  The
# program should continue prompting the user for more commands until they enter
# the quit command.  Each of the other four commands (new, add, remove, list)
# will interact with a dictionary that you will maintain to track the inventory
# of a collection of items.  Each item has an integer ID number (must be
# positive) and an integer count that tracks how many of that item are currently
# in the inventory.
#
# You are required to create at least 4 functions to solve this problem.  All 4
# of these functions take a single parameter, which is the dictionary
# representing the current state of the inventory.
#
# 1) A function named new_item(), that will add a new item to the inventory.
#    The function will prompt the user to enter the new item's ID number and
#    print an error message if the ID is invalid or if the ID already exists in
#    the dictionary.  Otherwise it adds the new ID to the dictionary with a
#    current inventory count of zero.
# 2) A function named add_inventory(), that will add to the count of a given
#    item.  The function will prompt the user to enter the existing item's ID
#    number, then prompt for how many more of that item to add to the inventory.
#    Errors must be printed if the ID is not in the inventory or if the count
#    provided is invalid (less than 1).  Otherwise it updates the count for the
#    given item by adding in the provided count.
# 3) A function named remove_inventory(), that will remove from the count for a
#    given item.  The function will prompt the user to enter the existing item's
#    ID number, then prompt for how many of that item to remove from the
#    inventory.  Errors must be printed if the ID is not in the inventory or if
#    the count provided is invalid (less than 1).  Otherwise it updates the
#    count for the given item by removing the provided count.  If the new count
#    would be negative, print a warning message and set the count to be zero.
# 4) A function named list_inventory(), that prints the current inventory,
#    sorted by increasing ID numbers.  If the inventory is empty, print a
#    message stating that.
#
# There are several important details here.  First, your program should never
# exit when an error is encountered.  Instead, print the appropriate error
# message and move on to the next command.  Second, each of the 4 functions
# above corresponds directly to the 4 non-quit commands that the user can enter.
# Your main program must call the appropriate function based on the command
# entered, or print an error if the command itself was invalid.  Each of the 4
# functions, then, will handle all input/output, error messages, and inventory
# updates in the function.
#
# Note that commands are case insensitive, and that you should print a blank
# line after each command is processed to make the output easier to read.
#
# Your input and output messages must conform to the following examples:
#
# Inventory System
# Available commands: new, add, remove, list, quit
# Enter command: list
# Inventory empty.
#
# Enter command: done
# Invalid command!
# Available commands: new, add, remove, list, quit
#
# Enter command: new
# Enter the new item's ID: 14400
#
# Enter command: list
# ID: Count
# 14400: 0
#
# Enter command: add
# Enter the item ID: 7
# Error! 7 not in inventory!
#
# Enter command: add
# Enter the item ID: 14400
# How many more 14400 items? 50
#
# Enter command: list
# ID: Count
# 14400: 50
#
# Enter command: add
# Enter the item ID: 14400
# How many more 14400 items? 4
#
# Enter command: list
# ID: Count
# 14400: 54
#
# Enter command: new
# Enter the new item's ID: 14400
# Error! 14400 already in inventory!
#
# Enter command: remove
# Enter the item ID: 4
# Error! 4 not in inventory!
#
# Enter command: remove
# Enter the item ID: 14400
# How many less 14400 items? 45
#
# Enter command: list
# ID: Count
# 14400: 9
#
# Enter command: remove
# Enter the item ID: 14400
# How many less 14400 items? 10
# Warning: More 14400 items removed than in inventory.  Inventory for 14400 set to zero.
#
# Enter command: list
# ID: Count
# 14400: 0
#
# Enter command: quit
#
# Note the order of inputs, capitalization of messages, spacing, etc.




def new_item(my_dict):
    x = input("Enter the new item's ID: ")
    if x in my_dict:
        print("Error! 14400 already in inventory!")
    else:
        my_dict[x] = 0
    return my_dict

def add_inventory(my_dict):
    x = input("Enter the item ID: ")
    if x not in my_dict:
        print(f"Error! {x} not in inventory!")
    else:
        y = int(input(f"How many more {x} items? "))
        if y < 1:
            print("Error! number of items must be one or more!")
        else:
            my_dict[x] = my_dict[x] + y
    return(my_dict)

def remove_inventory(my_dict):
    x = input("Enter the item ID: ")
    if x not in my_dict:
        print(f"Error! {x} not in inventory!")
    else:
        y = int(input(f"How many less {x} items? "))
        if y < 1:
            print("Error! number of items must be one or more!")
        else:
            my_dict[x] = my_dict[x] - y
            if my_dict[x] < 0:
                print("Warning: More 14400 items removed than in inventory.  Inventory for 14400 set to zero.")
                my_dict[x] = 0
                
    return(my_dict)

def list_inventory(my_dict):
    if my_dict == {}:
        print("Inventory empty.")
    else:
        print("ID: Count")
        sorted_dict = sorted(my_dict.items(), key = lambda x: x[1], reverse = False)
        for key, value in sorted_dict:
            print(f"{key}: {value}")

inventory = {}
print("Inventory System")
print("Available commands: new, add, remove, list, quit")
x = input("Enter command: ")

while x != "quit":
    if x != "new" and x != "add" and x != "remove" and x !=  "list":
        print("Invalid command!")
        print("Available commands: new, add, remove, list, quit", "\n")
        x = input("Enter command: ")
        continue
    if x == "new":
        new_item(inventory)
        print("\n", end="")
        x = input("Enter command: ")
    if x == "add":
        add_inventory(inventory)
        print("\n", end="")
        x = input("Enter command: ")
    if x == "remove":
        remove_inventory(inventory)
        print("\n", end="")
        x = input("Enter command: ")
    if x == "list":
        list_inventory(inventory)
        print("\n", end="")
        x = input("Enter command: ")















