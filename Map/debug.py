from mapgen import WorldMap


def render_ascii(world: WorldMap) -> str:
    lines = []
    for edge in world.edges:
        if edge.label:
            lines.append(f"[{edge.src}] -> [{edge.dst}]  ({edge.label})")
        else:
            lines.append(f"[{edge.src}] -> [{edge.dst}]")
    return "\n".join(lines)

