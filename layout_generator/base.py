import logging
from abc import ABC, abstractmethod
from typing import Dict, List

from layout_generator.constants.schemas import Edges, Nodes, OutputFormat


class BaseLayout(ABC):
    """
    Abstract base class for the layout algorithms.
    """

    def __init__(self):
        self.log = logging.getLogger()
        logging.basicConfig(level=logging.INFO)

    @abstractmethod
    def get_layout(self, nodes: List[Nodes], edges: List[Edges]) -> OutputFormat:
        """
        Calculate the layout positions for the nodes based on the algorithm.

        Args:
            nodes (List[Nodes]): A list of nodes in the graph.
            edges (List[Edges]): A list of edges defining relationships between nodes.

        Returns:
            OutputFormat: The formatted output with node positions.
        """
        pass

    @abstractmethod
    def get_positions(
        self,
        nodes: List[Nodes],
        edges: List[Edges],
        *args,
    ) -> List[Dict]:
        """
        Obtain the positions for nodes in the layout.

        Args:
            nodes (List[Nodes]): A list of nodes in the graph.
            edges (List[Edges]): A list of edges defining relationships between nodes.
            *args: Additional arguments for layout customization.

        Returns:
            List[Dict]: A list of dictionaries containing node positions.
        """
        pass
