import sqlite3

class Inventory:
    def __init__(self, database_name="MethodsFinalProject.db", table_name="Inventory"):
        self.databadeName = database_name
        self.tableName = table_name

    def set_database_table(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def view_inventory(self):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {self.tableName}")
        items = cursor.fetchall()
        for item in items:
            print(item)

        connection.close()

    def search_inventory(self, title):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {self.tableName} WHERE title=?", (title,))
        results = cursor.fetchll()

        if results:
            for results in results:
                print(results)
        else:
            print(f"No results found for title: {title}")

        connection.close()
    
    def decrease_stock(self, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        cursor.execute(f"UPDATE {self.tableName} SET stock = stock - 1 WHERE ISBN=?", (ISBN,))

        connection.commit()
        connection.close()

    def get_database_name(self):
        return self.databaseName
    
    def set_database_name(self, databaseName):
        self.databaseName = databaseName

    def get_table_name(self):
        return self.tableName
    
    def set_table_name(self, tableName):
        self.tableName = tableName