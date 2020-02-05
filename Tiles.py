import enum

class TileCategories(enum.Enum):
    # category
    SUITS  = "suits"
    HONORS = "honors"
    BOUNS  = "bonus"
    
    # unknown
    UNKNOWN_CATEGORY = "unknown_category"

class TileTypes(enum.Enum):
    # suit
    DOTS       = "dots"
    BAMBOO     = "bamboo"
    CHARACTERS = "characters"

    # honor
    WINDS   = "winds"
    DRAGONS = "dragons"

    # bonus
    SEASONS = "seasons"
    FLOWERS = "flowers"

    # unknown
    UNKNOWN_TYPE = "unknown_type"

class TileSequences(enum.Enum):
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
    EAST  = "east"
    SOUTH = "south"
    WEST  = "west"
    NORTH = "north"

    # honor - dragon
    RED   = "red"
    GREEN = "grenn"
    WHITE = "white"

    # bonus - season
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"

    # bonus - flower
    PLUM          = "plum"
    ORCHID        = "orchid"
    CHRYSANTHEMUM = "chrysanthemum"
    BAMBOO        = "bamboo"

    # unknown
    UNKNOWN_SEQUENCE = "unknown_sequence"

class TileAttributes:
    def __init__(self, _category: TileCategories, _type: TileTypes, _seq: TileSequences) :
        self.category = _category
        self.type = _type
        self.sequence = _seq

class Tiles:
    def __init__(self, _attribute: TileAttributes) :
        self.attribute = _attribute