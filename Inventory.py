import sqlite3
from tabulate import tabulate

class Inventory:
    def __init__(self, database_name="MethodsFinalProject.db", table_name="Inventory"):
        self.database_name = database_name
        self.table_name = table_name

    def set_database_table(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def view_inventory(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Inventory")
            items = cursor.fetchall()

            if not items:
                print("No items in the inventory.")
                return

            headers = [description[0] for description in cursor.description]
            table_data = [list(map(str, item)) for item in items]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def search_inventory(self, title):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Inventory WHERE title=?", (title,))
            results = cursor.fetchall()

            if results:
                for result in results:
                    print(result)
            else:
                print(f"No results found for title: {title}")

    def decrease_stock(self, isbn):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()

            try:
                cursor.execute(f"UPDATE Inventory SET stock = stock - 1 WHERE ISBN=?", (isbn,))
                connection.commit()
            except sqlite3.Error as e:
                print(f"Error updating stock: {e}")

    def get_database_name(self):
        return self.database_name

    def set_database_name(self, database_name):
        self.database_name = database_name

    def get_table_name(self):
        return self.table_name

    def set_table_name(self, table_name):
        self.table_name = table_name