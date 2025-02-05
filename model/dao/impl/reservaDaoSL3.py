from typing import List
import sqlite3 as sql
from datetime import datetime

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
        cursor= None
        try:
            data_inicial= self._converteDataTextoSQL(reserva.data_inicio)
            data_final= self._converteDataTextoSQL(reserva.data_final)
            id_aluno= reserva.aluno.id
            id_livro= reserva.livro.id
            cursor= self.conn.cursor()
            cursor.execute('''INSERT INTO Reservas(data_inicial, data_final, id_aluno, id_livro) 
                          VALUES (?, ?, ?, ?)''',
                         (data_inicial, data_final, id_aluno, id_livro))
            self.conn.commit()
            if cursor.rowcount > 0:
                reserva.id=cursor.lastrowid
            else:
                raise DbException(f"Erro, não foi possivel inserir os dados")
        except sql.Error as erro:
            raise DbException(f"Erro ao Reserva. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)
            
            

    def update(self,reserva: Reserva):
        cursor = None
        try:
            reserva_id= reserva.id
            data_inicial= self._converteDataTextoSQL(reserva.data_inicio)
            data_final= self._converteDataTextoSQL(reserva.data_final)
            data_entregue= self._converteDataSQL(reserva.data_entregue)
            id_aluno= reserva.aluno.id
            id_livro= reserva.livro.id
            cursor= self.conn.cursor()
            cursor.execute('''
                            UPDATE Reservas SET 
                            data_inicial = ?,
                            data_final = ?,
                            data_entregue = ?,
                            id_aluno = ?,
                            id_livro = ?
                            WHERE id_reserva = ?''',
                            (data_inicial, data_final, data_entregue,
                             id_aluno, id_livro, reserva_id))
            self.conn.commit()
        except sql.Error as erro:
            raise DbException(f"Erro ao atualizar reserva. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)

    
    def deleteById(self,id: int):
        cursor= None 
        try:
            cursor= self.conn.cursor()
            cursor.execute('DELETE FROM Reservas WHERE id_reserva = ?',(id,))
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
            cursor= self.conn.execute('''
                            SELECT
                            Reservas.id_reserva, Reservas.data_inicial, Reservas.data_final, Reservas.data_entregue,  
                            Reservas.id_livro, livros.id_livro, livros.titulo, livros.autor, livros.editora,
                            Reservas.id_aluno, alunos.id_usuario, alunos.nome, alunos.sobrenome
                            FROM Reservas
                            INNER JOIN livros ON Reservas.id_livro =  livros.id_livro
                            INNER JOIN alunos ON Reservas.id_aluno = alunos.id_usuario
                            WHERE id_reserva = ?;
                            ''', (id,))
            resultSet=cursor.fetchone()
            if resultSet is not None:
                livro= self._instanciaLivro(resultSet)
                aluno= self._instanciaAluno(resultSet)
                return self._instanciaReserva(resultSet,livro,aluno)
            return None
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar reserva. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)  

    def findAll(self) -> List[Reserva]:
        cursor= None
        try:
            cursor=self.conn.cursor()
            resultSetList='''
                            SELECT
                            Reservas.id_reserva, Reservas.data_inicial, Reservas.data_final, Reservas.data_entregue,  
                            Reservas.id_livro, livros.id_livro, livros.titulo, livros.autor, livros.editora,
                            Reservas.id_aluno, alunos.id_usuario, alunos.nome, alunos.sobrenome
                            FROM Reservas
                            INNER JOIN livros ON Reservas.id_livro =  livros.id_livro
                            INNER JOIN alunos ON Reservas.id_aluno = alunos.id_usuario;
                        '''
            listaReserva= list()
            dicioanrioLivros= {}
            dicioanrioAluno= {}
            for resultSet in cursor.execute(resultSetList):
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
    
 
    def findByLivro(self, livro: Livro):
        cursor= None
        try:
            id_livro= livro.id
            cursor= self.conn.cursor()
            resultSetList=  cursor.execute( '''
                                SELECT
                                Reservas.id_reserva, Reservas.data_inicial, Reservas.data_final, Reservas.data_entregue,  
                                Reservas.id_livro, livros.id_livro, livros.titulo, livros.autor, livros.editora,
                                Reservas.id_aluno, alunos.id_usuario, alunos.nome, alunos.sobrenome
                                FROM Reservas
                                INNER JOIN livros ON Reservas.id_livro =  livros.id_livro
                                INNER JOIN alunos ON Reservas.id_aluno = alunos.id_usuario
                                WHERE Reservas.id_livro = ?
                                ORDER BY nome
                            ''',(id_livro,))
            listaReserva= []
            dicionarioAluno= {}
            dicionarioLivro= {}
            for resultSet in resultSetList:
                if resultSet[9] not in dicionarioAluno:
                    dicionarioAluno.update({resultSet[9]: self._instanciaAluno(resultSet)})
                if resultSet[4] not in dicionarioLivro:
                    dicionarioLivro.update({resultSet[4]: self._instanciaLivro(resultSet)})
                listaReserva.append(self._instanciaReserva(resultSet,dicionarioLivro[resultSet[4]],dicionarioAluno[resultSet[9]]))
            return listaReserva
        except sql.Error as erro:
            raise DbException(f"Erro ao buscar todas reserva. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)            

    
    def findByAluno(self, aluno: Aluno):
        cursor= None
        try:
            id_aluno= aluno.id
            cursor= self.conn.cursor()
            cursor.execute('''
                            SELECT
                            Reservas.id_reserva, Reservas.data_inicial, Reservas.data_final, Reservas.data_entregue,  
                            Reservas.id_livro, livros.id_livro, livros.titulo, livros.autor, livros.editora,
                            Reservas.id_aluno, alunos.id_usuario, alunos.nome, alunos.sobrenome
                            FROM Reservas
                            INNER JOIN livros ON Reservas.id_livro =  livros.id_livro
                            INNER JOIN alunos ON Reservas.id_aluno = alunos.id_usuario
                            WHERE Reservas.id_aluno= ?''',(id_aluno,))
            resultSetList= cursor.fetchall()
            listaReserva= list()
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
            raise DbException(f"Erro ao retona lsita de reservas. \nDetalhes: {erro}")
        finally:
            DB.closeCursor(cursor)
    
    def _instanciaLivro(self, resultSet):
        id_livro, titulo, autor, editora = resultSet[5], resultSet[6], resultSet[7], resultSet[8]
        return Livro(id_livro, titulo, autor, editora)

    def _instanciaAluno(self, resultSet):
        id_usuario, nome, sobrenome= resultSet[10], resultSet[11], resultSet[12]
        return Aluno(id_usuario, nome, sobrenome)
    
    def _instanciaReserva(self, resultSet, livro: Livro, aluno: Aluno):
        id_reserva, data_inicial, data_final, data_entregue =  resultSet[0], resultSet[1], resultSet[2], resultSet[3]
        return  Reserva(id_reserva,livro,aluno,self._converteDataSQL(data_inicial),self._converteDataSQL(data_final),self._converteDataSQL(data_entregue))
         
    def _converteDataSQL(self,dataHora):
        if dataHora is not None:
            return datetime.strptime(dataHora,"%Y-%m-%d %H:%M:%S")
       
    def _converteDataTextoSQL(self, data: datetime):
        if data is not None:
            return data.strftime("%Y-%m-%d %H:%M:%S")
        return None
    
    def _converteDataTexto(self,data):
        if data is not None:
            return datetime.strptime(data,'%d/%m/%Y')
        return None