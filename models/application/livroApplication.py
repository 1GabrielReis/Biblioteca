
from abc import ABC, abstractmethod
from typing import List

from model.entities.livro import Livro
from service.livroService import LivroService

ativo= True
livroDao= LivroService()

def insert():
    print('Teste insert')
    titulo=input("Titulo o livro: ")
    autor=input("Autor do livro: ")
    editora=input("Editora do livro: ")
    livro= Livro(None,titulo, autor,editora)
    livroDao.insert(livro)
    print("Inserido! novo Id: ", livro.id)
    print(livro)

def update():
    print('Teste update')
    id_livro=int(input("Id do livro: "))
    livro: Livro= livroDao.findById(id_livro)
    atributo=int(input("""
                   Qual atributo você desja alterar:
                   1- titulo
                   2- autor 
                   3- editora 
                   """))
    if atributo == 1:
        livro.titutlo= input("Qual o nome do livro: ")
    elif atributo == 2:
        livro.autor= input("Qual o nome do autor do livro: ")
    else:
        livro.editora= input("Qual a ditora do livro: ")
    livroDao.update(livro)
    print(livro)




def deleteById():
    print('Teste find By Id')
    id_livro=int(input("Id do livro: "))
    livroDao.deleteById(id_livro)
    print('Delete realizado com sucesso! ')
    pass

def findById():
    print('Teste find By Id')
    id_livro=int(input("Id do livro: "))
    livro: Livro= livroDao.findById(id_livro)
    print(livro)

def findAll():
    print('Teste find all')
    livros: list[Livro] = livroDao.findAll()
    print(livros)


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