import sqlite3
from Inventory import Inventory
class Cart:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""

    def __init__(self, database_name="MethodsFinalProject.db", table_name="Cart"):
        self.database_name = database_name
        self.table_name = table_name

    def view_cart(self, user_id):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()

            # Use a JOIN statement to retrieve information from both Cart and Inventory tables
            cursor.execute(f'SELECT Cart.ISBN, Title, Author, Genre, Pages, "Release Date", Quantity FROM {self.table_name} INNER JOIN Inventory ON Cart.ISBN = Inventory.ISBN WHERE UserID=?', (user_id,))
            cart_items = cursor.fetchall()

            if not cart_items:
                print("Your cart is empty.")
                return

            print("Items in your cart:")
            for item in cart_items:
                # item[0] is the ISBN, and the other elements are from the Inventory table
                print(f"ISBN: {item[0]}, Title: {item[1]}, Author: {item[2]}, Genre: {item[3]}, Pages: {item[4]}, Release Date: {item[5]}, Quantity: {item[6]}")

    def add_to_cart(self, user_id, isbn):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()

            # Check if the book with the specified ISBN exists in the Inventory table
            cursor.execute("SELECT * FROM Inventory WHERE ISBN=?", (isbn,))
            book_data = cursor.fetchone()

            if not book_data:
                print(f"Book with ISBN {isbn} not found in the inventory.")
                return

            try:
                # Book exists in the Inventory, so insert it into the Cart
                cursor.execute(f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES (?, ?, 1)",
                            (user_id, isbn))
                connection.commit()
                print(f"Book with ISBN {isbn} added to your cart.")
            except sqlite3.Error as e:
                print(f"Error adding to cart: {e}")

    def remove_from_cart(self, user_id, isbn):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()

            # Check if the book with the specified ISBN exists in the Cart
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID=? AND ISBN=?", (user_id, isbn))
            book_data = cursor.fetchone()

            if not book_data:
                print(f"Book with ISBN {isbn} not found in your cart.")
                return

            try:
                # Book exists in the Cart, so remove it from the Cart
                cursor.execute(f"DELETE FROM {self.table_name} WHERE UserID=? AND ISBN=?", (user_id, isbn))
                connection.commit()
                print(f"Book with ISBN {isbn} removed from your cart.")
            except sqlite3.Error as e:
                print(f"Error removing from cart: {e}")

    def check_out(self, user_id):
            with sqlite3.connect(self.database_name) as connection:
                cursor = connection.cursor()

                # Get cart items for the user
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID=?", (user_id,))
                cart_items = cursor.fetchall()

                if not cart_items:
                    print("Your cart is empty. Nothing to check out.")
                    return

                # Call the Inventory class function to decrease the stock of the books
                inventory = Inventory()
                for item in cart_items:
                    inventory.decrease_stock(item[1])

                # Remove all items from the cart after checking out
                cursor.execute(f"DELETE FROM {self.table_name} WHERE UserID=?", (user_id,))
                connection.commit()

                print("Checkout successful. Your cart is now empty.")
