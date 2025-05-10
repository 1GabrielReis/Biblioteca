from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from ..controller_base import Controller_base
from ...view.view_entities.response_aluno import Response_aluno
from ...models.service.alunoService import AlunoService
from ...models.schemas.aluno_schema import Aluno_Schema

class Controller_aluno(Controller_base):
    def __init__(self):
        self.router_aluno = APIRouter()
        self.service = AlunoService()
        self.response = Response_aluno()
        self.register_routes()

    def register_routes(self):

        @self.router_aluno.get("/", status_code=200)
        def listar_alunos():
            try:
                alunos = self.service.findAll()
                if not alunos:
                    return {"mensagem": "Nenhum aluno encontrado"}
                return self.response.format_list(alunos)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao listar alunos: {str(e)}")

        @self.router_aluno.get("/{id}", status_code=200)
        def buscar_aluno(id: int):
            try:
                aluno = self.service.findById(id)
                if not aluno:
                    raise HTTPException(status_code=404, detail="Aluno não encontrado")
                return self.response.format(aluno)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao buscar aluno: {str(e)}")

        @self.router_aluno.post("/", status_code=201)
        def criar_aluno(aluno: Aluno_Schema):
            if aluno.id is not None:
                    raise HTTPException(status_code=400,detail=f"ID não deve ser enviado ao criar aluno.")
            try:
                novo_aluno= self.service.instanceObject(aluno)
                self.service.insert(novo_aluno)
                return self.response.format(novo_aluno)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao criar aluno: {str(e)}")

        @self.router_aluno.put("/{id}", status_code=200)
        def atualizar_aluno(id: int, aluno: Aluno_Schema):
            try:
                aluno_obj= self.service.instanceObject(id=id, aluno=aluno)
                aluno_atualizado = self.service.update(aluno_obj)
                return self.response.format(aluno_atualizado)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao atualizar aluno: {str(e)}")

        @self.router_aluno.delete("/{id}", status_code=204)
        def deletar_aluno(id: int):
            try:
                self.service.deleteById(id)
                return Response(status_code=204)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao deletar aluno: {str(e)}")