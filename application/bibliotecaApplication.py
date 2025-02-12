
from typing import List
from abc import ABC, abstractmethod

from model.entities.aluno import Aluno
from model.entities.biblioteca import Biblioteca
from model.dao.daoFactory import DaoFactory
from model.dao.bibliotecaDao import BibliotecaDao


ativo= True
bibliotecaDao = DaoFactory.createBibliotecaDao()

def insert():
    print('Teste insert')
    nota=int(input('Uma nota de 0 a 10 em relaçao ao atendimento da biblioteca: '))
    id_aluno=(input('Qual o Id do aluno: '))
    aluno = Aluno(id_aluno,None,None)
    biblioteca= Biblioteca(None,nota,aluno)
    bibliotecaDao.insert(biblioteca)
    print("Inserido! novo Id: ", biblioteca.id)
    print(biblioteca)

    
def update():
    print('Teste update')
    id_biblioteca= int(input('Qual o id da avaliação da biblioteca: '))
    biblioteca= bibliotecaDao.findById(id_biblioteca)
    atributo=int(input("""
                   Qual atributo você desja alterar:
                   1- nota da avalição
                   2- id do aluno
                   """))
    if atributo == 1:
        biblioteca.nota=int(input('Qual a nota de avaliação da biblioteca: '))
    else:
        biblioteca.aluno.id=int(input('Qual o ID do aluno: '))
    bibliotecaDao.update(biblioteca)
    biblioteca= bibliotecaDao.findById(id_biblioteca)
    print(biblioteca)

def deleteById():
    print('Teste delete By Id')
    id_biblioteca=int(input('ID da avaliação da biblioteca: '))
    bibliotecaDao.deleteById(id_biblioteca)
    print('Delete realizado com sucesso! ')


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
    print('find By Aluno')
    id_aluno=int(input('Qual o ID do aluno para encontra sua avaliação da biblioteca: '))
    aluno= Aluno(id_aluno,None,None)
    biblioteca = bibliotecaDao.findByAluno(aluno)
    print(biblioteca)


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