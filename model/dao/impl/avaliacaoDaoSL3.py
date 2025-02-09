from typing import List
import sqlite3 as sql

from model.entities.avaliacao import Avaliacao
from model.dao.avaliacaoDao import AvaliacaoDao

from model.entities.aluno import Aluno
from model.entities.livro import Livro
from model.entities.reserva import Reserva

from db.db import DB
from db.dbException import DbException

class AvaliacaoDaoSL3(AvaliacaoDao):
    def __init__(self, conn):
        super().__init__()
        self.conn= conn

    def insert(self,avaliacao: Avaliacao):
        pass

    def update(self,avaliacao: Avaliacao):
        pass

    def deleteById(self,id: int):
        pass

    def findById(self,id: int):
        pass

    def findAll(self) -> List[Avaliacao]:
        cursor= None
        try:
            cursor= self.conn.cursor()
            resultSetList='''
                            SELECT 
                            avaliar_livro.id_avaliar, avaliar_livro.nota,
                            avaliar_livro.id_aluno, alunos.id_usuario, alunos.nome, alunos.sobrenome, 
                            avaliar_livro.id_livro, livros.id_livro, livros.titulo, livros.autor, livros.editora, 
                            avaliar_livro.id_reserva, Reservas.id_reserva, Reservas.data_inicial,  Reservas.data_final, Reservas.data_entregue, Reservas.id_aluno, Reservas.id_livro
                            FROM avaliar_livro
                            INNER JOIN alunos ON avaliar_livro.id_aluno = alunos.id_usuario
                            INNER JOIN livros ON avaliar_livro.id_livro = livros.id_livro
                            INNER JOIN Reservas ON avaliar_livro.id_reserva = Reservas.id_reserva;
                           '''
            listaAvalicoes= List()
            bibliotecaAluno= {}
            bibliotecaLivro= {}
            bibliotecaReserva= {}
            for resultSet in cursor.execute(resultSetList):
                if resultSet[2] not in bibliotecaAluno:
                    pass
                if resultSet[6] not in bibliotecaLivro:
                    pass
                if resultSet[11] not in bibliotecaReserva:
                    pass
                listaAvalicoes.append()
            return(listaAvalicoes)
        except:
            pass
        finally:
            DB.closeCursor(cursor)

    def findByAluno(self, avaliacao) -> List[Avaliacao]:
        pass

    def findByLivro(self, avaliacao) -> List[Avaliacao]:
        pass

    def findByReserva(self, avaliacao) -> List[Avaliacao]:
        pass
