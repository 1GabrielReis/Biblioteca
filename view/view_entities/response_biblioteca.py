from ..response_base import Response_base
import json

class Response_biblioteca(Response_base):
    
    def format(self, biblioteca):
        return {
            "status": "sucesso",
            "dados": {
                "id": biblioteca.id,
                "nota": biblioteca.nota,
                "aluno": {
                    "id":biblioteca.aluno.id,
                    "nome":biblioteca.aluno.nome,
                    "sobrenome": biblioteca.aluno.sobrenome
                }
            }
        }
        

    
    def format_list(self, biblioteca_notas):
        return {
            "status": "sucesso",
            "quantidade": len(biblioteca_notas),
            "dados": [self.format(biblioteca)["dados"] for biblioteca in biblioteca_notas] if biblioteca_notas else []
        }
        