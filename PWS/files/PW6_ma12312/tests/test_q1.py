import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import mirror_message

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q1_testcases = [
    # Visible Testcases
    ('ABC', 'ZYX', True), 
    ('abc', 'zyx', True), 
    ('Habib', 'Szyry', True), 
    ('CS101!', 'XH101!', True), 
    
    # Hidden Testcases
    ('A', 'bbeebd879e1dff6918546dc0c179fdde505f2a21591c9a9c96e36b054ec5af83', False), 
    ('Z', '559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd', False),
    ('M', '8ce86a6ae65d3692e7305e2c58ac62eebd97d3d943e093f577da25c36988246b', False),
    ('m', '1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9', False),
    ('Az', '31b18bdf7a9ca945b76bacb2636b786af81cdc6fb226f9e6e804593e153eeddc', False),
    ('Hello World!', '5aabe7fce3db22ff9f74b0e765aadc488946f837c945d59e13466be1ce78d606', False),
    ('12345', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', False),
    ('a-b_c', '91c9b481426a73cdfb7abc333c4cb6c8a3b87a824f9ab142f2cfc50fb20a19d7', False),
    ('Python 3.14', '22d2c66d045933ff0f1d613dec4e3fcf627980d099eab0df543ac6f9c11714b5', False),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ada7786586ec886660f1c7d8cef91d5a8c71467da4dbb6c408c784d2a4189f97', False),
    ('abcdefghijklmnopqrstuvwxyz', '93ba56cccdc19890b8d31b4f0e9d81f3eff202ed3c130bd98b39fc160b6554ed', False),
    ('AaZz', '4a357649dafad27eb423460200117bd2bda9005d2cf4c44bc6a2a0973993b077', False),
    ('Campus@2026', '4373c9e1fa4c8511f01487bc8b3ce3cacc0dc09dd32ebeeff40b0f49bcd95b36', False),
    ('Mirror Message', '958a063165aae86f7fa6051477d56da3bc5ef1cddec67c8545687559c29e5728', False),
    ('!@#$%^&*()', '95ce789c5c9d18490972709838ca3a9719094bca3ac16332cfec0652b0236141', False),
    ('The Quick Brown Fox', '273d812cf18533238bab7e1c06136c85df9f31d9ce914c58a290198d6ae730ca', False)
]

@pytest.mark.parametrize("message, expected, visible", q1_testcases)
def test_q1(message, expected, visible):
    if visible:
        assert mirror_message(message) == expected
    else:
        assert hashcode(mirror_message(message)) == expected