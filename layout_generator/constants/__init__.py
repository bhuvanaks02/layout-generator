from layout_generator.constants.schemas import Edges, Nodes


class LayoutConstants:
    """
    The class contains all the constants that will be required for the graph layouts.
    """

    module_path = "layout_generator.layouts"
    layout_name = "kamada_kawai_layout"
    available_layouts = ["kamada_kawai_layout", "custom_layout"]
    rca_node_types = {
        "left_positioned_nodes": ["Probable Cause"],
        "right_positioned_nodes": ["RecommendedAction", "CorrectiveProcedure"],
        "currently_selected_node": ["Investigated Event"],
    }
    rca_node_positions = {"midpoint": [100, 300], "node_spacing": [350, 250]}
