from typing import List
from abc import ABC, abstractmethod
import datetime

from model.entities.livro import Livro
from model.entities.aluno import Aluno
from model.entities.reserva import Reserva
from model.dao.daoFactory import DaoFactory
from model.dao.reservaDao import Reserva


ativo= True
bibliotecaDao = DaoFactory.createBibliotecaDao()

def insert():
    
    pass


def update():
    pass


def deleteById():
    pass


def findById():
    pass


def findAll():
    pass


def findByLivro() :
    pass


def findByAluno():
    pass

    print("""
                  Menu
          Digite sua escolha:
          1- Avaliar o atendimento  
          2- Altera avalição do atendiemnto
          3- Excluir avalição do atendiemnto
          4- encontrar avalição do atendiemnto
          5- Listar de avalição do atendiemnto
          6- Lista de aluno que avaliaram o atenmento
          7- Sair do sistema
          """)
    return int(input())

def sistema():
    resposta= escolha()
    ativo = True
    if resposta == 1:
        insert()
    elif resposta == 2:
        update()
    elif resposta == 3:
        deleteById()
    elif resposta == 4:
        findById()
    elif resposta == 5:
        findAll()
    elif resposta == 6:
        findByAluno()
    elif resposta == 7:
        ativo= False
    else:
        print('Escolha invalida')
    return ativo

while ativo:
    ativo= sistema()