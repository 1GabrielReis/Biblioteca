import sqlite3 as sql
import os

from .dbException import DbException

class DB:
    conn= None
    
    @staticmethod
    def loadProperties():
        if DB.conn is None:
            try:
                db_path = r"D:\Gabriel SSD\SENAI BACK-END\atividade\projeto_biblioteca\models\Biblioteca.db"
                DB.conn = sql.connect(db_path, check_same_thread=False)
                print("[DEBUG] Banco usado:", os.path.abspath(db_path))
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
            
    


