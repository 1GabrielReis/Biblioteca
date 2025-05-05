from ...db.db import DB
from .impl.alunoDaoSL3 import AlunoDaoSL3
from .impl.livroDaoSL3 import LivroDaoSL3
from .impl.bibliotecaDaoSL3 import BibliotecaDaoSL3
from .impl.reservaDaoSL3 import ReservaDaoSL3
from .impl.avaliacaoDaoSL3 import AvaliacaoDaoSL3

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