from fastapi import APIRouter , status
from fastapi.responses import Response

from ..controller_base import Controller_base
from .controllerException import ControllerException
from view.view_entities.response_aluno import Response_aluno
from models.service.alunoService import AlunoService
from models.schemas.aluno_schema import Aluno_Schema

class Controller_aluno(Controller_base):
    def __init__(self):
        self.router_aluno = APIRouter()
        super().__init__()
        self.service = AlunoService()
        self.response = Response_aluno()
        self.register_routes()

    def register_routes(self):

        @self.router_aluno.get("/", status_code= status.HTTP_200_OK , summary= "Lista todos os aluno")
        def findAll():
            try:
                alunos = self.service.findAll()
                if not alunos:
                    return {"mensagem": "Nenhum aluno encontrado"}
                return self.response.format_list(alunos)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao listar alunos: {str(e)}")

        @self.router_aluno.get("/{id}", status_code=status.HTTP_200_OK, summary= "Encontra aluno por ID")
        def findById(id: int):
            try:
                aluno = self.service.findById(id)
                if not aluno:
                    raise ControllerException(status_code=404, detail="Aluno não encontrado")
                return self.response.format(aluno)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar aluno: {str(e)}")

        @self.router_aluno.post("/", status_code=status.HTTP_201_CREATED, summary= "Criar aluno")
        def insert(aluno: Aluno_Schema):
            try:
                novo_aluno= self.service.instanceObject(aluno)
                self.service.insert(novo_aluno)
                return self.response.format(novo_aluno)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao criar aluno: {str(e)}")

        @self.router_aluno.put("/{id}", status_code=status.HTTP_200_OK, summary= 'Alterar Aluno')
        def update(id: int, aluno: Aluno_Schema):
            try:
                aluno_obj= self.service.instanceObject(id=id, aluno=aluno)
                aluno_atualizado = self.service.update(aluno_obj)
                return self.response.format(aluno_atualizado)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar aluno: {str(e)}")

        @self.router_aluno.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary= 'Deletar Aluno')
        def deleteById(id: int):
            try:
                self.service.deleteById(id)
                return Response(status_code=204)
            except Exception as e:
                raise ControllerException(status_code=status.http_500, detail=f"Erro ao deletar aluno: {str(e)}")