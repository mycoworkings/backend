import pymysql




#con = GetMysqlConn()

class MySql():

    def __init__(self):
        try:
            self._conn = pymysql.connect('localhost',
                             'root',
                             'espinete',
							'mycoworkings',charset='utf8', 
							use_unicode=True)
            self._cursor = self._conn.cursor()
        except Exception:
            print ('error: no me pude conectar 1!')
            return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        return self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
