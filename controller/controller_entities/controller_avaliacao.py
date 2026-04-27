from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response

from models.service.avaliacaoService import AvaliacaoService
from models.schemas.avaliacao_schema import Avaliacao_Schema

from view.view_entities.response_avaliacao import Response_avaliacao

from ..controller_base import Controller_base
from .controllerException import ControllerException

class Controller_avaliacao(Controller_base):
    def __init__(self):
        self.router_avaliacao= APIRouter()
        super().__init__()
        self.service= AvaliacaoService()
        self.response= Response_avaliacao()
        self.register_routes()

    def register_routes(self):

        @self.router_avaliacao.post("/", status_code=status.HTTP_201_CREATED,summary='Criar avaliação')
        def insert(avaliacao: Avaliacao_Schema):
            try:
                avaliacao_now=  self.service.instance_avaliacao(avaliacao=avaliacao)
                self.service.insert(avaliacao_now)
                return self.response.format(avaliacao_now)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao avaliar livro: {str(e)}")

        @self.router_avaliacao.put("/{id}", status_code=status.HTTP_200_OK, summary='Alterar avaliação')
        def update(id: int, avaliacao: Avaliacao_Schema):
            try:
                avaliacao_obj = self.service.instance_avaliacao(avaliacao=avaliacao, id=id)
                self.service.update(avaliacao_obj)
                return self.response.format(avaliacao_obj)
            except ValueError as e:
                raise HTTPException(status_code=422, detail=str(e))
            except Exception as e:
                raise ControllerException(message=f"Erro ao atualizar avaliação do livro: {str(e)}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


        @self.router_avaliacao.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,summary='Deletar Avaliação' )
        def deleteById(id: int):
            try:
                self.service.deleteById(id=id)
                return Response(status_code=204)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao deletar avaliação do livro: {str(e)}")

        @self.router_avaliacao.get("/{id}", status_code=status.HTTP_200_OK, summary='Encontra avaliação por ID')
        def findById(id: int):
            try:
                avaliacao= self.service.findById(id=id)
                return self.response.format(avaliacao)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar avaliação do livro: {str(e)}")

        @self.router_avaliacao.get("/", status_code=status.HTTP_200_OK,summary='Lista avaliaçoes')
        def findAll():
            try:
                avaliacoes= self.service.findAll()
                return self.response.format_list(avaliacoes)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao listar avaliações de livros: {str(e)}")
            
        @self.router_avaliacao.get("/aluno/{id}", status_code=status.HTTP_200_OK, summary='Encontra avaliação por id de aluno')
        def findByAluno(id: int):
            try:
                avaliacoes= self.service.findByAluno(id=id)
                return self.response.format_list_by_Aluno(avaliacoes)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar avaliações do livros: {str(e)}")

        @self.router_avaliacao.get("/livro/{id}", status_code=status.HTTP_200_OK, summary='Encontra avaliação por id de livro')
        def findByLivro(id: int):
            try:
                avaliacoes = self.service.findByLivro(id= id)
                return self.response.format_list_by_livro(avaliacoes= avaliacoes)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar avaliações de livros do aluno: {str(e)}")

        @self.router_avaliacao.get("/reserva/{id}", status_code=status.HTTP_200_OK, summary='Encontra avaliação por id de Reserva')
        def findByReserva(id: int):
            try:
                avaliacao= self.service.findByReserva(id= id)
                return self.response.format_list_by_Reserva(avaliacoes= avaliacao)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar avaliações de livros reservado: {str(e)}")