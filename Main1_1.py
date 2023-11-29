import User
import Inventory
import Cart
import sqlite3

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
    if answer4=="1": 
       break
    elif answer4=="2":
      viewCa = Cart.Cart()
      viewCa.view_cart()
    elif answer4=="3":
      addCa = Cart.Cart()
      isbnCa = input("Enter the ISBN of the item you would like to add to your cart: ")
      addCa.add_to_cart(isbnCa)
    elif answer4=="4":
      removeCa = Cart.Cart()
      isbnRe = input("Enter the ISBN of the item you would like to remove from your cart: ")
      removeCa.remove_from_cart(isbnRe)
    elif answer4=="5":
      checkOut = Cart.Cart()
      checkOut.check_out()

    elif answer4 !="1" or "2" or "3" or "4" or "5":
      print("\n Not Valid Choice Try again") 


def inventoryMenu():
   while True:
    print ("""
    1. Go Back
    2. View Inventory
    3. Search Inventory
    """)
    answer3 = input("Please Select an Option: ") 
    if answer3=="1": 
       break
    elif answer3=="2":
      viewII = Inventory.Inventory()
      print(viewII.view_inventory()) 
    elif answer3=="3":
      searchItem = input("What would you like to search for: ")
      searchI = Inventory.Inventory()
      print(searchI.search_inventory(searchItem))

    elif answer3 !="1" or "2" or "3":
      print("\n Not Valid Choice Try again") 


answer1 = (input)
print("Welcome to the M&T E-Commerce Store!")
#before login loop menu
ans=True
while ans:
    print ("""
    1. Log In
    2. Create Account
    3. Logout
    """)
    ans=answer1("Please Select an Option: ") 
    if ans=="1": 
       logUin = User.User()
       print("\n")
       logUin.login()
       break
    elif ans=="2":
      print("\n")
      creatAcc = User.User()
      creatAcc.create_account()
    elif ans=="3":
      quit()
    elif ans !="1" or "2" or "3":
      print("\n Not Valid Choice Try again") 


#after login loop menu (main menu)
while True:
    print ("""
    1. Log Out
    2. View Account Information
    3. Inventory Informatoin
    4. Cart Information
    """)
    answer2 = input("Please Select an Option: ") 
    if answer2=="1": 
       quit()

    elif answer2=="2":
      viewACI = User.User()
      viewACI.view_account_information

    elif answer2=="3":
      inventoryMenu()

    elif answer2=="4":
      cartMenu()

    elif answer2 !="1" or "2" or "3" or "4":
      print("\n Not Valid Choice Try again")
