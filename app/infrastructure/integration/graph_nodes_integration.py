from langgraph.graph import END

from app.domain.interface.graph_state_interface import PlanExecute
from app.domain.interface.planning_steps_interface import Response
from app.infrastructure.integration.agents_integration import AgentFactory


class GraphNodes(AgentFactory):
    """Graph Nodes for Plan and Execute."""

    def __init__(self):
        super().__init__()
        self.agent_planner = self.agent_planner()
        self.agent_executor = self.agent_executor()
        self.agent_replanner = self.agent_replanner()

    def plan_step_node(self, state: PlanExecute):
        """Create an initial plan based on the user input."""
        plan = self.agent_planner.invoke({"messages": [("user", state["input"])]})
        return {"plan": plan.steps}

    def execute_step_node(self, state: PlanExecute):
        """Execute the first step in the current plan."""
        plan = state["plan"]
        plan_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(plan))
        task = plan[0]
        task_formatted = f"""For the following plan:
        {plan_str}\n\nYou are tasked with executing step {1}, {task}."""
        agent_response = self.agent_executor.invoke(
            {"messages": [("user", task_formatted)]}
        )
        return {
            "past_steps": [(task, agent_response["messages"][-1].content)],
        }

    def replan_step_node(self, state: PlanExecute):
        """Update the plan or provide a final response."""
        output = self.agent_replanner.invoke(state)
        if isinstance(output.action, Response):
            return {"response": output.action.response}
        else:
            return {"plan": output.action.steps}

    def should_end_node(self, state: PlanExecute):
        """Determine if the workflow should end or continue."""
        if "response" in state and state["response"]:
            return END
        else:
            return "agent"
