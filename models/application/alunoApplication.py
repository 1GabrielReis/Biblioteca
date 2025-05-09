from abc import ABC, abstractmethod
from typing import List

from model.entities.aluno import Aluno
from service.alunoService import AlunoService

ativo= True
alunoDao= AlunoService()

def insert():
    print('Teste insert')
    nome=input("Nome do aluno: ")
    sobrenome=input("Sobrenome do aluno: ")
    aluno=Aluno(id= None,nome=nome, sobrenome=sobrenome)
    alunoDao.insert(aluno)
    print("Inserido! novo Id: ", aluno.id)
    print(aluno)


 
def update():
    print('Teste update')
    id_aluno=int(input('Id do aluno: '))
    aluno: Aluno= alunoDao.findById(id_aluno)
    atributo=int(input("""
                   Qual atributo você desja alterar:
                   1- nome
                   2- sobrenome 
                   """))
    if atributo == 1:
        aluno.nome= input("Qual o nome do aluno: ")
    else:
        aluno.sobrenome= input("Qual o sobrenome do aluno: ")
    alunoDao.update(aluno)
    print(aluno)
    


def deleteById():
    print('Teste delete By Id')
    id_aluno=int(input('Id do aluno: '))
    alunoDao.deleteById(id_aluno)
    print('Delete realizado com sucesso! ')

def findById():
    print('Teste find By Id')
    id_aluno=int(input('Id do aluno: '))
    aluno: Aluno= alunoDao.findById(id_aluno)
    print(aluno)

def findAll():
    print('Teste find all')
    alunos: list[Aluno]= alunoDao.findAll()
    print(alunos)
 

def escolha():
    print("""
                  Menu
          Digite sua escolha:
          1- Adicionar aluno 
          2- altera aluno 
          3- Excluir aluno
          4- encontrar aluno
          5- Listar alunos
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