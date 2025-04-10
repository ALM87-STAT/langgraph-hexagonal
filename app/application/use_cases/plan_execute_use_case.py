from langgraph.graph import StateGraph, START, END
from opik.integrations.langchain import OpikTracer
import opik

from app.domain.interface.graph_state_interface import PlanExecute
from app.infrastructure.integration.graph_nodes_integration import GraphNodes


class PlanExecuteUseCase(GraphNodes):
    """Graph Workflow for Plan and Execute."""

    def __init__(self):
        super().__init__()
        self.__initialize_opik_tracer()

    def invoke(self, text_input: str) -> dict:
        """Invoke the graph with inputs and configuration."""
        graph, opik_tracer = self.__build_graph()
        config = {"recursion_limit": 50, "callbacks": [opik_tracer]}
        inputs = {
            "input": text_input,
        }
        response = graph.invoke(inputs, config=config)

        return response

    def __build_graph(self):
        """Construct and return the Plan and Execute graph."""
        builder = StateGraph(PlanExecute)

        # Add nodes
        builder.add_node("planner", self.plan_step_node)
        builder.add_node("agent", self.execute_step_node)
        builder.add_node("replan", self.replan_step_node)

        # Add edges
        builder.add_edge(START, "planner")
        builder.add_edge("planner", "agent")
        builder.add_edge("agent", "replan")
        builder.add_conditional_edges(
            "replan",
            self.should_end_node,
            ["agent", END],
        )

        # Compile graph
        graph = builder.compile()
        graph.name = "Plan and Execute"
        opik_tracer = OpikTracer(graph=graph.get_graph(xray=True))
        return graph, opik_tracer

    def __initialize_opik_tracer(self):
        """Initialize the Opik tracer."""
        try:
            opik.configure(use_local=True, url="http://localhost:5173/api")
        except Exception as e:
            print(f"Error initializing Opik tracer: {e}")


# ------------------------------------------------------------------------------


# import asyncio
# import nest_asyncio

# grapg_workflow = PlanExecuteUseCase()
# graph, opik_tracer = grapg_workflow.build_graph()

# config = {"recursion_limit": 50, "callbacks": [opik_tracer]}
# inputs = {
#     "input": """Quién ganó el mundial de fútbol masculino en el año 2002?""",
# }


# async def run_workflow():
#     async for event in graph.astream(inputs, config=config):
#         for k, v in event.items():
#             if k != "__end__":
#                 print(v)


# async def run_workflow():
#     result = await graph.ainvoke(inputs, config=config)
#     print(result)


# def run_workflow():
#     result = graph.invoke(inputs, config=config)
#     print(result["response"])


# run_workflow()

# nest_asyncio.apply()
# asyncio.run(run_workflow())
