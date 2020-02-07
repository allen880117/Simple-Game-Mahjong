#!/usr/bin/python3
# coding=utf-8
import Tile as tl
import Hand as tl_list
import typing


class TileNameConvertor:
    def __init__(self):
        pass

    def run(self, _tile_list:tl_list.TileList) -> typing.List[str]:
        name_list = []
        
        for tile in _tile_list.get_list():
            tile_category = tile.get_category()
            tile_type     = tile.get_type()
            tile_sequence = tile.get_sequence()

            if tile_category == tl.TileCategories.SUITS:
                if tile_type == tl.TileTypes.SUIT_DOTS:
                    if (tile_sequence.value >= 1) and (tile_sequence.value <= 9):
                        name_list.append(str(tile_sequence.value)+"t")                
                    else:
                        name_list.append("error")

                elif tile_type == tl.TileTypes.SUIT_BAMBOO:
                    if (tile_sequence.value >= 1) and (tile_sequence.value <= 9):
                        name_list.append(str(tile_sequence.value)+"s")                
                    else:
                        name_list.append("error")

                elif tile_type == tl.TileTypes.SUIT_CHARACTERS:
                    if (tile_sequence.value >= 1) and (tile_sequence.value <= 9):
                        name_list.append(str(tile_sequence.value)+"w")                
                    else:
                        name_list.append("error")

                else:
                    name_list.append("error")

            elif tile_category == tl.TileCategories.HONORS:
                if tile_type == tl.TileTypes.HONOR_WINDS:
                    if tile_sequence == tl.TileSequences.HONOR_EAST:
                        name_list.append("east")
                    elif tile_sequence == tl.TileSequences.HONOR_SOUTH:
                        name_list.append("south")
                    elif tile_sequence == tl.TileSequences.HONOR_WEST:
                        name_list.append("west")
                    elif tile_sequence == tl.TileSequences.HONOR_NORTH:
                        name_list.append("north")
                    else:
                        name_list.append("error")
                
                elif tile_type == tl.TileTypes.HONOR_DRAGONS:
                    if tile_sequence == tl.TileSequences.HONOR_RED:
                        name_list.append("red")
                    elif tile_sequence == tl.TileSequences.HONOR_GREEN:
                        name_list.append("green")
                    elif tile_sequence == tl.TileSequences.HONOR_WHITE:
                        name_list.append("white")
                    else:
                        name_list.append("error")
                else:
                    name_list.append("error")

            elif tile_category == tl.TileCategories.BONUS:
                if tile_type == tl.TileTypes.BONUS_SEASONS:
                    if tile_sequence == tl.TileSequences.BONUS_SPRING:
                        name_list.append("spring")
                    elif tile_sequence == tl.TileSequences.BONUS_SUMMER:
                        name_list.append("summer")
                    elif tile_sequence == tl.TileSequences.BONUS_AUTUMN:
                        name_list.append("autumn")
                    elif tile_sequence == tl.TileSequences.BONUS_WINTER:
                        name_list.append("winter")
                    else:
                        name_list.append("error")

                elif tile_type == tl.TileTypes.BONUS_FLOWERS:
                    if tile_sequence == tl.TileSequences.BONUS_PLUM:
                        name_list.append("plum")
                    elif tile_sequence == tl.TileSequences.BONUS_ORCHID:
                        name_list.append("orchid")
                    elif tile_sequence == tl.TileSequences.BONUS_BAMBOO:
                        name_list.append("bamboo")
                    elif tile_sequence == tl.TileSequences.BONUS_CHRYSANTHEMUM:
                        name_list.append("chrysanthemum")
                    else:
                        name_list.append("error")

            else:
                name_list.append("error")
        
        return name_list


    def output(self, _tile_list: tl_list.TileList) -> None:
        name_list = self.run(_tile_list)
        for name in name_list:
            print(name)
