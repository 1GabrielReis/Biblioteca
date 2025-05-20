from ..response_base import Response_base

class Resonse_reserva(Response_base):
    def format(self, reserva):
        return {
            "status": "sucesso",
            "dados": {
                "id": reserva.id,
                "data_inicio": reserva.data_inicio,
                "data_final": reserva.data_final,
                "data_entregue": reserva.data_entregue,
                "livro": {
                    "id":reserva.livro.id,
                    "titulo":reserva.livro.titulo,
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