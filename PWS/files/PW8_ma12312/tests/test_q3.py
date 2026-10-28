import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q3 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q3_testcases = [
    # Visible Testcases
    (['ab', 'aab', 'abb', 'abab', 'abaaaba'], [0, 1, 1, 0, 1], True),
    (['aa'], [1], True),
    (['aaaaaa'], [3], True),
    (['abababab'], [0], True),
    (['aabbcc'], [3], True),

    # Hidden Testcases
    (['keyhbmeknckfavrpqyyfjxjjmivtsftikovkcdcwefctqrqjryhtlcvstm', 'rpqipvntglpsbmoyxpjhkfufrxgnqjvhtizxn', 'sddpeibedjk', 'dkxqcthvgmzymoohniertqanrbkfdolfwfaalwolqpipngsaquxurvzwjpfejkfyys', 'jdzsnpejkyqktrdlljfuozlfsvrhqrwgtojnxllzmbfvoexxxttzcbprwzyztsovcxootxoswbffcokhtosfvn', 'hwqfvaiqxdksxvbtcr', 'bsdmsblyvzulromgbvteqxqahed', 'geptwdurphheydbyxrm', 'rplpqbzsnpotqwmcrdyckzfyghzz'], '8cd4126e6bda44c50f7e2ca6d7d30d088222203dcec117a15b5cc792c88791f5', False),
    (['sofkfrrvoqaakwzksohvmnncpfgblidcsclggmghighzzhrjhmnvdkgxsloi', 'mxrghbmoqwoajqcaqzqxinbjtnkywtbxwjmqatmct', 'apgythaslgwdjdwvkrzgxbwluhlopfrelci', 'qjqswxhvmlwecxrnnvuqgydcduvjxohelcwyawvecoltdwgueqloivvtkadsabdlcnxpnybxjfhnoplllvoxwwopvhord', 'jtepxcmubqbitxzzplidjenuoaulbkpktfglkmfvcknxqmeyu', 'ftfaqndypcxejvxiosgojdmfccpk', 'ubtkhbuzmlqkpbbbwrvstnjvxjbtncbwzorusdnzmkbdjvyhzzvugnchsy', 'fhymcsiltwjjiownaszuwbnaeorpimjfwt'], 'ea288350e2a9edce8b1f2c5dc74e858bef142dc2e24831aa5bfb465e5e8f386b', False),
    (['zqzcdhefjzuqfkigwydqalimitpkwduxsauxslqanstag', 'vmggdujscxesizsjycskimjtqfcoctyrgxjdpyeowavlriojizsrggnywkijdodicyhfreurltzaouzksugugn', 'ouojrgpgkuixdbuddltrvfpjzzwafmqdmmku', 'zqbfnhbabvfavoztvohurpgicqtczwnxvlxxtvuglaqltafawjcwgagjinrdmobhnauebvgdufxegtbgaqysfwdqyhsgloahwnb', 'lasoembsbtjgwacvuvygavlwfuedjwwhyhyjwxkfbtofjogogkjojyxncfmekmowcjmk', 'rdfrxmmwwgyfwrboqfnwpngroegtkfoyypektjj', 'gpslaqjtcxixtsucjvjolxjbndilpdtzxdndlow', 'xwrhmpcsqmednmqzthrtjlnggvfpmdqkfadhe'], '1805208115236cb54229676d9730c8ee6dd350d4402fafb1b9003da66a6f26da', False),
    (['mmcnmyiqmtzleuwggsjobbo', 'shkcwkkaygdtuidyzzzimaqbncrbjertmnkrgasxloakmxpwbcrlxmupegqbwdrijmav', 'mglbmlmjybxjafrnyqtqtamdgdl', 'hqyahcmdkmugjxclyrbchnlfpcspyahjsuvzeraepczucimxlwymyagztaxkmdjugiqkxdl', 'zohkphryovtojrdmlggtmjwzqzaccizgewsipkomdebfsnaravtolchgckayihzciychvqbdqxdbesapmerdposvqlukadfhds', 'axmackfvewddkhizugyfumixjmyfkqboqfccjupgtdnfaanhlkddefgotcxalgscos'], '5b79e1bbb5f86a991c3bec8519195bf273d101f7652c72df36dc2fb68eb66fc6', False),
    (["a" * 100000], '5c3e6ad4119ed2d270e1ff567668ca6f69a56e7a10f036a3d37c7bceab3d119a', False),
    (["ab" * 50000], 'd0bca111f8628137adc4c16f123496dcdd1d590d06cb5d9acd68b39fe656fb97', False),
    (['abba'], '080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22', False),
    (['aaa'], '080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22', False),
    (['aaaaa'], '038966de9f6b9a901b20b4c6ca8b2a46009feebe031babc842d43690c0bc222b', False),
    (['aabbaa'], '06d033ece6645de592db973644cf7357255f24536ff7b03c3b2ace10736f7636', False),
]

@pytest.mark.parametrize("words, expected, visible", q3_testcases)
def test_q3(words, expected, visible):
    result = minimum_replacements(words)
    assert isinstance(result, list)
    assert len(result) == len(words)
    assert all(isinstance(value, int) for value in result)
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
