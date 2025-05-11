from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from ..controller_base import Controller_base

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
        @self.router_livro.get("/", status_code=200)
        def listar_alunos():
            pass