
class Livro: 
    def __init__(self,id,titulo,autor,editora):
        self.id=id
        self.titutlo= titulo
        self.autor= autor 
        self.editora= editora 

    def __str__(self) -> str:
        return f"({self.id},{self.titutlo},{self.autor},{self.editora})"

    def __repr__(self) -> str:
        self.__str__()