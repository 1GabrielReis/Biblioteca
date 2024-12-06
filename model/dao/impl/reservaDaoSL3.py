from typing import List
import sqlite3 as sql
import datetime

from model.entities.reserva import Reserva
from model.dao.reservaDao import ReservaDao

from model.entities.livro import Livro
from model.entities.aluno import Aluno

from db.db import DB
from db.dbException import DbException

class ReservaDaoSL3(ReservaDao):
    def __init__(self):
        super().__init__()
    
    
    def insert(self,reserva: Reserva):
        pass

    
    def update(self,reserva: Reserva):
        pass

    
    def deleteById(self,id: int):
        pass

    
    def findById(self,id: int):
        pass

    
    def findAll(self) -> List[Reserva]:
        pass

    
    def findByLivro(self) -> List[Livro]:
        pass

    
    def findByAluno(self) -> List[Aluno]:
        pass
    