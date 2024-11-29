from typing import List
import sqlite3

from model.entities.biblioteca import Biblioteca
from model.dao.bibliotecaDao import BibliotecaDao

from model.entities.aluno import Aluno

from db.db import DB
from db.dbException import DbException

class BibliotecaDaoSL3(BibliotecaDao):
    
    def __init__(self,conn):
        super().__init__()
        self.conn= conn

    def insert(self,biblioteca: Biblioteca):
        pass

    
    def update(self,biblioteca: Biblioteca):
        pass

   
    def deleteById(self,id: int):
        pass

   
    def findById(self,id: int):
        pass

   
    def findAll(self,biblioteca: List[Biblioteca]):
        pass
