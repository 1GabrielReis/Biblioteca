class Aluno:
    def __init__(self,nome,sobrenome,id=None):
        self.id=id
        self.nome= nome 
        self.sobrenome=sobrenome 

    def __str__(self): # serve para situação simples (print())
        return f"({self.id}, {self.nome}, {self.sobrenome})"
    
    def __repr__(self): # serve para ser armazenado em outro objeto(lista,dupla,dicionario) entre outros 
        return self.__str__()