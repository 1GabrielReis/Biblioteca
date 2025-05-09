from pydantic import BaseModel
from typing import Optional

class Aluno_Schema(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
        