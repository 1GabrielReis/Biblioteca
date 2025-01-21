from typing import List
from abc import ABC, abstractmethod
from datetime import datetime

from model.entities.livro import Livro
from model.entities.aluno import Aluno
from model.entities.reserva import Reserva
from model.dao.daoFactory import DaoFactory
from model.dao.reservaDao import Reserva

class ClassAbstrata(ABC):
    @abstractmethod
    def _converteDataTexto(self):
        pass

class DataTempo(ClassAbstrata):
    def _converteDataTexto(self,data):
        if data is not None:
            return datetime.strptime(data,'%d/%m/%Y')

ativo= True
reservaDao = DaoFactory.createReservaDao()
converteDataTempo= DataTempo()

def insert():
    pass
    #livro= Livro(6,None,None,None)
    #aluno= Aluno(6,None,None)
    #data_inicial=converteDataTempo._converteDataTexto('20/01/2025')
    #print(data_inicial)
    #data_final=converteDataTempo._converteDataTexto('20/02/2025')
    #print(data_final)
    #data_entregue=converteDataTempo._converteDataTexto('15/02/2025')
    #print(data_entregue)
    #reserva= Reserva(1, livro, aluno, data_inicial, data_final, data_entregue)
    #print(reserva)
    #reserva= Reserva(livro,aluno,data_inicial,data_final,data_entregue)
    #reserva1='20/01/2025'
    #print(reserva1)
    #reserva2=converteDataTempo._converteDataTexto(reserva1)
    #print(reserva2)
    #print('Fim')



def update():
    pass


def deleteById():
    print("test deleteById")
    id_reserva=int(input('Id da reserva: '))
    reservaDao.deleteById(id_reserva)
    print('Delete realizado com sucesso! ')


def findById():
    print('test find by id')
    id_reserva= int(input('Qual o Id da reserva: '))
    reserva= reservaDao.findById(id_reserva)
    print(reserva)



def findAll():
    print('test find All')
    reserva: Reserva= reservaDao.findAll()
    print(reserva)


def findByLivro() :
    pass


def findByAluno():
    pass

def escolha():
    print("""
                  Menu
          Digite sua escolha:
          1- Adiconar reserva  
          2- Altera reserva
          3- Excluir reserva
          4- Encontrar reserva
          5- Listar de reserva
          6- Lista de livros reservado
          7- Lista de alunos que reservaram
          8- Sair do sistema
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
        findByLivro()
    elif resposta == 7:
        findByAluno()
    elif resposta == 8:
        ativo= False    
    else:
        print('Escolha invalida')
    return ativo

while ativo:
    ativo= sistema()