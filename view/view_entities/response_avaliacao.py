from datetime import datetime

from ..response_base import Response_base
from .response_aluno import Response_aluno
from .response_livro import Response_livro
from .response_reserva import Response_reserva

class Response_avaliacao(Response_base):
    def __init__(self):
        super().__init__()
        self.response_aluno= Response_aluno()
        self.response_livro= Response_livro()
        self.response_reserva= Response_reserva()
        
    def _format_reserva(self, reserva):
        reserva = reserva.copy()
        reserva['aluno']= reserva['aluno']['id']
        reserva['livro']= reserva['livro']['id']
        return reserva

    def _formatDate(self, data: datetime):
        if data is not None:
            return data.date().isoformat()
        return None

    def format(self, avaliacao):
        if not avaliacao:
            return {
                "status": "sucesso",
                "quantidade": 0,
                "livro": None,
                "dados": []
            }
        return {
            "status": "sucesso",
            "dados":{
                "id":avaliacao.id,
                "nota":avaliacao.nota,
                "aluno": self.response_aluno.format(avaliacao.aluno)['dados'],
                "livro":self.response_livro.format(avaliacao.livro)['dados'],
                "reserva": self._format_reserva(self.response_reserva.format(avaliacao.reserva)['dados'])
                
            }
        }

    def format_list(self, avaliacoes):
        return {
            "status": "sucesso",
            "quantidade": len(avaliacoes),
            "dados": [self.format(avaliacao)["dados"] for avaliacao in avaliacoes] if avaliacoes else []
        }

    def format_list_by_Aluno(self, avaliacoes):
        if not avaliacoes:
            return {
                "status": "sucesso",
                "quantidade": 0,
                "aluno": None,
                "dados": []
            }
        
        aluno = avaliacoes[0].aluno

        return{
            "status": "sucesso",
            "aluno": {

                "id": aluno.id,
                "nome": aluno.nome,
                "sobrenome": aluno.sobrenome
            },
            "quantidade": len(avaliacoes),
            "dados": [
                {
                    "id": avaliacao.id,
                    "nota": avaliacao.nota,
                    "livro":self.response_livro.format(avaliacao.livro)['dados'],
                    "reserva": self._format_reserva(self.response_reserva.format(avaliacao.reserva)['dados'])
                } for avaliacao in avaliacoes
            ]

        }

    def format_list_by_livro(self, avaliacoes):
        pass


    def format_list_by_Reserva(self, avaliacoes):
        pass