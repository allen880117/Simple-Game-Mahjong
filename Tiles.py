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
    DOTS       = 1
    BAMBOO     = 2
    CHARACTERS = 3

    # honor
    WINDS   = 4
    DRAGONS = 5

    # bonus
    SEASONS = 6
    FLOWERS = 7


class TileSequences(enum.IntEnum):  # NUMBER: 25
    # unknown
    UNKNOWN_SEQUENCE = 0

    # suit
    ONE   = 1
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9

    # honor - wind
    EAST  = 10
    SOUTH = 11
    WEST  = 12
    NORTH = 13

    # honor - dragon
    RED   = 14
    GREEN = 15
    WHITE = 16

    # bonus - season
    SPRING = 17
    SUMMER = 18
    AUTUMN = 19
    WINTER = 20

    # bonus - flower
    PLUM          = 21
    ORCHID        = 22
    CHRYSANTHEMUM = 23
    BAMBOO        = 24


class TileAttributes:
    def __init__(self, _category: TileCategories, _type: TileTypes, _seq: TileSequences):
        self.type = {
            'category': _category,
            'type'    : _type,
            'sequence': _seq
        }

        self.type_id = self.get_type_id()

    def get_type_id(self) -> int:
        return                                      \
            self.type['category'].value * 8  * 25 + \
            self.type['type'].value     * 25 +      \
            self.type['sequence'].value

class Tiles:
    def __init__(self, _attribute: TileAttributes):
        self.attribute = _attribute