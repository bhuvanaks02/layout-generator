from typing import Dict, List, Tuple

import networkx as nx

from layout_generator.constants.schemas import Edges, Nodes, Position


class LayoutUtils:
    """
    This class has utilities for layouts.
    """

    @staticmethod
    def snakecase_to_camelcase(layout_name: str) -> str:
        """
        A function which converts snake case words to camel case words.
        :param layout_name: Name of the type of layout being implemented in snake case.
        :return: Name of the layout in camel case.
        :rtype: str
        """
        return "".join(layout_name.title().split("_"))

    @staticmethod
    def fetch_node_format(nodes: List[Nodes]) -> List:
        """
        This function takes nodes in a certain format and extracts node id's into another list.
        :param nodes: A list of dictionaries of nodes.
        :return: Returns a list of node_ids
        :rtype: A List
        """
        nodes_list = []
        for node in nodes:
            nodes_list.append(node.id)
        return nodes_list

    @staticmethod
    def fetch_edge_format(edges: List[Edges]) -> List[Tuple]:
        """
        This function takes the edges and extracts from and to into a list of tuples.
        :param edges: A list of dictionaries containing edges.
        :return: Edges with 'from' and 'to' node_id.
        :rtype: List of tuples
        """
        edges_list = []
        for edge in edges:
            edge_tuple = (edge.source, edge.target)
            edges_list.append(edge_tuple)
        return edges_list

    @staticmethod
    def include_node_positions(node: Nodes, nodes_list: List[Nodes]) -> None:
        """
        This function takes x and y positions from list of nodes and includes them in the input nodes list.
        :param node: A single node dictionary.
        :param nodes_list: A list of node_ids.
        :return: None.
        """

        for each_position in nodes_list:
            if node.id == each_position.get("id"):
                node.positions = Position(
                    x=each_position.get("x", None), y=each_position.get("y", None)
                )
            break

    def output_nodes_formatting(
        self, nodes: List[Nodes], nodes_list: List[Dict]
    ) -> List[Nodes]:
        """
        This function is used for iterating through nodes list given as input by the user for formatting output.
        :param nodes: A list of dictionaries containing nodes information.
        :param nodes_list: A list of node_ids.
        :return: None.
        """
        for node in nodes:
            self.include_node_positions(node, nodes_list)
        return nodes

    def create_graph(self, nodes: List[Nodes], edges: List[Edges]) -> nx.DiGraph:
        g = nx.DiGraph()
        nodes_list = self.fetch_node_format(nodes)
        edges_list = self.fetch_edge_format(edges)
        g.add_nodes_from(nodes_list)
        g.add_edges_from(edges_list)
        return g

    @staticmethod
    def format_output_nodes(nodes: List[Dict]) -> List[Nodes]:
        for node in nodes:
            node["positions"] = {}
        return [Nodes(**node) for node in nodes]

    @staticmethod
    def format_output_edges(edges: list[dict]) -> List[Edges]:
        return [Edges(**edge.get("data")) for edge in edges]

