from ..response_base import Response_base

class Response_livro(Response_base):

    def format(self,livro):
        return {
            "status": "sucesso",
            "dados": {
                "id": livro.id,
                "titulo": livro.titutlo,
                "autor": livro.autor,
                "editora": livro.editora
            }
        }

    def format_list(self,livros):
        return {
            "status": "sucesso",
            "quantidade": len(livros),
            "dados": [self.format(livro)["dados"] for livro in livros] if livros else []
        }