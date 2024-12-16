from graph_layouts.constants import LayoutConstants


def test_module_path():
    """Test if the module path is set correctly in LayoutConstants."""
    expected_path = "graph_layouts.layouts"
    assert LayoutConstants.module_path == expected_path


def test_layout_name():
    """Test if the layout name is set correctly in LayoutConstants."""
    expected_layout_name = "kamada_kawai_layout"
    assert LayoutConstants.layout_name == expected_layout_name


def test_available_layouts():
    """Test if the available layouts list is correctly set in LayoutConstants."""
    expected_layouts = ["kamada_kawai_layout", "custom_layout"]
    assert LayoutConstants.available_layouts == expected_layouts
    assert (
        "kamada_kawai_layout" in LayoutConstants.available_layouts
    ), "'kamada_kawai_layout' should be in available_layouts"
    assert "custom_layout" in LayoutConstants.available_layouts
