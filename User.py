class User:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""
        self.logged_in = False
        self.user_id = ""

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.logged_in = False
        self.user_id = ""

    def logout(self):
        self.user_id = ""
        self.logged_in = False
        return False

    def getLoggedIn(self):
        return self.logged_in

    def getUserID(self):
        return self.user_id