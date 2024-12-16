import importlib
import logging
from typing import List

from layout_generator.base import BaseLayout
from layout_generator.constants import LayoutConstants
from layout_generator.constants.schemas import Edges, Nodes, OutputFormat
from layout_generator.errors import InvalidClassError, InvalidLayoutName, ModuleImportError
from layout_generator.utils import LayoutUtils


class GraphLayouts:
    """
    This class of the Layouts SDK is used to call the function fetch_layouts() which dynamically imports the
    specific layout mentioned and gives the positions of nodes and edges based on various parameters.
    """

    def __init__(self):
        self.log = logging.getLogger("Initializing Graph Layouts")
        self.utils = LayoutUtils()
        self.constants = LayoutConstants()

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
        :return: Dictionary which gives output format of nodes and edges with their respective positions
        """
        try:
            if not layout_name:
                layout_name = self.constants.layout_name
            if not nodes:
                raise ValueError("Nodes cannot be None or empty.")
            self.log.info(f"fetch_layout: Fetching layout for {layout_name}")
            layout_object = self.fetch_dynamic_module(layout_name)
            output_nodes = layout_object.get_layout(nodes=nodes, edges=edges)
            return output_nodes

        except Exception as e:
            self.log.error(e.args)
            raise

    def fetch_layout_details(self, layout_name: str) -> List[str]:
        """
        The function fetches full module path and class name of the particular module or layout being called.
        :param layout_name: A string denoting the name of the layout algorithm.
        :return: List of strings which gives full module path and the converted class name.
        """
        try:
            layout_path = f"{self.constants.module_path}.{layout_name}"
            if layout_name not in LayoutConstants.available_layouts:
                raise InvalidLayoutName(InvalidLayoutName.message)
            class_name = self.utils.snakecase_to_camelcase(layout_name)
            return [layout_path, class_name]
        except Exception as e:
            self.log.error(e.args)
            raise

    def fetch_dynamic_module(self, layout_name: str) -> type(BaseLayout):
        """
        The function takes the layout name and dynamically imports the particular class in the layouts folder and
         returns an object of that class.
        :param layout_name: A string denoting the name of the layout algorithm.
        :return: An object of the specific layout algorithm's class.
        """
        try:
            layout_path, class_name = self.fetch_layout_details(layout_name)
            module_name = importlib.import_module(layout_path)
            if not module_name:
                raise ModuleImportError(ModuleImportError.message)
            node_positions = getattr(module_name, class_name, None)

            if not node_positions:
                raise InvalidClassError(f"{class_name} is an invalid class")

            if not issubclass(node_positions, BaseLayout):
                raise TypeError("Class is not a subclass of BaseLayout")

            return node_positions()

        except Exception as e:
            self.log.error(e.args)
            raise
