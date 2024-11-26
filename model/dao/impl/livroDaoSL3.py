from typing import List
import sqlite3 as sql

from entities.livro import Livro
from alunoDao import AlunoDao
from db.db import DB
from db.dbException import DbException

class LivroDaoSL3(AlunoDao):
    def __init__(self,conn):
        super().__init__()
        self.conn
    
    def insert(self,livro: Livro):
        cursor= None
        try:
            id_livro,titulo,autor,editora=vars(livro).values()

            cursor=self.conn.cursor()
            cursor.execute(
                "INSERT INTO livros(titulo, autor, editora) VALUES (?, ?, ?)",
                (titulo,autor,editora)
            )
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao cadastrar livro. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)
        
    
    def update(self,livro: Livro):
        cursor=None
        try:
            id_livro, titulo, autor, editora = vars(livro).values()
            cursosr= self.conn.cursosr()
            cursor.execute('''
                            UPDATE livros
                            SET titulo= ?, autor= ?, editora= ?
                            WHERE id = ? ''',(titulo,autor,editora,id_livro))
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao atualizar livro. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursosr)
            



    
    def deleteById(self,id: int):
        pass

    
    def findById(self,id: int):
        pass

    
    def findAll(self,livro: List[Livro]):
        pass
