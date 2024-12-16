from typing import List
from unittest.mock import Mock, patch

import pytest

from graph_layouts.base import BaseLayout
from graph_layouts.constants.schemas import Edges, Nodes, OutputFormat
from graph_layouts.errors import DataFetchError
from graph_layouts.layouts.kamada_kawai_layout import KamadaKawaiLayout


@pytest.fixture
def layout():
    return KamadaKawaiLayout()


@pytest.fixture
def sample_nodes() -> List[Nodes]:
    return [
        Nodes(id="1", label="Node 1", positions={"x": 1.0, "y": 1.0}),
        Nodes(id="2", label="Node 2", positions={"x": 1.0, "y": 1.0}),
        Nodes(id="3", label="Node 3", positions={"x": 1.0, "y": 1.0}),
    ]


@pytest.fixture
def sample_edges() -> List[Edges]:
    return [
        Edges(source="1", target="2"),
        Edges(source="2", target="3"),
        Edges(source="3", target="1"),
    ]


def test_initialization(layout):
    """Test if the layout is properly initialized"""
    assert isinstance(layout, BaseLayout)
    assert hasattr(layout, "utils")
    assert hasattr(layout, "log")


def test_get_layout_success(layout, sample_nodes, sample_edges):
    """Test successful layout generation"""
    with patch.object(layout, "get_positions") as mock_get_positions:
        mock_get_positions.return_value = [
            {"id": "1", "x": 0.1, "y": 0.2},
            {"id": "2", "x": 0.3, "y": 0.4},
            {"id": "3", "x": 0.5, "y": 0.6},
        ]

        result = layout.get_layout(sample_nodes, sample_edges)

        assert isinstance(result, OutputFormat)
        assert len(result.nodes) == len(sample_nodes)
        assert len(result.edges) == len(sample_edges)

        mock_get_positions.assert_called_once_with(sample_nodes, sample_edges)


def test_get_layout_empty_nodes_edges(layout):
    """Test get_layout with empty nodes and edges lists"""
    result = layout.get_layout([], [])
    assert isinstance(result, OutputFormat)
    assert len(result.nodes) == 0
    assert len(result.edges) == 0


def test_get_layout_empty_positions(layout, sample_nodes, sample_edges):
    """Test get_layout when get_positions returns empty list"""
    with patch.object(layout, "get_positions", return_value=[]):
        layout.get_positions = Mock(return_value=[])
        with pytest.raises(DataFetchError, match="Unable to get the nodes."):
            layout.get_layout(sample_nodes, sample_edges)
