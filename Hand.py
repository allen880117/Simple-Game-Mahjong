#!/usr/bin/python3
#coding=utf-8
import Tile as tl
import typing

class Hand:
    # Constructor
    def __init__(self, _tiles: typing.List[tl.Tiles]):
        # Copy
        self.tiles = _tiles

        # Init
        self.triplet_list = typing.List[tl.Tiles] 
        self.quad_list = typing.List[tl.Tiles]
        self.sequence_list = typing.List[tl.Tiles]

    # Get and Set
    def get_tiles(self) -> typing.List[tl.Tiles]:
        return self.tiles
    
    def set_tiles(self, _tiles: typing.List[tl.Tiles]) -> None:
        self.tiles = _tiles

    def get_triplet_list(self) -> typing.List[tl.Tiles]:
        return self.triplet_list


    # Sort Tiles
    def sort_tiles(self) :
        self.tiles.sort(key=tl.Tiles.get_id)