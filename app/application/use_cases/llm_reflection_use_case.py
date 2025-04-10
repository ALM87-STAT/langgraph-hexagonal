from infrastructure.controllers.llm_reflection_controller import LLMReflectionController

class LLMReflectionUseCase:
    def __init__(self, reflection_controller: LLMReflectionController):
        self.reflection_controller = reflection_controller

    def execute(self, user_input: str) -> str:
        return self.reflection_controller.reflect_and_correct(user_input)
