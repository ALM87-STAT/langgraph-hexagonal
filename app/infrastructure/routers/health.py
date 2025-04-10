from fastapi import APIRouter
from application.use_cases.health_use_case import HealthUseCase
from infrastructure.controllers.health_controller import HealthController

health_router = APIRouter()
health_use_case = HealthUseCase()
controller = HealthController(health_use_case)


@health_router.get("/health")
def health():
    return controller.health_check()
