from graph_layouts import GraphLayouts
from graph_layouts.utils import LayoutUtils

nodes = [
    {
        "topText": "Investigated Event",
        "project_id": "project_259",
        "label": "Compressor Air Pressure Issue",
        "id": "6768",
        "node_id": "6768",
        "event_id": "6768",
        "linked_node": "alarm_configuration_124",
        "hierarchy": "site_100$dept_100$line_159$equipment_7468",
        "source_id": "alarm_event_35070237",
        "timestamp": "27 Sep 2024, 22:53",
        "border_type": "dashed",
        "color": {
            "background": "#f1f1f1",
            "highlight": {"border": "#a6a5a4"},
            "border": "#a6a5a4",
        },
        "clickable": False,
        "node_type": "Event",
        "level_name": "",
    },
    {
        "topText": "Probable Cause",
        "project_id": "project_259",
        "label": "Compressor Pump Failure",
        "id": "6754",
        "node_id": "6754",
        "event_id": "6754",
        "linked_node": "alarm_configuration_126",
        "hierarchy": "site_100$dept_100$line_159$equipment_7468",
        "source_id": "alarm_event_35069929",
        "timestamp": "25 Sep 2024, 12:53",
        "border_type": "solid",
        "color": {
            "background": "#f1f1f1",
            "highlight": {"border": "#ce87fa"},
            "border": "#ce87fa",
        },
        "clickable": True,
        "node_type": "Event",
        "level_name": "",
    },
    {
        "topText": "RecommendedAction",
        "project_id": "project_259",
        "label": "Adjust pressure regulator to proper settings",
        "id": "jCbacx9gFQ4AaFuQNjQczX",
        "node_id": "jCbacx9gFQ4AaFuQNjQczX",
        "event_id": None,
        "linked_node": None,
        "hierarchy": None,
        "source_id": None,
        "timestamp": None,
        "border_type": "solid",
        "color": {
            "background": "#f1f1f1",
            "highlight": {"border": "#3F9A3B"},
            "border": "#3F9A3B",
        },
        "clickable": True,
        "node_type": "RecommendedAction",
        "level_name": "Rotary screw compressor manual.pdf",
    },
    {
        "topText": "RecommendedAction",
        "project_id": "project_259",
        "label": "Clean or replace air filter",
        "id": "ZnsfhCobMi6T25Rsixi3gf",
        "node_id": "ZnsfhCobMi6T25Rsixi3gf",
        "event_id": None,
        "linked_node": None,
        "hierarchy": None,
        "source_id": None,
        "timestamp": None,
        "border_type": "solid",
        "color": {
            "background": "#f1f1f1",
            "highlight": {"border": "#3F9A3B"},
            "border": "#3F9A3B",
        },
        "clickable": True,
        "node_type": "RecommendedAction",
        "level_name": "Rotary screw compressor manual.pdf",
    },
]
edges = [
    {
        "data": {
            "id": "217mdc-S6754-pat-S6768",
            "label": "Causes",
            "source": "6754",
            "target": "6768",
            "arrows": "to",
            "color": "black",
        }
    },
    {
        "data": {
            "id": "aos-Salarm_configuration_124-e8l-SjCbacx9gFQ4AaFuQNjQczX",
            "label": "ResolvedBy",
            "source": "6768",
            "target": "jCbacx9gFQ4AaFuQNjQczX",
            "arrows": "to",
            "color": "black",
        }
    },
    {
        "data": {
            "id": "8po-Salarm_configuration_124-e8l-SZnsfhCobMi6T25Rsixi3gf",
            "label": "ResolvedBy",
            "source": "6768",
            "target": "ZnsfhCobMi6T25Rsixi3gf",
            "arrows": "to",
            "color": "black",
        }
    },
    {
        "data": {
            "id": "9i4-Salarm_configuration_124-e8l-SZnsfhCobMi6T25Rsixi3gf",
            "label": "ResolvedBy",
            "source": "6768",
            "target": "ZnsfhCobMi6T25Rsixi3gf",
            "arrows": "to",
            "color": "black",
        }
    },
    {
        "data": {
            "id": "aak-Salarm_configuration_124-e8l-SZnsfhCobMi6T25Rsixi3gf",
            "label": "ResolvedBy",
            "source": "6768",
            "target": "ZnsfhCobMi6T25Rsixi3gf",
            "arrows": "to",
            "color": "black",
        }
    },
]
node_list = LayoutUtils().format_output_nodes(nodes)
edge_list = LayoutUtils().format_output_edges(edges)
output_format = GraphLayouts().fetch_layout(layout_name="custom_layout", nodes=node_list, edges=edge_list)
print(output_format)
