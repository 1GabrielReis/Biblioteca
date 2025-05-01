from fastapi import APIRouter, HTTPException

from ..controller_base import Controller_base
from ...models.service.alunoService import AlunoService
from ...view.view_entities.response_aluno import Response_aluno

class Controller_aluno(Controller_base):
    def __init__(self):
        self.router_aluno = APIRouter()
        self.service = AlunoService()
        self.response = Response_aluno()
        self.register_routes()

    def register_routes(self):

        @self.router_aluno.get("/listar")
        def listar_alunos():
            try:
                alunos = self.service.findAll()
                return self.response.format_list(alunos)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao listar alunos: {str(e)}")

        @self.router_aluno.get("/{id}")
        def buscar_aluno(id: int):
            try:
                aluno = self.service.findById(id)
                if not aluno:
                    raise HTTPException(status_code=404, detail="Aluno não encontrado")
                return self.response.format(aluno)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao buscar aluno: {str(e)}")

        @self.router_aluno.post("/")
        def criar_aluno(data: dict):
            try:
                novo_aluno = self.service.insert(data)
                return self.response.format(novo_aluno)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao criar aluno: {str(e)}")

        @self.router_aluno.put("/")
        def atualizar_aluno(data: dict):
            try:
                aluno_atualizado = self.service.update(data)
                return self.response.format(aluno_atualizado)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao atualizar aluno: {str(e)}")

        @self.router_aluno.delete("/{id}")
        def deletar_aluno(id: int):
            try:
                self.service.deleteById(id)
                return {"mensagem": "Aluno deletado com sucesso"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao deletar aluno: {str(e)}")