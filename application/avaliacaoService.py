from typing import List

from model.entities.avaliacao import Avaliacao
from model.entities.aluno import Aluno
from model.entities.biblioteca import Biblioteca
from model.entities.reserva import Reserva
from model.dao.daoFactory import DaoFactory

ativo= True
avaliacaoDao= DaoFactory.createAvaliacaoDao()

def insert():
    pass

def update():
    pass

def deleteById():
    pass

def findById():
    print('Test find By Id')
    id_avaliacao= int(input(" QuAL Id da avalição: "))
    avaliacao= avaliacaoDao.findById(id_avaliacao)
    print(avaliacao)

def findAll():
    print('Test find All')
    avaliacoes: List[Avaliacao]= avaliacaoDao.findAll()
    print(avaliacoes)


def findByAluno():
    pass

def findByLivro():
    pass

def findByReserva():
    pass

def escolha():
    print("""
                  Menu
          Digite sua escolha:
          1- Avaliar o livro  
          2- Altera avalição do livro
          3- Excluir avalição do livro
          4- Encontrar avalição do livro
          5- Listar de avalições dos livros
          6- Lista de avaliação por aluno
          7- Lista de avaliação por livro
          8- Lista de avaliação por reserva
          9- Sair do sistema
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
        findByLivro()
    elif resposta == 8:
        findByReserva()
    elif resposta == 9:
        ativo= False
    else:
        print('Escolha invalida')
    return ativo

while ativo:
    ativo= sistema()
