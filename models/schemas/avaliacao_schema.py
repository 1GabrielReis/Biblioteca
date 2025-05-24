from pydantic import BaseModel

class Avaliacao_Schema(BaseModel):
    nota: int 
    reserva: int 