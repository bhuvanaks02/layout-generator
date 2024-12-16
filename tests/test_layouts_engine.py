import logging
from unittest.mock import Mock, patch

import pytest

from graph_layouts.base import BaseLayout
from graph_layouts.constants import LayoutConstants
from graph_layouts.constants.schemas import Edges, Nodes, OutputFormat, Position
from graph_layouts.errors import InvalidClassError, InvalidLayoutName, ModuleImportError
from graph_layouts.layout_engine import GraphLayouts
from graph_layouts.utils import LayoutUtils

sample_nodes = [
    Nodes(id="1", label="Node 1", positions=Position(x=0.0, y=0.0)),
    Nodes(id="2", label="Node 2", positions=Position(x=1.0, y=1.0)),
    Nodes(id="3", label="Node 3", positions=Position(x=2.0, y=2.0)),
]

sample_edges = [Edges(source="1", target="2"), Edges(source="2", target="3")]


@pytest.fixture
def graph_layouts():
    return GraphLayouts()


def test_init(graph_layouts):
    """Test initialization of GraphLayouts class"""
    assert isinstance(graph_layouts.log, logging.Logger)
    assert isinstance(graph_layouts.utils, LayoutUtils)
    assert isinstance(graph_layouts.constants, LayoutConstants)


def test_fetch_layout_valid_module(graph_layouts):
    """Test fetch_layout with valid inputs"""
    output_nodes = graph_layouts.fetch_layout(
        "kamada_kawai_layout", sample_nodes, sample_edges
    )
    assert output_nodes is not None
    assert isinstance(output_nodes, OutputFormat)


def test_fetch_layout_default_layout(graph_layouts):
    """Test fetch_layout with default layout name"""
    output_nodes = graph_layouts.fetch_layout(nodes=sample_nodes, edges=sample_edges)
    assert output_nodes is not None
    assert isinstance(output_nodes, OutputFormat)


def test_fetch_layout_no_nodes(graph_layouts):
    """Test fetch_layout with missing nodes"""
    with pytest.raises(ValueError, match="Nodes cannot be None or empty."):
        graph_layouts.fetch_layout(
            "kamada_kawai_layout", nodes=None, edges=sample_edges
        )


def test_fetch_layout_details_valid(graph_layouts):
    """Test fetch_layout_details method for success case"""
    layout_name = "kamada_kawai_layout"
    layout_path, class_name = graph_layouts.fetch_layout_details(layout_name)

    expected_path = f"{graph_layouts.constants.module_path}.kamada_kawai_layout"
    expected_class = "KamadaKawaiLayout"

    assert layout_path == expected_path
    assert class_name == expected_class


def test_fetch_layout_details_invalid_layout(graph_layouts):
    layout_name = "spring_layout"
    with pytest.raises(InvalidLayoutName, match="Layout name is not valid."):
        graph_layouts.fetch_layout_details(layout_name)


def test_fetch_layout_details_empty_layout(graph_layouts):
    """Test fetch_layout_details with empty layout name"""
    with pytest.raises(InvalidLayoutName, match="Layout name is not valid."):
        graph_layouts.fetch_layout_details("")


@patch("importlib.import_module")
@patch(
    "builtins.issubclass", return_value=True
)  # Mock issubclass to always return True
def test_fetch_dynamic_module_valid(mock_issubclass, mock_importlib, graph_layouts):
    """Test fetch_dynamic_module for success case"""
    mock_layout_class = Mock(spec=BaseLayout)
    mock_instance = Mock(spec=BaseLayout)
    mock_layout_class.return_value = mock_instance
    mock_module = Mock()
    mock_module.KamadaKawaiLayout = mock_layout_class  # Ensure it's a mock class
    mock_importlib.return_value = mock_module

    layout_name = "kamada_kawai_layout"
    result = graph_layouts.fetch_dynamic_module(layout_name)

    expected_path = f"{graph_layouts.constants.module_path}.kamada_kawai_layout"
    mock_importlib.assert_called_once_with(expected_path)

    assert result == mock_instance


@patch("importlib.import_module")
def test_fetch_dynamic_module_import_error(mock_importlib, graph_layouts):
    """Test fetch_dynamic_module when import fails"""
    mock_importlib.side_effect = ModuleImportError("Unable to import module")

    with pytest.raises(ModuleImportError):
        graph_layouts.fetch_dynamic_module("kamada_kawai_layout")


@patch("importlib.import_module")
def test_fetch_dynamic_module_missing_class(mock_importlib, graph_layouts):
    """Test fetch_dynamic_module when class is missing"""
    mock_module = Mock()
    mock_module.KamadaKawaiLayout = None
    mock_importlib.return_value = mock_module
    class_name = "KamadaKawaiLayout"
    with pytest.raises(InvalidClassError, match=f"{class_name} is an invalid class"):
        graph_layouts.fetch_dynamic_module("kamada_kawai_layout")


@patch("importlib.import_module")
def test_fetch_dynamic_module_invalid_class(mock_importlib, graph_layouts):
    """Test fetch_dynamic_module when class is not a BaseLayout"""

    class InvalidClass:
        pass

    mock_module = Mock()
    mock_module.KamadaKawaiLayout = InvalidClass
    mock_importlib.return_value = mock_module

    with pytest.raises(TypeError, match="Class is not a subclass of BaseLayout"):
        graph_layouts.fetch_dynamic_module("kamada_kawai_layout")
