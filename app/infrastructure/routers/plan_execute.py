from fastapi import APIRouter
from starlette.responses import JSONResponse

from application.dto.plan_excecute_dto import PlanExcecuteDto
from application.use_cases.plan_execute_use_case import PlanExecuteUseCase
from infrastructure.controllers.plan_execute_controller import PlanExecuteController

plan_execute_router = APIRouter()

health_use_case = PlanExecuteUseCase()
controller = PlanExecuteController(health_use_case)


@plan_execute_router.post("/plan-execute")
async def plan_execute(data: PlanExcecuteDto) -> JSONResponse:
    """
    Endpoint to execute the Plan and Execute workflow.

    Args:
        data (GraphDto): Input data for the workflow.

    Returns:
        JSONResponse: Response containing the result of the workflow.
    """
    response = controller.plan_execute(data)
    return response
