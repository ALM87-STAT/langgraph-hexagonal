# Research agent and node
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.infrastructure.integration.agents_tools_integration import ToolManager
from app.config.configuration import ConfigLoader
from app.domain.interface.planning_steps_interface import Plan, Act
from assets.prompts import (
    AGENT_EXECUTOR_PROMPT,
    SYSTEM_PLANER_PROMPT,
    SYSTEM_REPLANER_PROMPT,
)


class AgentFactory(ToolManager):
    def __init__(self):
        super().__init__()
        self.config = ConfigLoader().get_config
        self.llm = init_chat_model(**self.config.models.application_2.parameters)
        self.TOOLS = self.get_tools

    def agent_planner(self):
        planner_prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PLANER_PROMPT),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        planner = planner_prompt_template | self.llm.with_structured_output(Plan)

        return planner

    def agent_executor(self):
        executor = create_react_agent(
            self.llm, self.TOOLS, messages_modifier=AGENT_EXECUTOR_PROMPT
        )

        return executor

    def agent_replanner(self):
        replanner_prompt_template = ChatPromptTemplate.from_template(
            SYSTEM_REPLANER_PROMPT
        )

        replanner = replanner_prompt_template | self.llm.with_structured_output(Act)

        return replanner
