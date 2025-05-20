from fastapi import APIRouter
from ..controller.controller_entities.controller_aluno import Controller_aluno
from ..controller.controller_entities.controller_livro import Controller_livro
from ..controller.controller_entities.controller_biblioteca import Controller_biblioteca
from ..controller.controller_entities.controller_reserva import Controller_reserva

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

reserva_ctrl = Controller_reserva()
router.include_router(
    reserva_ctrl.router_reserva,
    prefix="/reserva",
    tags=["Reserva"]
)