from datetime import datetime

from ..response_base import Response_base

class Resonse_reserva(Response_base):

    def _formatDate(self, data: datetime):
        if data is not None:
            return data.date().isoformat()
        return None

    def format(self, reserva):
        return {
            "status": "sucesso",
            "dados": {
                "id": reserva.id,
                "data_inicio": self._formatDate(reserva.data_inicio),
                "data_final": self._formatDate(reserva.data_final),
                "data_entregue": self._formatDate(reserva.data_entregue),
                "livro": {
                    "id":reserva.livro.id,
                    "titulo":reserva.livro.titutlo,
                    "autor": reserva.livro.autor,
                    "editora": reserva.livro.editora
                },
                "aluno": {
                    "id":reserva.aluno.id,
                    "nome":reserva.aluno.nome,
                    "sobrenome": reserva.aluno.sobrenome
                }
            }
        }
        

    def format_list(self, reservas):
        return {
            "status": "sucesso",
            "quantidade": len(reservas),
            "dados": [self.format(reserva)["dados"] for reserva in reservas] if reservas else []
        }
    

    def format_list_by_livro(self, reservas):
        if not reservas:
            return {
                "status": "sucesso",
                "quantidade": 0,
                "livro": None,
                "dados": []
            }

        livro = reservas[0].livro  

        return {
            "status": "sucesso",
            "livro": {
                "id": livro.id,
                "titulo": livro.titutlo,
                "autor": livro.autor,
                "editora": livro.editora
            },
            "quantidade": len(reservas),
            "dados": [
                {
                    "id": reserva.id,
                    "data_inicio": self._formatDate(reserva.data_inicio),
                    "data_final": self._formatDate(reserva.data_final),
                    "data_entregue": self._formatDate(reserva.data_entregue),
                    "aluno": {
                        "id": reserva.aluno.id,
                        "nome": reserva.aluno.nome,
                        "sobrenome": reserva.aluno.sobrenome
                    }
                } for reserva in reservas
            ]
        }