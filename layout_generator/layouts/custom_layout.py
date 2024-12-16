from typing import Dict, List

from layout_generator.base import BaseLayout
from layout_generator.constants import LayoutConstants
from layout_generator.constants.schemas import Edges, Nodes, OutputFormat
from layout_generator.errors import DataFetchError
from layout_generator.utils import LayoutUtils


class CustomLayout(BaseLayout):
    """
    This class is a custom layout class for a different layout style.
    """

    def __init__(self):
        super().__init__()
        self.log.info("Initializing Custom Layout")
        self.constants = LayoutConstants()
        self.utils = LayoutUtils()

    def get_layout(self, nodes: List[Nodes], edges: List[Edges]) -> OutputFormat:
        """
        Generates the layout by positioning nodes and formatting the output.
        :param nodes: A list of Nodes objects
        :param edges: A list of Edges objects
        :return: A dictionary of nodes and edges with updated positions in nodes.
        """
        try:
            if not nodes:
                raise DataFetchError("Unable to get the nodes.")
            nodes_list = self.get_positions(nodes, edges)
            if not nodes_list:
                raise DataFetchError("Unable to get the nodes list.")
            nodes = self.utils.output_nodes_formatting(nodes, nodes_list)
            return OutputFormat(nodes=nodes, edges=edges)
        except Exception as e:
            self.log.error(e.args)
            raise e

    def get_positions(
        self, nodes: List[Nodes], edges: List[Edges], *args
    ) -> List[Dict]:
        """
        Calculates positions for nodes based on predefined rules.

            :param nodes: A list of `Nodes` objects.
            :param edges: A list of `Edges` objects.
            :param args: Additional arguments for customization (unused).
            :return: A generator yielding dictionaries containing node IDs and their x, y positions.
        """
        try:
            node_types = self.constants.rca_node_types
            self.log.info(f"Edges: {edges}")
            node_positions = self.constants.rca_node_positions
            mid_point = node_positions.get("midpoint")
            left_positioned_nodes = node_types.get("left_positioned_nodes")
            right_positioned_nodes = node_types.get("right_positioned_nodes")

            left_to_top_map = {0: 1}
            left_distance = node_positions.get("node_spacing")[0]
            top_distance = node_positions.get("node_spacing")[1]
            for node in nodes:
                if node.topText == node_types.get("currently_selected_node")[0]:
                    top = mid_point[0]
                    left = mid_point[1]
                elif node.topText in left_positioned_nodes:
                    index_ = left_positioned_nodes.index(node.topText) - 1
                    count_ = left_to_top_map.get(index_, 0)
                    left = mid_point[1] + (index_ * left_distance)
                    top = mid_point[0] + (count_ * top_distance)
                    left_to_top_map[index_] = count_ + 1

                elif node.topText in right_positioned_nodes:
                    index_ = right_positioned_nodes.index(node.topText) + 1
                    count_ = left_to_top_map.get(index_, 0)
                    left = mid_point[1] + (index_ * left_distance)
                    top = mid_point[0] + (count_ * top_distance)
                    left_to_top_map[index_] = count_ + 1
                else:
                    continue
                yield {"id": node.id, "x": left, "y": top}

        except Exception as e:
            self.log.error(e.args)
            raise
