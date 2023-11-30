import User
import Inventory
import Cart
import sqlite3

#after login loop menu (main menu)########################
def mainMenu():
  while True:
    print ("""
    1. Log Out
    2. View Account Information
    3. Inventory Informatoin
    4. Cart Information
    """)
    answer2 = input("Please Select an Option: ") 
    if answer2=="1": 
       print("\nLogging out...\n")
       quit()
    elif answer2=="2":
      loggedIN.view_account_information()
    elif answer2=="3":
      inventoryMenu()
    elif answer2=="4":
      cartMenu()
    elif answer2 !="1" or "2" or "3" or "4":
      print("\n Not Valid Choice Try again")


# function for car menu, allows menu to go back to previous. ################
def cartMenu():
   while True:
    print ("""
    1. Go Back
    2. View Cart
    3. Add Items to Cart
    4. Remove an Item from Cart
    5. Check Out
    """)
    answer4 = input("Please Select an Option: ") 
    cart = Cart.Cart()
    if answer4=="1": 
       mainMenu()
    elif answer4=="2":
      cart.view_cart(loggedIN.getUserID())
    elif answer4=="3":
      isbnCa = input("Enter the ISBN of the item you would like to add to your cart: ")
      cart.add_to_cart(loggedIN.getUserID(), isbnCa)
    elif answer4=="4":
      isbnRe = input("Enter the ISBN of the item you would like to remove from your cart: ")
      cart.remove_from_cart(loggedIN.getUserID(), isbnRe)
    elif answer4=="5":
      cart.check_out(loggedIN.getUserID())
    elif answer4 !="1" or "2" or "3" or "4" or "5":
      print("\n Not Valid Choice Try again") 


# function for Inventory menu #####################
def inventoryMenu():
   while True:
    print ("""
    1. Go Back
    2. View Inventory
    3. Search Inventory
    """)
    answer3 = input("Please Select an Option: ") 
    inventory = Inventory.Inventory()
    if answer3=="1": 
       mainMenu()
    elif answer3=="2":
      print(inventory.view_inventory()) 
    elif answer3=="3":
      searchItem = input("What would you like to search for: ")
      print(inventory.search_inventory(searchItem))

    elif answer3 !="1" or "2" or "3":
      print("\n Not Valid Choice Try again") 


print("\nWelcome to the M&T E-Commerce Store!")

#before login loop menu ####################
while True:
    print ("""
    1. Log In
    2. Create Account
    3. Logout
    """)
    answer1 = input("Please Select an Option: ") 
    if answer1=="1": 
       loggedIN = User.User()
       print("\n")
       # checks for invalid username/password input
       while True:
        if loggedIN.login() == False:
         break
        else:
         mainMenu()
    elif answer1=="2":
      print("\n")
      creatAcc = User.User()
      creatAcc.create_account()
    elif answer1=="3":
      print("\nLogging out...\n")
      quit()
    elif answer1 !="1" or "2" or "3":
      print("\n Not Valid Choice Try again") 


