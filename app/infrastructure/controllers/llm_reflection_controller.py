from langchain import LLMChain
from langchain.prompts import PromptTemplate

class LLMReflectionController:
    def __init__(self, llm_chain: LLMChain):
        self.llm_chain = llm_chain

    def reflect_and_correct(self, user_input: str) -> str:
        # Step 1: Generate initial response
        initial_response = self.llm_chain.run(user_input)

        # Step 2: Reflection logic
        reflection_prompt = PromptTemplate(
            input_variables=["initial_response"],
            template="Reflect on the following response: {initial_response}"
        )
        reflection = self.llm_chain.run(reflection_prompt.format(initial_response=initial_response))

        # Step 3: Check for contradictions or errors
        if "error" in reflection.lower():
            # Step 4: Generate corrected response
            correction_prompt = PromptTemplate(
                input_variables=["initial_response", "reflection"],
                template="Given the initial response: {initial_response}, and the reflection: {reflection}, provide a corrected response."
            )
            corrected_response = self.llm_chain.run(correction_prompt.format(initial_response=initial_response, reflection=reflection))
            return corrected_response

        return initial_response
