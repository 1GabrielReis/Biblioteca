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
        def insert(livro: Livro_Schema):
            try:
                novo_livro= self.service.instanceObject(livro)
                self.service.insert(novo_livro)
                return self.response.format(novo_livro)
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao criar livro: {str(e)}")

        @self.router_livro.put("/{id}", status_code=200)
        def update(id: int, livro: Livro_Schema):
            try:
                novo_livro= self.service.instanceObject(id= id, livro= livro)
                self.service.update(novo_livro)
                return self.response.format(novo_livro)
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao atualizar livro: {str(e)}")

        @self.router_livro.delete("/{id}", status_code=204)
        def deleteById(id: int):
            try:
                self.service.deleteById(id)
                return Response(status_code=204)
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao deletar livro: {str(e)}")

        @self.router_livro.get("/{id}", status_code=200)
        def findById(id: int):
            try:
                livro= self.service.findById(id)
                return self.response.format(livro)
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao buscar livro: {str(e)}")

        @self.router_livro.get("/", status_code=200)
        def findAll():
            try:
                livros= self.service.findAll()
                return self.response.format_list(livros)
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao listar livros: {str(e)}")