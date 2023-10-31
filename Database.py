import mysql.connector

class Database:
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
            self.CURSOR = self.conn.cursor(dictionary=True)
            self.CURSOR.execute(QUERY)
        except Exception as e:
            print("[ERROR] Table not created")
    
    def insertor(self, ttitle, tdesc):
        self.CURSOR.execute("INSERT INTO todos(ttitle, tdesc) VALUES('{}', '{}')".format(ttitle, tdesc))
        self.conn.commit()
    
    def fetcher(self):
        self.CURSOR.execute("SELECT * FROM todos")
        rows = self.CURSOR.fetchall()
        return rows
    
    def deleteDB(self):
        self.CURSOR.execute("DROP TABLE todos")