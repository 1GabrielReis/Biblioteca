from typing import List

from .aluno import Aluno
from .biblioteca import Biblioteca

class Biblioteca:
    def __init__(self,id,nota,aluno: Aluno):
        self.id=id
        self.nota=nota
        self.aluno= aluno 

    def media(self, notas: List[Biblioteca]):
        total= sum(nota.nota for nota in notas)
        return total/len(notas)
    
   

    
        


        