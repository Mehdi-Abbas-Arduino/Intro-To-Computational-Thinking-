import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q3_testcases = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7, None, [0, 1, 2, 6, 5, 4, 3, 7, 8, 9], True),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2, -4, None, [0, 1, 5, 4, 3, 2, 6, 7, 8, 9], True),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 10, None, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], True),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, -1, None, [8, 7, 6, 5, 4, 3, 2, 1, 0, 9], True),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20, 30, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -20, -10, None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True),
    ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], 2, 6, None, [2, 3, 13, 11, 7, 5, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], True),
    ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], 3, -3, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', 'd2577e5cc60c488670fdd2c6cb8e1ea86e6288721d7a0acebda7b8ade3caf1cd', False),
    ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], 0, 16, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', 'c0c3d6619a49199299d41f1497dad9560c05f13002c7f846c73cdf07a5fe4d73', False),
    ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], 0, -1, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', '21b6d2b64d2f7cc372f9d9f69d498f87242d4a0a6786e10cd966b4585d3bde38', False),
    ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], 23, 29, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', '52ddf73a3a7c4159026468d4a45f85da62263b8417bd2121584c44b9f70c596c', False),
    ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], -7, 0, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', '52ddf73a3a7c4159026468d4a45f85da62263b8417bd2121584c44b9f70c596c', False),
    (['gerbil', 'cat', 'dog', 'grey parrot', 'horse', 'goldfish', 'rabbit', 'hamster', 'otter', 'manatee', 'peacock', 'snake', 'gerbil', 'lion', 'elephant', 'gerbil', 'gerbil', 'rhinoceros', 'gerbil', 'hippopotamus', 'koala', 'gerbil'], 9, 15, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', '2d004646402296cd37fe455f1817bfe689210256a5bba6c1614e3527120095f4', False),
    (['gerbil', 'cat', 'dog', 'grey parrot', 'horse', 'goldfish', 'rabbit', 'hamster', 'otter', 'manatee', 'peacock', 'snake', 'gerbil', 'lion', 'elephant', 'gerbil', 'gerbil', 'rhinoceros', 'gerbil', 'hippopotamus', 'koala', 'gerbil'], 3, -1, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', 'e44a12e745dfd838d83e05d68f6f6672d43cbe51d96bb8b68fb18e839aecd771', False),
    (['gerbil', 'cat', 'dog', 'grey parrot', 'horse', 'goldfish', 'rabbit', 'hamster', 'otter', 'manatee', 'peacock', 'snake', 'gerbil', 'lion', 'elephant', 'gerbil', 'gerbil', 'rhinoceros', 'gerbil', 'hippopotamus', 'koala', 'gerbil'], 0, 22, 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91', '8bc39736caa6823cebcf52977ee693991a9da1cf5f3f648bc43f247535d46c8d', False),
]


@pytest.mark.parametrize("t, start, stop, expected_return, expected_list, visible", q3_testcases)
def test_q3(t, start, stop, expected_return, expected_list, visible):
    actual_return = reverse_slice(t, start, stop)

    if visible:
        assert actual_return == expected_return
        assert t == expected_list
    else:
        assert hashcode(actual_return) == expected_return
        assert hashcode(t) == expected_list