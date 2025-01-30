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
        
    def _gerarData(self) -> datetime:
        dia= int(input('Dia: '))
        mes= int(input('Mes: '))
        ano= int(input('Ano: '))
        data='{}/{}/{}'.format(dia,mes,ano)
        return self._converteDataTexto(data)    

ativo= True
reservaDao = DaoFactory.createReservaDao()
converteDataTempo= DataTempo()

def insert():
    print('Teste insert')
    id_aluno=int(input("Id do aluno: "))
    aluno= Aluno(id_aluno, None, None)
    id_livro=int(input("Id do livro "))
    livro= Livro(id_livro, None, None, None)
    info_datas=(' Data incial ',' Data final ')
    datas=[]
    for data in info_datas:
        print(data)
        datas.append(converteDataTempo._gerarData())
    data_inicial, data_final= datas = datas
    reserva= Reserva(None, livro, aluno, data_inicial, data_final, None)
    reservaDao.insert(reserva)
    print("Inserido! novo Id: ", reserva.id)
    print(reserva)
    
def update():
    print('Teste update')
    id_reserva= int(input('Qual o id da reserva:'))
    reserva= reservaDao.findById(id_reserva)
    atributo= int(input(
                        '''
                        Qual atributo você deseja alterar
                        1 - Id do aluno 
                        2 - Id do livro
                        3 - Datas da reserva 
                    '''))
    if atributo == 1:
        reserva.aluno.id = int(input('Qual o Id do aluno: '))
    elif atributo == 2:
        reserva.livro.id= int(input('Qual o Id do livro: '))
    elif atributo == 3:
        data= int(input(
                '''
                Qual data você deja altera:
                1 - Data incial 
                2 - Data final 
                3 - Data de entrega 
                ''')) 
        if data == 1:
            print('Qual a data incial: ')
            #reserva.data_inicio = metodo
        elif data == 2:
            print('Qual a data final: ')
            #reserva.data_final = metodo
        elif data == 3:
            print('Qual a data de entraga: ')
            #reserva.data_entregue = metodo
        else:
            raise ValueError("Idade inválida. Deve estar entre 1 a 3")
    else:
        raise ValueError("Idade inválida. Deve estar entre 1 a 3")
    #reservaDao.update(reserva)
    #reserva = reservaDao.findById(id_reserva)
    #print





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

def devolverLivro():
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
          8- Devolver livro 
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
        findByLivro()
    elif resposta == 7:
        findByAluno()
    elif resposta == 8:
        devolverLivro()
    elif resposta == 9:
        ativo= False    
    else:
        print('Escolha invalida')
    return ativo

while ativo:
    ativo= sistema()