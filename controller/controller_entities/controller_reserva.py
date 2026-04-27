from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response

from ..controller_base import Controller_base
from .controllerException import ControllerException

from models.service.reservaService import ReservaService
from models.schemas.reserva_Schema import Reserva_Schema

from view.view_entities.response_reserva import Response_reserva

class Controller_reserva(Controller_base):
    def __init__(self):
        super().__init__()
        self.service= ReservaService()
        self.response = Response_reserva()
        self.router_reserva = APIRouter()
        self.register_routes()

    def register_routes(self):
        
        @self.router_reserva.post("/", status_code=status.HTTP_200_OK, summary='Criar reserva')
        def insert(reserva: Reserva_Schema):
            try:
                nova_reserva= self.service.instance_reserva(reserva)
                self.service.insert(nova_reserva)
                return self.response.format(nova_reserva)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao adicionar Reserva: {str(e)}")

        @self.router_reserva.put("/{id}", status_code=status.HTTP_200_OK, summary='Alterar reserva')
        def update(reserva: Reserva_Schema, id):
            try:
                update_reserva= self.service.instance_reserva(id=id, reserva=reserva)
                self.service.update(update_reserva)
                return self.response.format(update_reserva)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar reserva: {str(e)}")

        @self.router_reserva.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary='Deletar reserva')
        def deleteById(id: int):
            try:
                self.service.deleteById(id=id)
                return Response(status_code=204)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao deletar reserva: {str(e)}")

        @self.router_reserva.get("/{id}", status_code=status.HTTP_200_OK, summary='Busca reserva por ID')
        def findById(id: int):
            try:
                reserva= self.service.findById(id=id)
                return self.response.format(reserva)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar reserva: {str(e)}")

        @self.router_reserva.get("/", status_code=status.HTTP_200_OK, summary='Lista reserva')
        def findAll():
            try:
                reservas= self.service.findAll()
                return self.response.format_list(reservas)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao listar reserva: {str(e)}")

        @self.router_reserva.get("/livro/{id}", status_code=status.HTTP_200_OK, summary='Busca reserva por id livro')
        def findByLivro(id: int):
            try:
                livros= self.service.findByLivro(id=id)
                return self.response.format_list_by_livro(livros)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar reserva do aluno: {str(e)}")

        @self.router_reserva.get("/aluno/{id}", status_code=status.HTTP_200_OK, summary='Busca reserva por id aluno')
        def findByAluno(id: int):
            try:
                alunos= self.service.findByAluno(id=id)
                return self.response.format_list_by_Aluno(alunos)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar reserva do livro: {str(e)}")

        @self.router_reserva.put("/{id}/devolver", status_code=status.HTTP_200_OK)
        def returnBook(id: int):
            print(">>> CHAMOU A ROTA")
            try:
                reserva= self.service.findById(id=id)
                self.service.returnBook(reserva=reserva)
                return self.response.format(reserva)
            except Exception as e:
                raise ControllerException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao devolver livro: {str(e)}")
