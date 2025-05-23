from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from ...models.service.avaliacaoService import Avaliacao
from ...models.schemas.avaliacao_schema import Avaliacao_Schema

from ...view.view_entities.response_avaliacao import Response_avaliacao

from ..controller_base import Controller_base
from .controllerException import ControllerException

class Controller_avaliacao(Controller_base):
    def __init__(self):
        super().__init__()
        self.service= Avaliacao()
        self.response= Response_avaliacao()
        self.router_avaliacao= APIRouter()
        self.register_routes()

    def register_routes(self):

        @self.router_avaliacao.post("/", status_code=201)
        def insert(reserva: Avaliacao_Schema):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao avaliar livro: {str(e)}")

        @self.router_avaliacao.put("/", status_code=200)
        def update(reserva: Avaliacao_Schema):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao atualizar avaliação do livro: {str(e)}")

        @self.router_avaliacao.delete("/{id}", status_code=204)
        def deleteById(id: int):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao deletar avaliação do livro: {str(e)}")

        @self.router_avaliacao.get("/{id}", status_code=200)
        def findById(id: int):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao buscar avaliação do livro: {str(e)}")

        @self.router_avaliacao.get("/", status_code=200)
        def findAll():
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao listar avaliações de livros: {str(e)}")

        @self.router_avaliacao.get("/{id}", status_code=200)
        def findByLivro(id: int):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao buscar avaliações de livros do aluno: {str(e)}")

        @self.router_avaliacao.get("/{id}", status_code=200)
        def findByAluno(id: int):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao buscar avaliações do livros: {str(e)}")

        @self.router_avaliacao.get("/{id}", status_code=200)
        def findByReserva(id: int):
            try:
                pass
            except Exception as e:
                raise ControllerException(status_code=500, detail=f"Erro ao buscar avaliações de livros reservado: {str(e)}")