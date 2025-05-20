from typing import List
from datetime import datetime

from ..model.entities.aluno import Aluno
from ..model.entities.livro import Livro
from ..model.entities.reserva import Reserva
from ..model.dao.reservaDao import ReservaDao
from ..schemas.reserva_Schema import Reserva_Schema

from ..model.dao.daoFactory import DaoFactory

from .serviceException import ServiceException
from .alunoService import AlunoService
from .livroService import LivroService

class ReservaService(ReservaDao):
    def __init__(self):
        super().__init__()
        self.reservaDao= DaoFactory.createReservaDao()

    def insert(self,reserva: Reserva):
        try:
            return self.reservaDao.insert(reserva)
        except Exception as e:
            raise ServiceException(f"Erro ao inserir reserva.\nDetalhes: {e}")

    def update(self,reserva: Reserva):
        try:
            return self.reservaDao.update(reserva)
        except Exception as e:
            raise ServiceException(f"Erro ao atualizar reserva.\nDetalhes: {e}")

    def deleteById(self,id: int):
        try:
            return self.reservaDao.deleteById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao deletar reserva por ID {id}.\nDetalhes: {e}")

    def findById(self,id: int):
        try:
            return self.reservaDao.findById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar reserva por ID {id}.\nDetalhes: {e}")

    def findAll(self) -> List[Reserva]:
        try:
            return self.reservaDao.findAll()
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as reservas. \nDetalhes: {e}")

    def findByLivro(self, id = int) -> List[Livro]:
        try:
            return self.reservaDao.findByLivro(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as reserva por livro \nDetalhes: {e}")

    def findByAluno(self, id = int) -> List[Aluno]:
        try:
            return self.reservaDao.findByAluno(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as reserva por aluno \nDetalhes: {e}")

    def returnBook(self, reserva: Reserva):
        try:
            return self.reservaDao.returnBook(reserva)
        except Exception as e:
            raise ServiceException(f"... \nDetalhes: {e}")
        
    def instance_reserva(self, reserva: Reserva_Schema ,id: int = None):
        try:
            data_inicio = datetime.strptime(reserva.data_inicio,"%Y-%m-%d") if reserva.data_inicio is not None else None
            data_final = datetime.strptime(reserva.data_final,"%Y-%m-%d") if reserva.data_final is not None else None
            data_entregue= datetime.strptime(reserva.data_entregue,"%Y-%m-%d") if reserva.data_entregue is not None else None
            aluno =  AlunoService()
            livro = LivroService()
            return Reserva(id=id,
                            data_inicio= data_inicio,
                            data_final= data_final,
                            data_entregue= data_entregue,
                            aluno= aluno.findById(reserva.aluno),
                            livro= livro.findAll(reserva.livro))
        except Exception as e:
            raise ServiceException(f"Erro ao instanciar Reserva \nDetalhes: {e}")