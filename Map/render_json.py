import json
from mapgen import WorldMap


def render_json(world: WorldMap) -> str:
    data = {
        "nodes": list(world.nodes.keys()),
        "edges": [
            {
                "from": e.src,
                "to": e.dst,
                "label": e.label
            }
            for e in world.edges
        ]
    }
    return json.dumps(data, indent=2)

