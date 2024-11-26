from typing import List
import sqlite3 as sql

from model.entities.aluno import Aluno
from model.dao.alunoDao import AlunoDao
from db.dbException import DbException
from db.db import DB

class AlunoDaoSL3(AlunoDao):
    def __init__(self,conn): #conn = DB
        super().__init__()
        self.conn=conn

    
    def insert(self,aluno: Aluno):
        cursor=None
        try:
            id_aluno, nome, sobrenome= vars(aluno).values()
            cursor= self.conn.cursor()
            cursor.execute(
                "INSERT INTO alunos(nome, sobrenome) VALUES (?, ?)",
                (nome,sobrenome)
            )
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao cadastrar aluno. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)


    
    def update(self,aluno: Aluno):
        cursor=None
        try:
            id_aluno,nome,sobrenome = vars(aluno).values()
            cursor= self.conn.cursor()
            cursor.execute('''
                            UPDATE alunos
					        SET nome = ?, sobrenome = ? 
					        WHERE id_usuario = ?''',(nome,sobrenome,id_aluno))
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao atualizar aluno. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

    
    def deleteById(self,id: int):
        cursor=None
        try:
            cursor= self.conn.cursor()
            cursor.execute('DELETE FROM alunos WHERE id = ?',(id,))
            self.conn.commit()
            if cursor.rowcount == 0:
                raise DbException(f"ID não encontrado")
        except sql.Error as erro:
            raise DbException(f"Erro ao deletar aluno. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)   

    
    def findById(self,id: int):
        cursor=None
        try:
            cursor= self.conn.cursor()
            cursor.execute('SELECT * FROM alunos WHERE id_usuario = ?',(id,))
            resultSet= cursor.fetchone()
            if resultSet is not None:
                aluno= self._instanciaAluno(resultSet)
                return aluno
            else:
                return None   
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar aluno. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)   
        

    def findAll(self):
        cursor=None
        try:
            cursor= self.conn.cursor()
            cursor.execute('SELECT * FROM alunos')
            resultSetList = cursor.fetchall()
            if resultSetList:
                return [self._instanciaAluno(resultSet) for resultSet in resultSetList]
            return None   

        except sql.Error as erro:
            raise DbException(f"Erro ao buscar todos os alunos. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)


    def _instanciaAluno(self, resultSet):
        id_aluno, nome, sobrenome= resultSet
        aluno= Aluno(id=id_aluno,nome=nome,sobrenome=sobrenome)
        return aluno
        
        

    