from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Node:
    name: str


@dataclass
class Edge:
    src: str
    dst: str
    label: Optional[str] = None


@dataclass
class WorldMap:
    nodes: Dict[str, Node] = field(default_factory=dict)
    edges: List[Edge] = field(default_factory=list)

    def add_node(self, name: str):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, src: str, dst: str, label: Optional[str] = None):
        self.add_node(src)
        self.add_node(dst)
        self.edges.append(Edge(src, dst, label))


def parse_map(text: str) -> WorldMap:
    world = WorldMap()

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        left, *rest = line.split(":")
        src, dst = map(str.strip, left.split("->"))
        label = rest[0].strip() if rest else None

        world.add_edge(src, dst, label)

    return world

