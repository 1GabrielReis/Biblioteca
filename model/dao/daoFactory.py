from db.db import DB
from model.dao.impl.alunoDaoSL3 import AlunoDaoSL3
from model.dao.impl.livroDaoSL3 import LivroDaoSL3
from model.dao.impl.bibliotecaDaoSL3 import BibliotecaDaoSL3

class DaoFactory:
    def createAlunoDao():
        return  AlunoDaoSL3(DB.getConn())
    
    def createLivroDao():
        return LivroDaoSL3(DB.getConn())
    
    def createBibliotecaDao():
        return BibliotecaDaoSL3(DB.getConn)