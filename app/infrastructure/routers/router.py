from fastapi import APIRouter

from infrastructure.routers.plan_execute import plan_execute_router


class Router:
    """Router for the application."""

    __router: APIRouter

    def __init__(self):
        self.__router = APIRouter()
        self.__router.include_router(plan_execute_router)

    def get_router(self) -> APIRouter:
        """Initialize the routes for the application."""
        return self.__router
