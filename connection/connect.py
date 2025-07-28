import mysql.connector

class mysqlConnection:
    
    c = None
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def con(self):    
        try:
            self.c = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            return "Connection successful"
        except mysql.connector.Error as err:
            return f"Error: {err}"
        
    def close(self):
        self.c.close()
            
        
            