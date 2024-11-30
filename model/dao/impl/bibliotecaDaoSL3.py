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
                            SELECT avaliar_biblioteca.*, alunos.*
                            FROM avaliar_biblioteca
                            INNER JOIN  alunos
                            ON avaliar_biblioteca.id_aluno = alunos.id_usuario  
                           ''')
            resultSetList= cursor.fetchall()
            listaBiblioteca= list()
            dicioanrioAluno= {}
            for resultSet in resultSetList:
                if resultSet[2] not in dicioanrioAluno:
                    dicioanrioAluno.update({resultSet[2]:self._instanciaAluno(resultSet)})
                
                listaBiblioteca.append(self._instanciaBiblioteca(resultSet,dicioanrioAluno[resultSet[2]]))
            return listaBiblioteca
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar todas avaliaçoes. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)


    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        pass


    def _instanciaBiblioteca(self, resultSet, aluno) -> Biblioteca:
        id_biblioteca, nota= resultSet[0], resultSet[1]
        return Biblioteca(id_biblioteca,nota,aluno)

    def _instanciaAluno(self,resultSet) -> Aluno:
        id_aluno,nome, sobrenome= resultSet[3], resultSet[4], resultSet[5]
        return Aluno(id_aluno, nome, sobrenome)
