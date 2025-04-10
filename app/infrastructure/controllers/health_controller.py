from application.use_cases.health_use_case import HealthUseCase


class HealthController:
    """Controller for health check."""

    def __init__(self, health_use_case: HealthUseCase):
        self.__health_use_case = health_use_case

    def health_check(self) -> dict:
        """Perform a health check."""
        return self.__health_use_case.invoke()
