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

