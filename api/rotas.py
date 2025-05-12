from fastapi import APIRouter
from ..controller.controller_entities.controller_aluno import Controller_aluno
from ..controller.controller_entities.controller_livro import Controller_livro
from ..controller.controller_entities.controller_biblioteca import Controller_biblioteca

router = APIRouter()

aluno_ctrl = Controller_aluno()
router.include_router(
    aluno_ctrl.router_aluno,
    prefix="/aluno",
    tags=["Aluno"]
)


livro_ctrl = Controller_livro()
router.include_router(
    livro_ctrl.router_livro,
    prefix="/livro",
    tags=["Livro"]
)

biblioteca_ctrl = Controller_biblioteca()
router.include_router(
    biblioteca_ctrl.router_biblioteca,
    prefix="/biblioteca",
    tags=["Biblioteca"]
)