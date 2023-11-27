import User
import Inventory
import Cart


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
      #print(viewCa.view_cart()) 
    elif answer4=="3":
      print("This adds items to carts")
    elif answer4=="4":
      print("This removes an item from cart")
    elif answer4=="5":
      print("this checks out user")

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
       print("call Login function from User Class")
       break
    elif ans=="2":
      print("call create account function from User class") 
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
      #print(viewACI.viewAccountInformation) 

    elif answer2=="3":
      print("fix this")
      inventoryMenu()

    elif answer2=="4":
      print("fix this")
      cartMenu

    elif answer2 !="1" or "2" or "3" or "4":
      print("\n Not Valid Choice Try again")