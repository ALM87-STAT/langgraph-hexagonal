from fastapi import APIRouter
from starlette.responses import JSONResponse

from application.dto.plan_excecute_dto import PlanExcecuteDto
from application.use_cases.plan_execute_use_case import PlanExecuteUseCase
from application.use_cases.llm_reflection_use_case import LLMReflectionUseCase
from infrastructure.controllers.plan_execute_controller import PlanExecuteController
from infrastructure.controllers.llm_reflection_controller import LLMReflectionController
from langchain import LLMChain

plan_execute_router = APIRouter()

health_use_case = PlanExecuteUseCase()
controller = PlanExecuteController(health_use_case)

# Initialize LLMChain (this should be configured properly)
llm_chain = LLMChain()  # Placeholder for actual LLMChain initialization
reflection_controller = LLMReflectionController(llm_chain)
reflection_use_case = LLMReflectionUseCase(reflection_controller)

@plan_execute_router.post("/plan-execute")
async def plan_execute(data: PlanExcecuteDto) -> JSONResponse:
    """
    Endpoint to execute the Plan and Execute workflow.

    Args:
        data (GraphDto): Input data for the workflow.

    Returns:
        JSONResponse: Response containing the result of the workflow.
    """
    # Use reflection use case to process the user input
    user_input = data.input  # Assuming PlanExcecuteDto has an 'input' attribute
    response = reflection_use_case.execute(user_input)
    return JSONResponse(content={'response': response})
