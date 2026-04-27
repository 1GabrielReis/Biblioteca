from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response

from models.service.bibliotecaService import BibliotecaService
from models.schemas.biblioteca_schema import Biblioteca_schema

from view.view_entities.response_biblioteca import Response_biblioteca

from ..controller_base import Controller_base
from .controllerException import ControllerException

class Controller_biblioteca(Controller_base):
    def __init__(self):
        super().__init__()
        self.service= BibliotecaService()
        self.response= Response_biblioteca()
        self.router_biblioteca = APIRouter()
        self.register_routes()

    def register_routes(self):
        
        @self.router_biblioteca.post("/", status_code=status.HTTP_201_CREATED, summary='Criar Avaliação da biblioteca')
        def insert(biblioteca : Biblioteca_schema):
            try:
                nova_avaliacao= self.service.instance_biblioteca(biblioteca)
                self.service.insert(nova_avaliacao)
                return self.response.format(nova_avaliacao)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao avaliar a biblioteca: {str(e)}")

        @self.router_biblioteca.put("/{id}", status_code=status.HTTP_200_OK, summary='Alterar Avalição da biblioteca')
        def update(id: int, biblioteca : Biblioteca_schema):
            try:
                livro_update= self.service.instance_biblioteca(id=id,biblioteca= biblioteca)
                self.service.update(livro_update)
                return self.response.format(livro_update)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar avaliação da biblioteca: {str(e)}")

        @self.router_biblioteca.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary='Deletar avaliação')
        def deleteById(id: int):
            try:
                self.service.deleteById(id=id)
                return Response(status_code=204)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao deletar avaliação da biblioteca: {str(e)}")

        @self.router_biblioteca.get("/{id}", status_code=status.HTTP_200_OK, summary='Busca avaliação por Id')
        def findById(id: int):
            try:
                avaliacao_biblioteca= self.service.findById(id=id)
                return self.response.format(avaliacao_biblioteca)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar avaliação da biblioteca: {str(e)}")

        @self.router_biblioteca.get("/", status_code=status.HTTP_200_OK,  summary='Lista todas as avaliação')
        def findAll():
            try:
                avaliacoes_biblioteca= self.service.findAll()
                return self.response.format_list(avaliacoes_biblioteca)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao listar avaliações da biblioteca: {str(e)}")

        @self.router_biblioteca.get("/aluno/{id}", status_code=status.HTTP_200_OK, summary='Busca avaliação por id aluno')
        def findByAluno(id: int):
            try:
                avaliacoes_aluno= self.service.findByAluno(id=id)
                return self.response.format_by_aluno(avaliacoes_aluno)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar avaliações da biblioteca do aluno: {str(e)}")
           