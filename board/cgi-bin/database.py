import pymysql

# db = pymysql.connect("127.0.0.1", "root", "123456", "py")
class Database:
    url = '127.0.0.1'
    user = 'root'
    password = '123456'
    db = 'py'
    charset = 'utf8'

    def __init__(self):
        self.connection = pymysql.connect(
            self.url, self.user, self.password, self.db, charset=self.charset)
        self.cursor = self.connection.cursor()

    def insert(self, query,params):
        try:
            self.cursor.execute(query,params)
            self.connection.commit()
        except Exception as e:
            print (e)
            self.connection.rollback()

    def query(self, query,params):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query,params)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
