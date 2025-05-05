from fastapi import APIRouter
from ..controller.controller_entities.controller_aluno import Controller_aluno

router = APIRouter()

aluno_ctrl = Controller_aluno()
router.include_router(
    aluno_ctrl.router_aluno,
    prefix="/alunos",
    tags=["Alunos"]
)