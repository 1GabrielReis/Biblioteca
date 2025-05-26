from typing import List

from ..model.entities.avaliacao import Avaliacao
from ..model.entities.aluno import Aluno
from ..model.entities.livro import Livro
from ..model.entities.reserva import Reserva

from ..service.avaliacaoService import AvaliacaoService

ativo= True
avaliacaoDao= AvaliacaoService()

def insert():
    print('Test insert')
    id_aluno= int(input('Id do aluno: '))
    id_livro= int(input('Id do livro: '))
    id_reserva= int(input('Id da reserva: '))
    nota_livro= int(input('Nota ao livro: '))
    aluno= Aluno(id_aluno, None, None)
    livro= Livro(id_livro, None, None, None)
    reserva= Reserva(id_reserva, None, None, None, None, None)
    avaliacao= Avaliacao(None, nota_livro, aluno, livro, reserva)
    avaliacaoDao.insert(avaliacao)
    print("Inserido! novo Id: ", avaliacao.id)

def update():
    print('updat')
    id_avaliacao=int(input('Id da avalição do livro: '))
    avaliacao: Avaliacao= avaliacaoDao.findById(id_avaliacao)
    atributo=int(input("""
                   Qual atributo você desja alterar:
                   1- nota do livro
                   2- id do aluno
                   3- id do livro
                   4- id do reserva
                   """))
    if atributo == 1:
        avaliacao.nota= int(input('Qual a avalição do '+ avaliacao.livro.titutlo +': '))
    elif atributo == 2:
        avaliacao.aluno.id= int(input('Qual o id do aluno: '))
    elif atributo == 3:
        avaliacao.livro.id= int(input('Qual O ID do livro: '))
    elif atributo == 4:
        avaliacao.reserva.id= int(input('QuaL O ID da Reserva: '))
    else:
        raise ValueError("Idade inválida. Deve estar entre 1 a 4")
    avaliacaoDao.update(avaliacao)
    avaliacao= avaliacaoDao.findById(id_avaliacao)
    print(avaliacao)

def deleteById():
    print('Test delete By Id')
    id_avalicao=int(input('id da avaliação: '))
    avaliacaoDao.deleteById(id_avalicao)
    print('Delete realizado com sucesso! ')

def findById():
    print('Test find By Id')
    id_avaliacao= int(input(" Qual Id da avalição: "))
    avaliacao= avaliacaoDao.findById(id_avaliacao)
    print(avaliacao)

def findAll():
    print('Test find All')
    avaliacoes: List[Avaliacao]= avaliacaoDao.findAll()
    print(avaliacoes)


def findByAluno():
    print('find By Aluno')
    id_aluno= int(input('Qual o id do aluno: '))
    avaliacoes= avaliacaoDao.findByAluno(id_aluno)
    print(avaliacoes)

def findByLivro():
    print('find By Livro')
    id_livro= int(input('Qual o id do livro: '))
    avaliacoes= avaliacaoDao.findByLivro(id_livro)
    print(avaliacoes)

def findByReserva():
    print("find By Reserva")
    id_reserva= int(input("Qual o id da Reserva: "))
    reserva= Reserva(id_reserva, None, None, None, None, None)
    avaliacoes= avaliacaoDao.findByReserva(reserva)
    print(avaliacoes)

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
