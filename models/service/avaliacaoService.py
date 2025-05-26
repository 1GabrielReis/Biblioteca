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
            avaliacoes = self.findAll()
            for avaliacao1 in avaliacoes:
                if avaliacao.reserva.id == avaliacao1.reserva.id:
                    raise ServiceException(f"O livro {avaliacao.livro} já foi avaliado referente ao registro de reserva {avaliacao.reserva.id}")
            return self.avaliacaoDao.insert(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao inserir avaliação do livro.\nDetalhes: {e}")

    def update(self,avaliacao: Avaliacao):
        try:
            avaliacao_bco: Avaliacao= self.findById(avaliacao.id)
            if avaliacao_bco.reserva.id != avaliacao.reserva.id:
                raise ServiceException("Não é permitido alterar a reserva de uma avaliação já cadastrada.")
            return self.avaliacaoDao.update(avaliacao)
        except Exception as e:
            raise ServiceException(f"Erro ao atualizar avaliação do livro.\nDetalhes: {e}")

    def deleteById(self,id: int):
        try:
            return self.avaliacaoDao.deleteById(id)
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

    def findByAluno(self, id: int):
        try:
            return self.avaliacaoDao.findByAluno(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as avalições de livros do aluno\nDetalhes: {e}")

    def findByLivro(self, id: int) -> List[Avaliacao]:
        try:
            return self.avaliacaoDao.findByLivro(id= id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos avaliaçoes do livro\nDetalhes: {e}")

    def findByReserva(self, id: int) -> List[Avaliacao]:
        try:
            return self.avaliacaoDao.findByReserva(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos avaliaçoes de livros reservado \nDetalhes: {e}")
                
    def instance_avaliacao(self, avaliacao: Avaliacao_Schema, id: int = None):
        try:
           nota= avaliacao.nota
           reserva: Reserva = ReservaService().findById(avaliacao.reserva)
           return Avaliacao(
               id= id,
               nota= nota,
               aluno= reserva.aluno,
               livro= reserva.livro,
               reserva= reserva
           )
        except Exception as e:
            raise ServiceException(f"Erro ao instanciar avaliação \nDetalhes: {e}")
