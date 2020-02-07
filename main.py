import Hand as tl_list
import Tile as tl
import Utils

if __name__ == "__main__":
    test = []
    for num  in range(1, 10):
        test.append(tl.Tiles(
            tl.TileCategories.SUITS,
            tl.TileTypes.SUIT_BAMBOO,
            tl.TileSequences(num)
        ))
    
    test = tl_list.TileList(test)

    name_convert = Utils.TileNameConvertor()
    name_convert.output(test)