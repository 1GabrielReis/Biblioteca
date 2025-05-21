from pydantic import BaseModel
from typing import Optional

class Reserva_Schema(BaseModel):
    livro: int
    aluno: int
    data_inicio: str
    data_final: str
    data_entregue: Optional[str] = None