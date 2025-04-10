from fastapi import APIRouter

from infrastructure.routers.plan_execute import plan_execute_router
from infrastructure.routers.llm_reflection import llm_reflection_router


class Router:
    """Router for the application."""

    __router: APIRouter

    def __init__(self):
        self.__router = APIRouter()
        self.__router.include_router(plan_execute_router)
        self.__router.include_router(llm_reflection_router)

    def get_router(self) -> APIRouter:
        """Initialize the routes for the application."""
        return self.__router
