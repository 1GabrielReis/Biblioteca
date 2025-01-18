from typing import List
from abc import ABC, abstractmethod
import datetime

from model.entities.livro import Livro
from model.entities.aluno import Aluno
from model.entities.reserva import Reserva
from model.dao.daoFactory import DaoFactory
from model.dao.reservaDao import Reserva


ativo= True
reservaDao = DaoFactory.createReservaDao()

def insert():
    print("test insert")
    id_aluno=input('Qul o Id do aluno: ')
    id_livro=input('Qual o Id do Livro: ')
    text_data=['Data reservada: ', 'Data de entrega: ']
    data_reserva=[]
    for texto in text_data:
        print(texto)
        dia= int(input('Dia: '))
        mes= int(input('Mes: '))
        ano= int(input('Ano: '))
        data_reserva.append('{}/{}/{}'.format(dia,mes,ano))
    aluno=Aluno(id_aluno, None, None)
    livro=Livro(id_livro, None, None, None)
    reserva=Reserva(None,livro,aluno,data_reserva[0],data_reserva[1],None)
    reservaDao.insert(reserva)
    print(f"Inserido! novo Id: {reserva.id} \n{reserva}")
    


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