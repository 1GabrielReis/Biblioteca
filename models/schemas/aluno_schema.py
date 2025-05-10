from pydantic import BaseModel

class Aluno_Schema(BaseModel):
    nome: str
    sobrenome: str
        