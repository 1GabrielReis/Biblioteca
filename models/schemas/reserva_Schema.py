from pydantic import BaseModel

class Reserva_Schema(BaseModel):
    livro: int
    aluno: int
    data_inicio: str
    data_final: str
    data_entregue: str