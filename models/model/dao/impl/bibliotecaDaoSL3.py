from typing import List
import sqlite3 as sql

from ...entities.biblioteca import Biblioteca
from ...dao.bibliotecaDao import BibliotecaDao

from ...entities.aluno import Aluno

from ....db.db import DB
from ....db.dbException import DbException

class BibliotecaDaoSL3(BibliotecaDao):
    
    def __init__(self,conn): 
        super().__init__()
        self.conn=conn

    def insert(self,biblioteca: Biblioteca):
        cursor= None 
        try:
            nota=  biblioteca.nota
            id_aluno= biblioteca.aluno.id
            cursor= self.conn.cursor()
            cursor.execute('INSERT INTO avaliar_biblioteca(nota, id_aluno)  VALUES (?, ?)',(nota,id_aluno))
            self.conn.commit()
            if cursor.rowcount > 0:
                biblioteca.id=cursor.lastrowid
            else:
                raise DbException(f"Erro, não foi possivel inserir os dados")
        except sql.Error as erro:
            raise DbException(f"Erro ao cadastrar avaliaçaõ do aluno. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

    
    def update(self,biblioteca: Biblioteca):
        cursor=None
        try:
            id_biblioteca= biblioteca.id
            nota=biblioteca.nota
            id_aluno=biblioteca.aluno.id
            cursor=self.conn.cursor()
            cursor.execute('''UPDATE avaliar_biblioteca
                            SET nota = ?, id_aluno = ?
                            WHERE id_biblioteca = ?''',(nota,id_aluno,id_biblioteca))
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao atualizar avaliação. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

   
    def deleteById(self,id: int):
        cursor= None
        try:
            cursor= self.conn.cursor()
            cursor.execute('DELETE FROM avaliar_biblioteca WHERE id_biblioteca = ?',(id,))
            self.conn.commit()
            if cursor.rowcount == 0:
                raise DbException(f"ID não encontrado")
        except sql.Error as erro:
            raise DbException(f"Erro ao deletar avaliação. \n Detalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

   
    def findById(self,id: int):
        cursor= None
        try:
            cursor=self.conn.cursor()
            cursor.execute('''
                            SELECT 
                            avaliar_biblioteca.id_biblioteca, avaliar_biblioteca.nota, avaliar_biblioteca.id_aluno,
                            alunos.id_usuario, alunos.nome, alunos.sobrenome  
                            FROM avaliar_biblioteca
                            INNER JOIN alunos
                            ON avaliar_biblioteca.id_aluno = alunos.id_usuario
                            WHERE id_biblioteca = ?
                           ''',(id,))
            resultSet= cursor.fetchone()
            if resultSet is not None:
                aluno=self._instanciaAluno(resultSet)
                return self._instanciaBiblioteca(resultSet,aluno)
            return None
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar avaliação. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)  

   
    def findAll(self) -> List[Biblioteca]:
        cursor= None
        try:
            cursor= self.conn.cursor()
            cursor.execute('''
                            SELECT 
                            avaliar_biblioteca.id_biblioteca, avaliar_biblioteca.nota, avaliar_biblioteca.id_aluno,
                            alunos.id_usuario, alunos.nome, alunos.sobrenome  
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


    def findByAluno(self,id: int):
        cursor=None
        try:
            cursor= self.conn.cursor()
            cursor.execute('''
                            SELECT
                            avaliar_biblioteca.id_biblioteca, avaliar_biblioteca.nota, avaliar_biblioteca.id_aluno,
                            alunos.id_usuario, alunos.nome, alunos.sobrenome 
                            FROM  avaliar_biblioteca
                            INNER JOIN  alunos
                            ON avaliar_biblioteca.id_aluno = alunos.id_usuario  
                            WHERE alunos.id_usuario = ? 
                            ORDER BY nome
                            ''',(id,))
            resultSetList= cursor.fetchall()
            listaBiblioteca= list()
            dicioanrioAluno= {}
            for resultSet in resultSetList:
                if resultSet[2] not in dicioanrioAluno:
                    dicioanrioAluno.update({resultSet[2]:self._instanciaAluno(resultSet)})
                
                listaBiblioteca.append(self._instanciaBiblioteca(resultSet,dicioanrioAluno[resultSet[2]]))
            return listaBiblioteca
        except sql.Error as erro:
            raise DbException(f"Erro ao retona lsita de avaliação. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)


    def _instanciaBiblioteca(self, resultSet, aluno) -> Biblioteca:
        id_biblioteca, nota= resultSet[0], resultSet[1]
        return Biblioteca(id_biblioteca,nota,aluno)

    def _instanciaAluno(self,resultSet) -> Aluno:
        id_aluno, nome, sobrenome= resultSet[3], resultSet[4], resultSet[5]
        return Aluno(id_aluno, nome, sobrenome)
