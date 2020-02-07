#!/usr/bin/python3
#coding=utf-8
import enum

class TileCategories(enum.IntEnum):  # NUMBER: 4
    # unknown
    UNKNOWN_CATEGORY = 0

    # category
    SUITS  = 1
    HONORS = 2
    BONUS  = 3


class TileTypes(enum.IntEnum):  # NUMBER: 8
    # unknown
    UNKNOWN_TYPE = 0

    # suit
    SUIT_DOTS       = 1
    SUIT_BAMBOO     = 2
    SUIT_CHARACTERS = 3

    # honor
    HONOR_WINDS   = 4
    HONOR_DRAGONS = 5

    # bonus
    BONUS_SEASONS = 6
    BONUS_FLOWERS = 7


class TileSequences(enum.IntEnum):  # NUMBER: 25
    # unknown
    UNKNOWN_SEQUENCE = 0

    # suit
    SUIT_ONE   = 1
    SUIT_TWO   = 2
    SUIT_THREE = 3
    SUIT_FOUR  = 4
    SUIT_FIVE  = 5
    SUIT_SIX   = 6
    SUIT_SEVEN = 7
    SUIT_EIGHT = 8
    SUIT_NINE  = 9

    # honor - wind
    HONOR_EAST  = 10
    HONOR_SOUTH = 11
    HONOR_WEST  = 12
    HONOR_NORTH = 13

    # honor - dragon
    HONOR_RED   = 14
    HONOR_GREEN = 15
    HONOR_WHITE = 16

    # bonus - season
    BONUS_SPRING = 17
    BONUS_SUMMER = 18
    BONUS_AUTUMN = 19
    BONUS_WINTER = 20

    # bonus - flower
    BONUS_PLUM          = 21
    BONUS_ORCHID        = 22
    BONUS_CHRYSANTHEMUM = 23
    BONUS_BAMBOO        = 24

class Tiles:
    def __init__(self, _category: TileCategories, _type: TileTypes, _seq: TileSequences):
        self.attribute = {
            'category': _category,
            'type'    : _type,
            'sequence': _seq
        }

        self.id = self.get_id()

    def get_id(self) -> int:
        return                                      \
            self.attribute['category'].value * 8  * 25 + \
            self.attribute['type'].value     * 25 +      \
            self.attribute['sequence'].value
    
    def get_category(self) -> TileCategories:
        return self.attribute['category']
    
    def get_type(self) -> TileTypes:
        return self.attribute['type']
    
    def get_sequence(self) -> TileSequences:
        return self.attribute['sequence']