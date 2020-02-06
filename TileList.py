#!/usr/bin/python3
#coding=utf-8
import Tiles
import typing

class TileList:
    def __init__(self, _tiles: typing.List[Tiles.Tiles]):
        self.tiles = _tiles

    def get_list(self) -> typing.List[Tiles.Tiles]:
        return self.tiles

    def rearrange(self) :
        self.tiles.sort(key=Tiles.Tiles.get_id)