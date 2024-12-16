from typing import Dict, List

import networkx as nx

from layout_generator.base import BaseLayout
from layout_generator.constants.schemas import Edges, Nodes, OutputFormat
from layout_generator.errors import DataFetchError
from layout_generator.utils import LayoutUtils


class KamadaKawaiLayout(BaseLayout):
    """
    Implementation of the kamada-kawai force-directed layout algorithm.
    """

    def __init__(self):
        super().__init__()
        self.log.info("Initializing Kamada Kawai Layout")
        self.utils = LayoutUtils()

    def get_layout(self, nodes: List[Nodes], edges: List[Edges]) -> OutputFormat:
        """
        This function gets the list of nodes with positional arguments according to the kamada-kawai layout
        :param nodes: List of node dictionaries
        :param edges: List of edge dictionaries
        :return: List of dictionaries containing nodes and edges with updated positions
        """
        try:

            nodes_list = self.get_positions(nodes, edges)
            if not nodes_list:
                raise DataFetchError("Unable to get the nodes.")
            nodes = self.utils.output_nodes_formatting(nodes, nodes_list)
            return OutputFormat(nodes=nodes, edges=edges)
        except Exception as e:
            self.log.error(e.args)
            raise

    def get_positions(
        self,
        nodes: List[Nodes],
        edges: List[Edges],
        *args,
    ) -> List[Dict]:
        """

        :param nodes: List of node dictionaries
        :param edges:List of edge dictionaries
        :return: A generator that yields dictionaries, containing the node ID and its x, y coordinates based on the
        Kamada-Kawai layout.
        :rtype: generator[dict[str, float]]
        """
        try:
            g = self.utils.create_graph(nodes, edges)
            positions = nx.kamada_kawai_layout(g)
            if not positions:
                raise DataFetchError(DataFetchError.message)
            for each_id, coord in positions.items():
                yield {"id": each_id, "x": coord[0], "y": coord[1]}
        except Exception as e:
            self.log.error(e.args)
            raise
