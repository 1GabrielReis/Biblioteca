from typing import List
import sqlite3 as sql

from model.entities.biblioteca import Biblioteca
from model.dao.bibliotecaDao import BibliotecaDao

from model.entities.aluno import Aluno

from db.db import DB
from db.dbException import DbException

class BibliotecaDaoSL3(BibliotecaDao):
    
    def __init__(self,conn):
        super().__init__()
        self.conn= conn

    def insert(self,biblioteca: Biblioteca):
        pass

    
    def update(self,biblioteca: Biblioteca):
        pass

   
    def deleteById(self,id: int):
        pass

   
    def findById(self,id: int):
        pass

   
    def findAll(self,biblioteca: List[Biblioteca]):
        cursor= None
        try:
            cursor=self.conn.cursor()
            cursor.execute('''
                            SELECT    avaliar_biblioteca.*  AS biblioteca, alunos.*
                            FROM avaliar_biblioteca
                            INNER JOIN  alunos
                            ON biblioteca.id_aluno = alunos.id_usuario  
                           ''')
            resultSetList= cursor.fetchall()           
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar todas avaliaçoes. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)


    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        pass


    def _instaciarBiblioteca(self, resultSet) -> Biblioteca:
        id_biblioteca,nota,id_aluno= resultSet