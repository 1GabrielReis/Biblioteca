from typing import List

from ..model.entities.aluno import Aluno
from ..model.dao.alunoDao import AlunoDao

from ..model.dao.daoFactory import DaoFactory

class AlunoService(AlunoDao):
    def __init__(self):
        super().__init__()
        self.alunoDao= DaoFactory.createAlunoDao()

    def insert(self,aluno: Aluno):
        return self.alunoDao.insert(aluno)

    def update(self,aluno: Aluno):
        return self.alunoDao.update(aluno)

    def deleteById(self,id: int):
        return self.alunoDao.deleteById(id)

    def findById(self,id: int):
        return self.alunoDao.findById(id)

    def findAll(self) -> List[Aluno]:
        return self.alunoDao.findAll()
