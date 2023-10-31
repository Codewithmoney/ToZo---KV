import mysql.connector

# Creating a class with the name Database
class Database:
    # Initializing Constructor
    def __init__(self):
        # Configure DB
        self.conn = mysql.connector.connect(
            host = "localhost", 
            port = '3306', 
            user = "root", 
            password = "root", 
            database = "tozo"
            )
        QUERY = """create table if not exists todos(
        tid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        ttitle VARCHAR(70), 
        tdesc VARCHAR(200)
        );"""
        try:
            # Creating cursor
            self.CURSOR = self.conn.cursor(dictionary=True)
            # executing the QUERY
            self.CURSOR.execute(QUERY)
        except Exception as e:
            return e
    
    # defining a function to create a record in table
    def creater(self, ttitle, tdesc):
        try:
            self.CURSOR.execute("INSERT INTO todos(ttitle, tdesc) VALUES('{}', '{}')".format(ttitle, tdesc))
            self.conn.commit()
        except Exception as e:
            return e
    
    # defining a function to read a record from table
    def reader(self):
        try:
            self.CURSOR.execute("SELECT * FROM todos")
            rows = self.CURSOR.fetchall()
            return rows
        except Exception as e:
            return e
    
    # defining a function to update a record in table
    def updater(self, tid, newTitle, newDesc):
        try:
            self.CURSOR.execute("UPDATE `todos` SET `ttitle` = '{}', `tdesc` = '{}' WHERE (`tid` = '{}');".format(newTitle, newDesc, tid))
            self.conn.commit()
        except Exception as e:
            return e

    # defining a function to delete the database
    def deleteDB(self):
        try:
            self.CURSOR.execute("DROP TABLE todos")
        except Exception as e:
            return e
    
    # defining a function to delete record/records from table
    def deleter(self, tid):
        if tid=="all":
            self.CURSOR.execute("DELETE FROM todos")
            self.conn.commit()
        else:
            try:
                self.CURSOR.execute("DELETE FROM todos WHERE tid={}".format(tid))
                self.conn.commit()
            except Exception as e:
                return "[ERROR] Can't perform delete action"