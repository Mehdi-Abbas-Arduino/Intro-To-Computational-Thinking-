import hashlib
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q4 import color_neighbors


def hashcode(colors):
    return hashlib.sha256(str(sorted(colors)).encode("utf-8")).hexdigest()


q4_testcases = [
    ([['Red', 'Blue', 'Green', 'Cyan'], ['Yellow', 'Black', 'White', 'Brown'], ['Pink', 'Orange', 'Purple', 'Gray']], 'Black', ['Blue', 'Orange', 'White', 'Yellow'], True),
    ([['Red', 'Blue', 'Green', 'Cyan'], ['Yellow', 'Black', 'White', 'Brown'], ['Pink', 'Orange', 'Purple', 'Gray']], 'Blue', ['Black', 'Green', 'Red'], True),
    ([['Red', 'Blue', 'Green', 'Cyan'], ['Yellow', 'Black', 'White', 'Brown'], ['Pink', 'Orange', 'Purple', 'Gray']], 'Gray', ['Brown', 'Purple'], True),

    ([['Gold']], 'Gold', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([['Violet', 'Indigo']], 'Violet', '396e78d0e450374dfa73512e30639439b7641c398d4e3476491613a053ee1c60', False),
    ([['Amber', 'Beige', 'Coral', 'Denim', 'Emerald']], 'Coral', 'a108ae242339567fdceaf2d922572372d9994004b1969c2797755636a3446e84', False),
    ([['Rose'], ['Mint'], ['Navy'], ['Olive']], 'Mint', '1949364d6e6b1ba506fa21a765c2b7bc6503c489c1ac2970cdad76045d6e11a2', False),
    ([['Ruby'], ['Jade'], ['Silver'], ['Copper'], ['Pearl']], 'Pearl', 'b4aedcf5e84647da29a07a4cc2c93f966b84fc7d786c1e70814a533e0e951f2e', False),
    ([['Crimson', 'Teal'], ['Ivory', 'Onyx']], 'Onyx', '7799359aac72dc32f4ab45e4af29f615bb31feea01cd7a760bdbf7cb4aad8ea3', False),
    ([['Scarlet', 'Azure', 'Lemon', 'Umber', 'Lilac'], ['Mauve', 'Sienna', 'Khaki', 'Cream', 'Plum']], 'Lemon', '30f8f104615bb3f0b66f5afdeb12afd3bb232044c6cf5d28eddcea3c6e73efc4', False),
    ([['Brick', 'Mustard'], ['Aqua', 'Fuchsia'], ['Tan', 'Maroon'], ['Lavender', 'Charcoal'], ['Cerulean', 'Sand']], 'Maroon', 'f63667bb66f44094cbb93a1037c470e4b3313b9379118c660b57860619cc8f4b', False),
    ([['Tomato', 'Sky', 'Lime', 'Snow'], ['Steel', 'Apricot', 'Blush', 'Ink'], ['Fern', 'Bronze', 'Pear', 'Flax'], ['Rust', 'Peach', 'Pine', 'Cocoa']], 'Apricot', '4da73a10470d92afc0a596d9fbf4942b191b5400531fc1ccd48b270f73badc52', False),
    ([['Ocher', 'Moss', 'Cloud', 'Mint Green', 'Garnet'], ['Wheat', 'Ash', 'Periwinkle', 'Rosewood', 'Salmon'], ['Bisque', 'Turquoise', 'Burgundy', 'Ivory White', 'Pumpkin'], ['Slate', 'Magenta', 'Olive Green', 'Dove', 'Mulberry'], ['Cobalt', 'Honey', 'Lilac Gray', 'Seashell', 'Midnight Blue']], 'Burgundy', '68269aa9a57f3970f1ff76fe08a1a2599c29d28fafbfdd1f874c5bf857a67b5d', False),
    ([['Ice', 'Wine', 'Forest', 'Beige', 'Pearl White', 'Amber Gold'], ['Coral Red', 'Ocean', 'Raspberry', 'Dusty Pink', 'Blue Gray', 'Canary'], ['Tangerine', 'Sage', 'Smoke', 'Pistachio', 'Copper Red', 'Stone'], ['Lilac Blue', 'Auburn', 'Mint Blue', 'Rose Pink', 'Denim Blue', 'Butter']], 'Pistachio', '22f01a71ba05c79e83ed6f2bc1687a374e694319a4fe5cbe3dee62b5fd1ff341', False),
    ([['Marigold', 'Basil', 'Orchid', 'Linen'], ['Carmine', 'Alabaster', 'Mulberry Red', 'Turquoise Blue'], ['Beryl', 'Fawn', 'Amethyst', 'Eggplant']], 'Fawn', '5c9cc2720870e2d50a0eb48a28ae9b2b7cafcfd85e0f172e51dad9225b150e1d', False),
]


@pytest.mark.parametrize("tile_wall, target_color, expected, visible", q4_testcases)
def test_q4(tile_wall, target_color, expected, visible):
    result = color_neighbors(tile_wall, target_color)

    assert isinstance(result, list), "Return a list of neighboring colors."
    assert all(isinstance(color, str) for color in result), (
        "Every neighboring color must be a string."
    )

    if visible:
        assert sorted(result) == sorted(expected)
    else:
        assert hashcode(result) == expected