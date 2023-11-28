import sqlite3
from Inventory import Inventory
class User:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""
        self.logged_in = False
        self.user_id = ""

    def __init__(self, database_name="MethodsFinalProject.db", table_name="User"):
        self.database_name = database_name
        self.table_name = table_name
        self.logged_in = False
        self.user_id = ""

    def login(self):
        # Input and validation for login
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Validate login credentials
        if self.validate_login(email, password):
            self.logged_in = True
            self.user_id = email  # Assuming email is the user ID
            print("Login successful.")
            return True
        else:
            print("Invalid email or password.")
            return False

    def validate_login(self, email, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE Email=? AND Password=?", (email, password))
            return cursor.fetchone() is not None

    def logout(self):
        self.user_id = ""
        self.logged_in = False
        return False

    def view_account_information(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID=?", (self.getUserID(),))
            user_data = cursor.fetchone()

            if user_data:
                print("Account information:")
                print(f"User ID: {user_data[0]}")
                print(f"Email: {user_data[1]}")
                print(f"First Name: {user_data[3]}")
                print(f"Last Name: {user_data[4]}")
                print(f"Address: {user_data[5]}")
                print(f"City: {user_data[6]}")
                print(f"State: {user_data[7]}")
                print(f"Zip: {user_data[8]}")
                print(f"Payment: {user_data[9]}")
            else:
                print("User not found.")

    def create_account(self):
        # Input and validation for creating an account
        email = input("Enter your email: ")
        password = input("Enter a new password: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        address = input("Enter your address: ")
        city = input("Enter your city: ")
        state = input("Enter your state: ")
        zip_code = input("Enter your ZIP code: ")
        payment = input("Enter your payment method: ")

        # Database interaction to create a new account
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO {self.table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (email, password, first_name, last_name, address, city, state, zip_code, payment))
            connection.commit()
            print(f"Account created for user {email}.")

    def getLoggedIn(self):
        return self.logged_in

    def getUserID(self):
        return self.user_id
