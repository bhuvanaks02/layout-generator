from unittest.mock import MagicMock, patch

from graph_layouts.layout_engine import BaseLayout


class ConcreteLayoutForTest(BaseLayout):
    def get_layout(self, nodes, edges):
        pass

    def get_positions(self, nodes, edges, *args):
        pass


@patch("graph_layouts.layout_engine.logging.getLogger")
def test_logging_initialization(mock_get_logger):
    """Test that the logging setup in BaseLayout is initialized correctly."""

    mock_logger_instance = MagicMock()
    mock_get_logger.return_value = mock_logger_instance

    layout_instance = ConcreteLayoutForTest()
    mock_get_logger.assert_called_once()

    layout_instance.log.info("Test log message")
    mock_logger_instance.info.assert_called_once_with("Test log message")
