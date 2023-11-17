class Cart:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name