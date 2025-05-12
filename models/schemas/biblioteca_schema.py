from pydantic import BaseModel

class Biblioteca_schema(BaseModel):
    nota: str
    aluno: str