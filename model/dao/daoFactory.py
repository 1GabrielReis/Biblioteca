from db.db import DB
from model.dao.impl.alunoDaoSL3 import AlunoDaoSL3

class DaoFactory:
    def createAlunoDao():
        return  AlunoDaoSL3(DB.getConn())