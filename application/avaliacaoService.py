from typing import List

from model.entities.avaliacao import Avaliacao
from model.entities.aluno import Aluno
from model.entities.biblioteca import Biblioteca
from model.entities.reserva import Reserva
from model.dao.daoFactory import DaoFactory

ativo= True
avaliacaoDao= DaoFactory.createAvaliacaoDao()

def insert(self,avaliacao: Avaliacao):
    pass

def update(self,avaliacao: Avaliacao):
    pass

def deleteById(self,id: int):
    pass

def findById(self,id: int):
    pass

def findAll(self) -> List[Avaliacao]:
    pass

def findByAluno(self, avaliacao) -> List[Avaliacao]:
    pass

def findByLivro(self, avaliacao) -> List[Avaliacao]:
    pass

def findByReserva(self, avaliacao) -> List[Avaliacao]:
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
