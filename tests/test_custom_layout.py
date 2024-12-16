import inspect
from unittest.mock import patch

import pytest

from graph_layouts.constants.schemas import Edges, Nodes, OutputFormat
from graph_layouts.errors import DataFetchError
from graph_layouts.layouts.custom_layout import CustomLayout
from graph_layouts.utils import LayoutUtils


@pytest.fixture
def custom_layout():
    return CustomLayout()


@pytest.fixture
def mock_constants():
    return {
        "rca_node_types": {
            "currently_selected_node": ["Investigated Event"],
            "left_positioned_nodes": ["Probable Cause"],
            "right_positioned_nodes": ["RecommendedAction", "CorrectiveProcedure"],
        },
        "rca_node_positions": {"midpoint": [100, 300], "node_spacing": [350, 250]},
    }


@pytest.fixture
def sample_nodes():
    return [
        Nodes(id="1", topText="Investigated Event"),
        Nodes(id="2", topText="Probable Cause"),
        Nodes(id="3", topText="Probable Cause"),
        Nodes(id="4", topText="RecommendedAction"),
        Nodes(id="5", topText="CorrectiveProcedure"),
    ]


@pytest.fixture
def sample_edges():
    return [
        Edges(source="1", target="2"),
        Edges(source="2", target="3"),
        Edges(source="1", target="4"),
    ]


def test_initialization(custom_layout):
    """Test proper initialization of CustomLayout"""
    assert isinstance(custom_layout, CustomLayout)
    assert custom_layout.constants is not None
    assert custom_layout.utils is not None


@patch.object(LayoutUtils, "output_nodes_formatting")
def test_get_layout_success(mock_format, custom_layout, sample_nodes, sample_edges):
    """Test layout generation for success status"""
    mock_format.return_value = sample_nodes
    result = custom_layout.get_layout(sample_nodes, sample_edges)

    assert isinstance(result, OutputFormat)
    assert result.nodes == sample_nodes
    assert result.edges == sample_edges
    mock_format.assert_called_once()


def test_get_layout_no_nodes(custom_layout):
    """Testing get_layout() with empty nodes list"""
    with pytest.raises(DataFetchError, match="Unable to get the nodes."):
        custom_layout.get_layout([], [])


def test_get_positions_valid(custom_layout, sample_nodes, sample_edges):
    """Test `get_positions` with valid data."""

    positions = custom_layout.get_positions(sample_nodes, sample_edges)
    assert inspect.isgenerator(positions)
    positions_list = list(positions)
    assert len(positions_list) == 5
    assert positions_list[0].get("id") == "1"
    assert isinstance(positions_list[0], dict)
