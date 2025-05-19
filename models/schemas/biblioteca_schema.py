from pydantic import BaseModel

class Biblioteca_schema(BaseModel):
    nota: int
    aluno_id: int