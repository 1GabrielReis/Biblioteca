from abc import ABC, abstractmethod
from typing import List

from model.entities.livro import Livro
from model.dao.daoFactory import DaoFactory
from model.dao.livroDao import LivroDao

ativo= True
livroDao= DaoFactory.createLivroDao()

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


def escolha():
    print("""
                  Menu
          Digite sua escolha:
          1- Adicionar livro 
          2- altera livro 
          3- Excluir livro
          4- encontrar livro
          5- Listar livros
          6- Sair do sistema
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
        ativo= False
    else:
        print('Escolha invalida')
    return ativo

while ativo:
    ativo= sistema()