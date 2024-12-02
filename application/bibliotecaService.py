
from typing import List
from abc import ABC, abstractmethod

from model.entities.aluno import Aluno
from model.entities.biblioteca import Biblioteca
from model.dao.daoFactory import DaoFactory
from model.dao.bibliotecaDao import BibliotecaDao


ativo= True
bibliotecaDao = DaoFactory.createBibliotecaDao()

def insert():
    pass
    print('Teste insert')
    nota=int(input('Uma nota de 0 a 10 em relaçao ao atendimento da biblioteca: '))
    id_aluno=(input('Qual o Id do aluno: '))
    newAluno = Aluno(id_aluno,None,None)
    BibliotecaDao.insert(nota,newAluno.id)

    

def update():
    pass

def deleteById():
    pass

def findById():
    print('Teste find By Id')
    id_biblioteca=int(input('Qual o id da avaliação: '))
    biblioteca= bibliotecaDao.findById(id_biblioteca)
    print(biblioteca)


def findAll():
    print('Teste find all')
    biblioteca= bibliotecaDao.findAll()
    print(biblioteca)

def findByAluno():
    pass

def escolha():
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