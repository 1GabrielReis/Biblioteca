from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from ..controller_base import Controller_base
from .controllerException import ControllerException

from ...view.view_entities.response_livro import Response_livro

from ...models.service.livroService import LivroService
from ...models.schemas.livro_schema import Livro_Schema



class Controller_livro(Controller_base):
    def __init__(self):
        self.service= LivroService()
        self.response= Response_livro()
        self.router_livro = APIRouter()
        self.register_routes()

    def register_routes(self):

        @self.router_livro.post("/", status_code=201)
        def insert(livro_schema: Livro_Schema):
            try:
                novo_livro= self.service.instanceObject(livro_schema)
                self.service.insert(novo_livro)
                return self.response.format(novo_livro)
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao criar aluno: {str(e)}")

        @self.router_livro.put("/{id}", status_code=200)
        def update(id: int, livro: Livro_Schema):
            pass

        @self.router_livro.delete("/{id}", status_code=204)
        def deleteById(id: int):
            pass

        @self.router_livro.get("/{id}", status_code=200)
        def findById(id: int):
            pass

        @self.router_livro.get("/", status_code=200)
        def findAll():
            pass