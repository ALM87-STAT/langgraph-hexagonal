from fastapi import APIRouter
from starlette.responses import JSONResponse
from application.dto.agents_dto import AgentsDto
from application.use_cases.llm_reflection_use_case import LLMReflectionUseCase

llm_reflection_router = APIRouter()

reflection_use_case = LLMReflectionUseCase()

@llm_reflection_router.post("/llm-reflect")
async def llm_reflect(data: AgentsDto) -> JSONResponse:
    """
    Endpoint to reflect on the agent's response.

    Args:
        data (AgentsDto): Input data for the agent.

    Returns:
        JSONResponse: Response containing the result of the reflection.
    """
    response = await reflection_use_case.reflect_and_correct(data)
    return JSONResponse(content=response)
