import importlib
import logging
from typing import List

from layout_generator.base import BaseLayout
from layout_generator.constants import LayoutConstants
from layout_generator.constants.schemas import Edges, Nodes, OutputFormat


class GraphLayouts:
    """
    This class of the Layouts SDK is used to call the function fetch_layouts() which dynamically imports the
    specific layout mentioned and gives the positions of nodes and edges based on various parameters.
    """

    def __init__(self):
        self.log = logging.getLogger("Initializing Graph Layouts")

    def fetch_layout(
        self,
        layout_name: str = None,
        nodes: List[Nodes] = None,
        edges: List[Edges] = None,
    ) -> OutputFormat:
        """
        This function is the main function which the user calls to fetch a certain layout.
        :param layout_name: A string denoting the name of the layout algorithm.
        :param nodes: A list of dictionaries which has nodes.
        :param edges: A list of dictionaries which has edges.
        :return: Dictionary which gives output format of nodes and edges with their respective positions.
        """
        pass
