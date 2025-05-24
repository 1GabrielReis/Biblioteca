from typing import List

from ..model.entities.aluno import Aluno
from ..model.entities.livro import Livro
from ..model.entities.reserva import Reserva
from ..model.entities.avaliacao import Avaliacao
from ..model.dao.avaliacaoDao import AvaliacaoDao
from ..model.dao.daoFactory import DaoFactory

from ..schemas.avaliacao_schema import Avaliacao_Schema

from .serviceException import ServiceException
from .reservaService import ReservaService
from .alunoService import AlunoService
from .livroService import LivroService



class AvaliacaoService(AvaliacaoDao):
    def __init__(self):
        super().__init__()
        self.avaliacaoDao= DaoFactory.createAvaliacaoDao()
    
    def insert(self,avaliacao: Avaliacao):
        try:
            return self.avaliacaoDao.insert(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao inserir avaliação do livro.\nDetalhes: {e}")

    def update(self,avaliacao: Avaliacao):
        try:
            return self.avaliacaoDao.update(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao atualizar avaliação do livro.\nDetalhes: {e}")

    def deleteById(self,id: int):
        try:
            return self.avaliacaoDao.deleteById(int)
        except Exception as e:
            raise ServiceException(f"Erro ao deletar avaliação do livro {id}.\nDetalhes: {e}")

    def findById(self,id: int):
        try:
            return self.avaliacaoDao.findById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar avaliação do livro {id}.\nDetalhes: {e}")

    def findAll(self) -> List[Avaliacao]:
        try:
            return self.avaliacaoDao.findAll()
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todas avaliações dos livros. \nDetalhes: {e}")

    def findByAluno(self, avaliacao) -> List[Avaliacao]:
        try:
            return self.avaliacaoDao.findByAluno(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as avalições de livros do aluno\nDetalhes: {e}")

    def findByLivro(self, avaliacao) -> List[Avaliacao]:
        try:
            return self.avaliacaoDao.findByLivro(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos avaliaçoes do livro\nDetalhes: {e}")

    def findByReserva(self, avaliacao) -> List[Avaliacao]:
        try:
            return self.avaliacaoDao.findByReserva(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos avaliaçoes de livros reservado \nDetalhes: {e}")
        
    def instance_reserva(self, avaliacao: Avaliacao_Schema ,id: int = None):
        try:
            reservaDao=  ReservaService()
            reserva: Reserva= reservaDao.findById(avaliacao.reserva)
            livro: Livro= reserva.livro
            aluno: Aluno= reserva.aluno
            nota= avaliacao.nota
            return Avaliacao(id= id, nota= nota, aluno= aluno, livro= livro, reserva= reserva)
        except Exception as e:
            raise ServiceException(f"Erro ao instanciar avaliação \nDetalhes: {e}")
