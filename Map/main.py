from mapgen import parse_map
from debug import render_ascii
from render_json import render_json


if __name__ == "__main__":
    text = """
    Stoneford -> Rivershade : Caravan Route (Contested Hills)
    Greenhollow -> Rivershade
    Rivershade -> Quarry Ruins Dungeon : Old Quarry Road (East)
    """

    world = parse_map(text)

    print("ASCII MAP")
    print(render_ascii(world))

    print("\nJSON MAP")
    print(render_json(world))

