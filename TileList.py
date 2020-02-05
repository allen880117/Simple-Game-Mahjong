import Tiles

class TileList:
    def __init__(self, _tiles: list) :
        self.tiles = _tiles

    def rearrange(self) :
        self.tiles.sort(key=Tiles.TileAttributes.get_type_id)