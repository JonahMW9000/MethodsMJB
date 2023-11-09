answer1 = (input)

print("Welcome to the M&T E-Commerce Store!")

ans=True
while ans:
    print ("""
    1. Log In
    2. Create Account
    3. Logout
    """)
    ans=answer1("Please Select an Option: ") 
    if ans=="1": 
      print("\n THIS TAKES USER AND PASS THEN ENTERS MAIN MENU") 
    elif ans=="2":
      print("\n THIS TAKES USER AND PASS FOR USER CLASS") 
    elif ans=="3":
      quit()
    elif ans !="1" or "2" or "3":
      print("\n Not Valid Choice Try again") 