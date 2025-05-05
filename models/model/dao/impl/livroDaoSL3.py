from typing import List
import sqlite3 as sql

from ...entities.livro import Livro
from ...dao.livroDao import LivroDao
from ....db.db import DB
from ....db.dbException import DbException

class LivroDaoSL3(LivroDao):
    def __init__(self,conn):
        super().__init__()
        self.conn= conn
    
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
            if cursor.rowcount > 0:
                livro.id=cursor.lastrowid
            else:
                raise DbException(f"Erro, não foi possivel inserir os dados")
        except sql.Error as erro:
            raise DbException(f"Erro ao cadastrar livro. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)
        
    
    def update(self,livro: Livro):
        cursor=None
        try:
            id_livro, titulo, autor, editora = vars(livro).values()
            cursor= self.conn.cursor()
            cursor.execute('''
                            UPDATE livros
                            SET titulo= ?, autor= ?, editora= ?
                            WHERE id_livro = ? ''',(titulo,autor,editora,id_livro))
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao atualizar livro. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)
            

    def deleteById(self,id: int):
        cursor=None
        try:
            cursor= self.conn.cursor()
            cursor.execute('DELETE FROM livros WHERE id_livro = ?', (id,))
            self.conn.commit()
            if cursor.rowcount == 0:
                raise DbException(f"ID não encontrado")
        except sql.Error as erro:
            raise DbException(f"Erro ao deletar livro. \n Detalhes: {erro}")
        finally:
            DB.closeCursor(cursor)  
              

    def findById(self,id: int):
        cursor= None
        try:
            cursor= self.conn.cursor()
            cursor.execute("SELECT * FROM livros WHERE id_livro = ? ",(id,))
            resultSet= cursor.fetchone()
            if resultSet is not None:
                livro=self._instaciaLivro(resultSet)
                return livro
            else:
                return None
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar aluno. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

    
    def findAll(self)-> List[Livro]:
        cursor=None
        try:
            cursor= self.conn.cursor()
            cursor.execute("SELECT * FROM livros")
            resultSetList=cursor.fetchall()
            if resultSetList:
               return [self._instaciaLivro(resultSet) for resultSet in resultSetList] 
            return None

        except sql.Error as erro:
            raise DbException(f"Erro ao buscar todos os livros. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)



    def _instaciaLivro(self,resultSet) -> Livro:
        livro= Livro(resultSet[0],resultSet[1],resultSet[2],resultSet[3])
        return livro