from starlette.responses import JSONResponse

from app.application.dto.plan_excecute_dto import PlanExcecuteDto
from app.application.use_cases.plan_execute_use_case import PlanExecuteUseCase


class PlanExecuteController:
    __plan_execute_use_case: PlanExecuteUseCase

    def __init__(self, plan_execute_use_case: PlanExecuteUseCase):
        self.__plan_execute_use_case = plan_execute_use_case

    def plan_execute(self, data: PlanExcecuteDto):
        response = self.__plan_execute_use_case.invoke(data.input)
        return JSONResponse(response)
