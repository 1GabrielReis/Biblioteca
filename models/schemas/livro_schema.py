from pydantic import BaseModel

class Livro_Schema(BaseModel):
    titulo: str
    autor: str
    editora: str