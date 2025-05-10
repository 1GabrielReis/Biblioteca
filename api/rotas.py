from fastapi import APIRouter
from ..controller.controller_entities.controller_aluno import Controller_aluno
from ..controller.controller_entities.controller_livro import Controller_livro

router = APIRouter()

aluno_ctrl = Controller_aluno()
router.include_router(
    aluno_ctrl.router_aluno,
    prefix="/alunos",
    tags=["Alunos"]
)


livro_ctrl = Controller_livro()
router.include_router(
    livro_ctrl.router_livro,
    prefix="/livros",
    tags=["Livros"]
)