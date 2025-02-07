from typing import List

from model.entities.avaliacao import Avaliacao
from model.entities.aluno import Aluno
from model.entities.biblioteca import Biblioteca
from model.entities.reserva import Reserva
from model.dao.daoFactory import DaoFactory

ativo= True
avaliacaoDao= DaoFactory.createAvaliacaoDao()

