#!/usr/bin/python3
#coding=utf-8
import Tile as tl
import typing

class TileList:
    def __init__(self, _tiles: typing.List[tl.Tiles]):
        self.tile_list = _tiles
        self.triplet_list = []
        self.quad_list = []
        self.sequence_list = []

    def get_list(self) -> typing.List[tl.Tiles]:
        return self.tile_list

    def rearrange(self) :
        self.tile_list.sort(key=tl.Tiles.get_id)