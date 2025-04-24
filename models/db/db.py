import sqlite3 as sql

from .dbException import DbException

class DB:
    conn= None
    
    @staticmethod
    def loadProperties():
        if DB.conn is None:
            try:
                DB.conn = sql.connect('Biblioteca.db')
                return DB.conn
            except sql.Error as erro:
                raise DbException(f"Erro ao conectar ao banco de dados: {erro}")
            
    @staticmethod
    def getConn():
        if DB.conn is None:
            try:
                DB.loadProperties()
                return DB.conn
            except sql.Error as erro:
                raise DbException(f"Erro ao concetar: {erro}")
        return DB.conn
  
    @staticmethod
    def closeCursor(cursor):
        if cursor != None:
            try:
                cursor.close()
            except sql.Error as erro:
                raise DbException(f"Erro ao obter cursor: {erro}")
            
    


