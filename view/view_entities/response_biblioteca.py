from ..response_base import Response_base

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
    
    
    def format_by_aluno(self, avalicoes_biblioteca):
        if not avalicoes_biblioteca:
            return {
                "status": "sucesso",
                "quantidade": 0,
                "aluno": None,
                "avaliacoes": []
            }

        aluno = avalicoes_biblioteca[0].aluno

        return {
            "status": "sucesso",
            "quantidade": len(avalicoes_biblioteca),
            "aluno": {
                "id": aluno.id,
                "nome": aluno.nome,
                "sobrenome": aluno.sobrenome
            },
            "avaliacoes": [
                {
                    "id": biblioteca.id,
                    "nota": biblioteca.nota
                } for biblioteca in avalicoes_biblioteca
            ]
        }

        