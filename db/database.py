import sqlite3   

class Db:
    def __init__(self, dbname="data.db"):
        self.conn = sqlite3.connect('data.db')
        
    def commit(self):
        self.conn.commit()

    def cursor(self):
        c = self.conn.cursor()
        return c

    def execute(self, q, par=[]):
        c = self.cursor()
        c.execute(q, par)
        self.conn.commit()

    def execute_and_fetch(self, q, par=[], type='a'):
        '''
            type:
                a => fetch all
                o => fetch one
        '''
        c = self.cursor()
        c.execute(q, par)
        if type == 'a':
            return c.fetchall()
        else:
            return c.fetchone()