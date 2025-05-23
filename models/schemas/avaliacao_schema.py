from pydantic import BaseModel

class Avaliacao_Schema(BaseModel):
    nota: int 
    aluno: int 
    livro: int
    reserva: int 