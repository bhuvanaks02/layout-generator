from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Position(BaseModel):
    x: float = None
    y: float = None


class Nodes(BaseModel):
    id: str
    label: Optional[str] = None
    positions: Optional[Position] = {}

    model_config = ConfigDict(extra="allow")


class Edges(BaseModel):
    source: str
    target: str

    model_config = ConfigDict(extra="allow")


class OutputFormat(BaseModel):
    nodes: List[Nodes]
    edges: List[Edges]
