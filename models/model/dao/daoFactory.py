from db.db import DB
from model.dao.impl.alunoDaoSL3 import AlunoDaoSL3
from model.dao.impl.livroDaoSL3 import LivroDaoSL3
from model.dao.impl.bibliotecaDaoSL3 import BibliotecaDaoSL3
from model.dao.impl.reservaDaoSL3 import ReservaDaoSL3
from model.dao.impl.avaliacaoDaoSL3 import AvaliacaoDaoSL3

class DaoFactory:
    def createAlunoDao():
        return  AlunoDaoSL3(DB.getConn())
    
    def createLivroDao():
        return LivroDaoSL3(DB.getConn())
    
    def createBibliotecaDao():
        return BibliotecaDaoSL3(DB.getConn())
    
    def createReservaDao():
        return ReservaDaoSL3(DB.getConn())
    
    def createAvaliacaoDao():
        return AvaliacaoDaoSL3(DB.getConn())