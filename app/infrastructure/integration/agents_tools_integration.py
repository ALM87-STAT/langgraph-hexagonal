from typing import Any, Callable, List, Optional

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

from app.config.configuration import ConfigLoader


class ToolManager:
    """A class to manage and provide access to various tools."""

    def __init__(self):
        """Initialize the ToolManager with configuration."""
        self.config = ConfigLoader().get_config

    @staticmethod
    @tool
    def tavily_tool(query: str) -> Optional[list[dict[str, Any]]]:
        """Search for general web results.

        This function performs a search using the Tavily search engine, which is designed
        to provide comprehensive, accurate, and trusted results. It's particularly useful
        for answering questions about current events.

        Args:
            query: The search query to perform.

        Returns:
            Optional[list[dict[str, Any]]]: The search results.
        """
        wrapped = TavilySearchResults(max_results=3)
        result = wrapped.invoke({"query": query})
        return result

    @property
    def get_tools(self) -> List[Callable[..., Any]]:
        """Get all available tools.

        Returns:
            List[Callable[..., Any]]: List of available tool functions
        """
        return [self.tavily_tool]
