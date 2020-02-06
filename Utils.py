#!/usr/bin/python3
# coding=utf-8
import Tiles
import TileList
import typing


class TileNameConvertor:
    def __init__(self):
        pass

    def run(self, _tile_list: TileList.TileList) -> typing.List[str]:
        name_list = []
        
        for tile in _tile_list.get_list():
            tile_category = tile.get_category()
            tile_type     = tile.get_type()
            tile_sequence = tile.get_type()

            if tile_category == Tiles.TileCategories.SUITS:
                if tile_type == Tiles.TileTypes.SUIT_DOTS:
                    if (tile_sequence.value >= 1) and (tile_sequence.value <= 9):
                        name_list.append(str(tile_sequence.value)+"t")                
                    else:
                        name_list.append("error")

                elif tile_type == Tiles.TileTypes.SUIT_BAMBOO:
                    if (tile_sequence.value >= 1) and (tile_sequence.value <= 9):
                        name_list.append(str(tile_sequence.value)+"s")                
                    else:
                        name_list.append("error")

                elif tile_type == Tiles.TileTypes.SUIT_CHARACTERS:
                    if (tile_sequence.value >= 1) and (tile_sequence.value <= 9):
                        name_list.append(str(tile_sequence.value)+"w")                
                    else:
                        name_list.append("error")

                else:
                    name_list.append("error")

            elif tile_category == Tiles.TileCategories.HONORS:
                if tile_type == Tiles.TileTypes.HONOR_WINDS:
                    if tile_sequence == Tiles.TileSequences.HONOR_EAST:
                        name_list.append("east")
                    elif tile_sequence == Tiles.TileSequences.HONOR_SOUTH:
                        name_list.append("south")
                    elif tile_sequence == Tiles.TileSequences.HONOR_WEST:
                        name_list.append("west")
                    elif tile_sequence == Tiles.TileSequences.HONOR_NORTH:
                        name_list.append("north")
                    else:
                        name_list.append("error")
                
                elif tile_type == Tiles.TileTypes.HONOR_DRAGONS:
                    if tile_sequence == Tiles.TileSequences.HONOR_RED:
                        name_list.append("red")
                    elif tile_sequence == Tiles.TileSequences.HONOR_GREEN:
                        name_list.append("green")
                    elif tile_sequence == Tiles.TileSequences.HONOR_WHITE:
                        name_list.append("white")
                    else:
                        name_list.append("error")
                else:
                    name_list.append("error")

            elif tile_category == Tiles.TileCategories.BONUS:
                if tile_type == Tiles.TileTypes.BONUS_SEASONS:
                    if tile_sequence == Tiles.TileSequences.BONUS_SPRING:
                        name_list.append("spring")
                    elif tile_sequence == Tiles.TileSequences.BONUS_SUMMER:
                        name_list.append("summer")
                    elif tile_sequence == Tiles.TileSequences.BONUS_AUTUMN:
                        name_list.append("autumn")
                    elif tile_sequence == Tiles.TileSequences.BONUS_WINTER:
                        name_list.append("winter")
                    else:
                        name_list.append("error")

                elif tile_type == Tiles.TileTypes.BONUS_FLOWERS:
                    if tile_sequence == Tiles.TileSequences.BONUS_PLUM:
                        name_list.append("plum")
                    elif tile_sequence == Tiles.TileSequences.BONUS_ORCHID:
                        name_list.append("orchid")
                    elif tile_sequence == Tiles.TileSequences.BONUS_BAMBOO:
                        name_list.append("bamboo")
                    elif tile_sequence == Tiles.TileSequences.BONUS_CHRYSANTHEMUM:
                        name_list.append("chrysanthemum")
                    else:
                        name_list.append("error")

            else:
                name_list.append("error")
        
        return name_list


    def output(self, _tile_list: TileList.TileList) -> None:
        name_list = self.run(_tile_list)
        for name in name_list:
            print(name)
