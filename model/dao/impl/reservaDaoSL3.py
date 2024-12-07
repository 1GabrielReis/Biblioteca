from typing import List
import sqlite3 as sql
import datetime

from model.entities.reserva import Reserva
from model.dao.reservaDao import ReservaDao

from model.entities.livro import Livro
from model.entities.aluno import Aluno

from db.db import DB
from db.dbException import DbException

class ReservaDaoSL3(ReservaDao):
    def __init__(self,conn):
        super().__init__()
        self.conn = conn
    
    
    def insert(self,reserva: Reserva):
        pass

    
    def update(self,reserva: Reserva):
        pass

    
    def deleteById(self,id: int):
        pass

    
    def findById(self,id: int):
        pass

    
    def findAll(self) -> List[Reserva]:
        cursor= None
        try:
            cursor=self.conn.cursor()
            cursor.execute('''
                            SELECT
                            Reservas.id_reserva, Reservas.data_inicial, Reservas.data_final, Reservas.data_entregue,  
                            Reservas.id_livro, livros.id_livro, livros.titulo, livros.autor, livros.editora,
                            Reservas.id_aluno, alunos.id_usuario, alunos.nome, alunos.sobrenome
                            FROM Reservas
                            INNER JOIN livros ON Reservas.id_livro =  livros.id_livro
                            INNER JOIN alunos ON Reservas.id_aluno = alunos.id_usuario;
                           ''')
            resultSetList= cursor.fetchall()
            listaReserva= List()
            dicioanrioLivros= {}
            dicioanrioAluno= {}
            for resultSet in resultSetList:
                if resultSet[4] not in dicioanrioLivros:
                    livro= self._instanciaLivro(resultSet)
                    dicioanrioLivros.update({resultSet[4]:livro})
                if resultSet[9] not in dicioanrioAluno:
                    aluno= self._instanciaAluno(resultSet)
                    dicioanrioAluno.update({resultSet[9]: aluno})
                listaReserva.append(self._instanciaReserva(resultSet,dicioanrioLivros[resultSet[4]],dicioanrioAluno[resultSet[9]]))
            return listaReserva
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar todas reserva. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

    def findByLivro(self) -> List[Livro]:
        pass

    
    def findByAluno(self) -> List[Aluno]:
        pass
    
    def _instanciaLivro(self, resultSet):
        id_livro, titulo, autor, editora = resultSet[5], resultSet[6], resultSet[7], resultSet[8]
        return Livro(id_livro, titulo, autor, editora)

    def _instanciaAluno(self, resultSet):
        id_usuario, nome, sobrenome= resultSet[10], resultSet[11], resultSet[12]
        return Aluno(id_usuario, nome, sobrenome)

    def _instanciaReserva(self, resultSet, livro: Livro, aluno: Aluno):
        id_reserva, data_inicial, data_final, data_entregue =  resultSet[0], resultSet[1], resultSet[2], resultSet[3]
        return Reserva(id_reserva,livro,aluno,data_inicial,data_final,data_entregue)