from ..response_base import Response_base

class Response_aluno(Response_base):

    def format(self,aluno):
        return {
            "status": "sucesso",
            "dados": {
                "id": aluno.id,
                "nome": aluno.nome,
                "email": aluno.email,
                "ativo": aluno.ativo
            }
        }

    def format_list(self,alunos):
        return {
            "status": "sucesso",
            "quantidade": len(alunos),
            "dados": [self.format(aluno)["dados"] for aluno in alunos]
        }
