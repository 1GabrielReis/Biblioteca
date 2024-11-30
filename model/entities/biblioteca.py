from typing import List

from model.entities.aluno import Aluno

class Biblioteca:
    def __init__(self,id,nota,aluno: Aluno):
        self.id=id
        self.nota=nota
        self.aluno= aluno 

    @staticmethod
    def media(notas: List['Biblioteca']) -> float:
        total= sum(nota.nota for nota in notas)
        return total/len(notas)
    
    def __str__(self) -> str:
        return f"({self.id}, {self.nota}, {self.aluno.id}, {self.aluno.nome})\n"
    
    def __repr__(self) -> str:
        return self.__str__()
    
   

    
        


        