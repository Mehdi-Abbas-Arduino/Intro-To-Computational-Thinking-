import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from q8 import leading_letters


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q8_testcases = [("'Never again, never again shall I submit to superior force.'",
  {'A': ['again,'],
   'B': [],
   'C': [],
   'D': [],
   'E': [],
   'F': ["force.'"],
   'G': [],
   'H': [],
   'I': ['I'],
   'J': [],
   'K': [],
   'L': [],
   'M': [],
   'N': ["'Never"],
   'O': [],
   'P': [],
   'Q': [],
   'R': [],
   'S': ['shall', 'submit', 'superior'],
   'T': ['to'],
   'U': [],
   'V': [],
   'W': [],
   'X': [],
   'Y': [],
   'Z': []},
  True,
  None),
 ('!!! co-operate Cooperate CO-OPERATE ???', ['co-operate'], True, 'C'),
 ('JULIET: Farewell. - God knows when we shall meet again. // I have a faint cold fear thrills through my veins // '
  "That almost freezes up the heat of life. // I'll call them back again to comfort me. - // Nurse! - What should she "
  'do here? // My dismal scene I needs must act alone.',
  'f810efe49ad23df66f5c96416d4fe339122cdd573ff52560cf0d4452f9fa7839',
  False,
  None),
 ('MACBETH: Is this a dagger which I see before me, // The handle toward my hand? Come, let me clutch // thee. // I '
  'have thee not, and yet I see thee still. // Art thou not, fatal vision, sensible // To feeling as to sight? Or art '
  'thou but // A dagger of the mind, a false creation // Proceeding from the heat-oppressd brain? // I see thee yet, '
  'in form as palpable // As this which now I draw.',
  '91b047e78443dd339cc393c9da794a2f6247f84a1f564a1f2974546bed70c982',
  False,
  None),
 ('PUCK: I am that merry wanderer of the night. // I jest to Oberon and make him smile // When I a fat and bean-fed '
  "horse beguile, // Neighing in likeness of a filly foal. // And sometime lurk I in a gossip's bowl // In very "
  'likeness of a roasted crab, // And, when she drinks, against her lips I bob // And on her withered dewlap pour the '
  'ale. // The wisest aunt, telling the saddest tale, // Sometime for three-foot stool mistaketh me; // Then slip I '
  'from her bum, down topples she // And "Tailor!" cries and falls into a cough, // And then the whole choir hold '
  'their hips and loffe // And waxen in their mirth and neeze and swear // A merrier hour was never wasted there.',
  'cca741940b95d808f3d833a49544f7601b394a74ee8c955f6d0ccd3cb843e10e',
  False,
  None),
 ('EDMUND: Thou, Nature, art my goddess. To thy law // My services are bound. Wherefore should I // Stand in the '
  'plague of custom, and permit // The curiosity of nations to deprive me // For that I am some twelve or fourteen '
  'moonshines // Lag of a brother? why "bastard"? Wherefore "base," // When my dimensions are as well compact, // My '
  'mind as generous and my shape as true // As honest madam\'s issue? Why brand they us // With "base," with '
  '"baseness," "bastardy," "base," // "base," // Who, in the lusty stealth of nature, take // More composition and '
  "fierce quality // Than doth within a dull, stale, tired bed // Go to th' creating a whole tribe of fops // Got "
  "'tween asleep and wake? Well then, // Legitimate Edgar, I must have your land. // Our father's love is to the "
  'bastard Edmund // As to th\' legitimate. Fine word, "legitimate." // Well, my legitimate, if this letter speed // '
  "And my invention thrive, Edmund the base // Shall top th' legitimate. I grow, I prosper. // Now, gods, stand up for "
  'bastards!',
  'c63d345e769f1a2e545579422f6cce07795441a7239736c8e43fc8abf1a7a376',
  False,
  None),
 ("MACBETH: If it were done when 'tis done, then 'twere well // It were done quickly. If th' assassination // Could "
  'trammel up the consequence and catch // With his surcease success, that but this blow // Might be the be-all and '
  "the end-all here, // But here, upon this bank and shoal of time, // We'd jump the life to come. But in these cases "
  '// We still have judgment here, that we but teach // Bloody instructions, which, being taught, return // To plague '
  "th' inventor. This even-handed justice // Commends th' ingredience of our poisoned chalice // To our own lips. He's "
  'here in double trust: // First, as I am his kinsman and his subject, // Strong both against the deed; then, as his '
  'host, // Who should against his murderer shut the door, // Not bear the knife myself. Besides, this Duncan // Hath '
  'borne his faculties so meek, hath been // So clear in his great office, that his virtues // Will plead like angels, '
  'trumpet-tongued, against // The deep damnation of his taking-off; // And pity, like a naked newborn babe // '
  "Striding the blast, or heaven's cherubin horsed // Upon the sightless couriers of the air, // Shall blow the horrid "
  'deed in every eye, // That tears shall drown the wind. I have no spur // To prick the sides of my intent, but only '
  "// Vaulting ambition, which o'erleaps itself // And falls on th' other-",
  'bb39ee04ee0e63af761dca088492391c3869d4a97edeb14545fd9e305dbb0631',
  False,
  None),
 ("JULIET: What's in a name? That which we call a rose // By any other word would smell as sweet. // So Romeo would, "
  'were he not Romeo called, // Retain that dear perfection which he owes // Without that title. Romeo, doff thy name, '
  '// And, for thy name, which is no part of thee, // Take all myself.',
  'ba389ec63c4263a18172d91f3cb0bc3ddf947895b60b6ac92f1cc871f3f4b750',
  False,
  None),
 ('MACBETH: Tomorrow and tomorrow and tomorrow // Creeps in this petty pace from day to day // To the last syllable of '
  'recorded time, // And all our yesterdays have lighted fools // The way to dusty death. Out, out, brief candle! // '
  "Life's but a walking shadow, a poor player // That struts and frets his hour upon the stage // And then is heard no "
  'more. It is a tale // Told by an idiot, full of sound and fury, // Signifying nothing.',
  '0ab38b98af58e2c9f34b7cf03e8ab3d96e9ae25e2d8f511de072cfa1f16981c1',
  False,
  None),
 ('IAGO: Thus do I ever make my fool my purse. // For I mine own gained knowledge should profane // If I would time '
  "expend with such a snipe // But for my sport and profit. I hate the Moor, // And it is thought abroad that 'twixt "
  "my sheets // 'Has done my office. I know not if 't be true, // But I, for mere suspicion in that kind, // Will do "
  "as if for surety. He holds me well. // The better shall my purpose work on him. // Cassio's a proper man. Let me "
  "see now: // To get his place and to plume up my will // In double knavery - How? how? - Let's see. // After some "
  "time, to abuse Othello's ear // That he is too familiar with his wife. // He hath a person and a smooth dispose // "
  'To be suspected, framed to make women false. // The Moor is of a free and open nature // That thinks men honest '
  "that but seem to be so, // And will as tenderly be led by th' nose // As asses are. // I have 't. It is engendered. "
  "Hell and night // Must bring this monstrous birth to the world's light.",
  'ea135445556430b6892ea226149a1e642b9018212cb5200dd4161c4fb21ad097',
  False,
  None),
 ('SHYLOCK: To bait fish withal; if it will feed nothing else, // it will feed my revenge. He hath disgraced me and // '
  'hindered me half a million, laughed at my losses, // mocked at my gains, scorned my nation, thwarted // my '
  "bargains, cooled my friends, heated mine enemies- // and what's his reason? I am a Jew. Hath not // a Jew eyes? "
  'Hath not a Jew hands, organs, dimensions, // senses, affections, passions? Fed with the // same food, hurt with the '
  'same weapons, subject to // the same diseases, healed by the same means, // warmed and cooled by the same winter '
  'and summer // as a Christian is? If you prick us, do we not // bleed? If you tickle us, do we not laugh? If you // '
  'poison us, do we not die? And if you wrong us, shall // we not revenge? If we are like you in the rest, we will // '
  'resemble you in that. If a Jew wrong a Christian, // what is his humility? Revenge. If a Christian wrong // a Jew, '
  'what should his sufferance be by Christian // example? Why, revenge! The villainy you teach me I // will execute, '
  'and it shall go hard but I will better the // instruction.',
  'aaeda42c1f7e6ee3fbc1b9857f8ecd70fcac784bdc0dfa95bf5b6ad842fba983',
  False,
  None),
 ("HAMLET: To be or not to be - that is the question: // Whether 'tis nobler in the mind to suffer // The slings and "
  'arrows of outrageous fortune, // Or to take arms against a sea of troubles // And, by opposing, end them. To die, '
  'to sleep - // No more - and by a sleep to say we end // The heartache and the thousand natural shocks // That flesh '
  "is heir to-'tis a consummation // Devoutly to be wished. To die, to sleep - // To sleep, perchance to dream. Ay, "
  "there's the rub, // For in that sleep of death what dreams may come, // When we have shuffled off this mortal coil, "
  "// Must give us pause. There's the respect // That makes calamity of so long life. // For who would bear the whips "
  "and scorns of time, // Th' oppressor's wrong, the proud man's contumely, // The pangs of despised love, the law's "
  "delay, // The insolence of office, and the spurns // That patient merit of th' unworthy takes, // When he himself "
  'might his quietus make // With a bare bodkin? Who would fardels bear, // To grunt and sweat under a weary life, // '
  'But that the dread of something after death, // The undiscovered country from whose bourn // No traveler returns, '
  'puzzles the will // And makes us rather bear those ills we have // Than fly to others that we know not of? // Thus '
  "conscience does make cowards of us all, // And thus the native hue of resolution // Is sicklied o'er with the pale "
  'cast of thought, // And enterprises of great pitch and moment // With this regard their currents turn awry // And '
  'lose the name of action. - Soft you now, // The fair Ophelia. - Nymph, in thy orisons // Be all my sins remembered.',
  'c07c332e14e7b0b31bc5ebd82f065cf54eaee6f179cdd56c9d04d21eaf599fcb',
  False,
  None),
 ('', '57240c46bf91521b608a8efa2e1ff4ea592d01ceefd18a6ffb5a3de9e779d0c4', False, None),
 ('!!! ??? --- ...', '57240c46bf91521b608a8efa2e1ff4ea592d01ceefd18a6ffb5a3de9e779d0c4', False, None),
 ("...Co-operate COOPERATE cooperate! 'Alpha' alpha ALPHA! Beta BETA? b-e-t-a",
  'fc39a3a00e5256b1b8ee754eaa4e800208ed700e611f9a913011c92356e9f754',
  False,
  None)]


@pytest.mark.parametrize("corpus,expected,is_visible,key_to_check", q8_testcases)
def test_q8(corpus, expected, is_visible, key_to_check):
    result = leading_letters(corpus)
    assert isinstance(result, dict)
    assert list(result) == [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    if is_visible:
        if key_to_check is None:
            assert result == expected
        else:
            assert result[key_to_check] == expected
    else:
        assert hashcode(result) == expected
