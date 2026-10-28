import hashlib
import os
import sys
from copy import deepcopy

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from q4 import special_list_sort


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q4_testcases = [
    ([
        ['Sarwan', 'EE', 2021], ['Ayesha Khan', 'CND', 2021], ['Hamza Junaid', 'EE', 2021], ['Ahsan Qadeer', 'CS', 2020], 
        ['Muhammad Ali Bhutto', 'EE', 2020], ['Marium Habiby', 'SDP', 2021], ['Adil Ali Khan', 'EE', 2021]
     ],
     [
         ['Ahsan Qadeer', 'CS', 2020], ['Muhammad Ali Bhutto', 'EE', 2020], ['Ayesha Khan', 'CND', 2021], ['Adil Ali Khan', 'EE', 2021],
         ['Hamza Junaid', 'EE', 2021], ['Sarwan', 'EE', 2021], ['Marium Habiby', 'SDP', 2021]
     ], True),

    ([
        ['Sarwan', 'EE', 2021], ['Lulowalokand Wala', 'CND', 2021], ['Hamza Junaid', 'EE', 2021], ['Ahsan Qadeer', 'CS', 2020],
        ['Muhammad Ali Bhutto', 'EE', 2020], ['Marium Habiby', 'SDP', 2021], ['Adil Ali Khan', 'EE', 2021]
     ],
     [
        ['Ahsan Qadeer', 'CS', 2020], ['Muhammad Ali Bhutto', 'EE', 2020], ['Lulowalokand Wala', 'CND', 2021], 
        ['Adil Ali Khan', 'EE', 2021], ['Hamza Junaid', 'EE', 2021], ['Sarwan', 'EE', 2021], ['Marium Habiby', 'SDP', 2021]
     ], True),

    ([
        ['Aazan Ijlal', 'CS', 2021], ['Adina Zuberi', 'SNP', 2020], ['Ahmed Sultan', 'EE', 2021], 
        ['Basim Haqqui', 'CND', 2022], ['Syed Pasha', 'EE', 2020], ['Darab Moazzam', 'CS', 2021],
        ['Eesha Sadiq', 'CND', 2022], ['Eman Imam', 'CND', 2020], ['Huzaifa Ahmed', 'EE', 2022],
        ['Maham Jawed', 'EE', 2020], ['Manaal Fatima', 'CND', 2021], ['Mir Akbar', 'CS', 2020], 
        ['Muhammad Ali', 'CS', 2020], ['Munsif Rehman', 'CS', 2022], ['Pashmeenay Shahzad', 'SNP', 2021],
        ['Sania Zehra', 'SNP', 2020], ['Sarah Mandviwala', 'CS', 2020], ['Sheryar Ur Rehman', 'EE', 2021],
        ['Tara Vera Ahmed', 'CND', 2022], ['Usman Abdullah', 'CND', 2022]
     ],
     [
        ['Eman Imam', 'CND', 2020], ['Mir Akbar', 'CS', 2020], ['Muhammad Ali', 'CS', 2020],
        ['Sarah Mandviwala', 'CS', 2020], ['Maham Jawed', 'EE', 2020], ['Syed Pasha', 'EE', 2020],
        ['Adina Zuberi', 'SNP', 2020], ['Sania Zehra', 'SNP', 2020], ['Manaal Fatima', 'CND', 2021],
        ['Aazan Ijlal', 'CS', 2021], ['Darab Moazzam', 'CS', 2021], ['Ahmed Sultan', 'EE', 2021],
        ['Sheryar Ur Rehman', 'EE', 2021], ['Pashmeenay Shahzad', 'SNP', 2021], ['Basim Haqqui', 'CND', 2022],
        ['Eesha Sadiq', 'CND', 2022], ['Tara Vera Ahmed', 'CND', 2022], ['Usman Abdullah', 'CND', 2022],
        ['Munsif Rehman', 'CS', 2022], ['Huzaifa Ahmed', 'EE', 2022]
     ], True),

    ([], [], True),

    ([
        ['Aazan Ijlal', 'CS', 2021], ['Muhammad Ali', 'CS', 2020], ['Munsif Rehman', 'CS', 2022],
        ['Basim Haqqui', 'CND', 2022], ['Huzaifa Ahmed', 'EE', 2022], ['Mir Akbar', 'CS', 2020],
        ['Usman Abdullah', 'CND', 2022], ['Darab Moazzam', 'CS', 2021], ['Sheryar Ur Rehman', 'EE', 2021],
        ['Maham Jawed', 'EE', 2020], ['Ahmed Sultan', 'EE', 2021], ['Sarah Mandviwala', 'CS', 2020],
        ['Tara Vera Ahmed', 'CND', 2022], ['Eman Imam', 'CND', 2020], ['Syed Pasha', 'EE', 2020],
        ['Sania Zehra', 'SNP', 2020], ['Eesha Sadiq', 'CND', 2022], ['Pashmeenay Shahzad', 'SNP', 2021],
        ['Manaal Fatima', 'CND', 2021], ['Adina Zuberi', 'SNP', 2020]
     ], '534047715adffe6ddc967bfc2262bde99a5028c1701caa8d5a2f4f2bb806842b', False),

    ([['Zara Abbas', 'CS', 2024]], '569a0a6bf6d8826af8ad4918d988e9fe0dca413851d748e9198135a2bab0487c', False),

    ([
        ['Zoya Khan', 'CS', 2023], ['Ayesha Abbas', 'CS', 2023],
        ['Hamza Ali', 'CS', 2023], ['Bilal Hussain', 'CS', 2023]
     ], 'bb21ae30760e0d862ac69a7b77f3a220bf0a0951a480ec1ecb9c20b346c09491', False),

    ([
        ['Ayesha Ali', 'EE', 2022], ['Zara Khan', 'CS', 2022],
        ['Bilal Raza', 'BBA', 2022], ['Mariam Noor', 'CND', 2022]
     ], 'c51b5c28234cd2ca44fa20d7d893530a89637632d56234dafb29e376081addd5', False),

    ([
        ['Ayesha Hassan', 'BBA', 2025], ['Zara Ahmed', 'SE', 2019],
        ['Bilal Ali', 'CS', 2024], ['Hamza Khan', 'EE', 2020]
     ], '7c3a4391e16a79cdb3fd1a16f036019f03a308227ce1ca81e869696b163696b4', False),

    ([
        ['Sana Malik', 'CS', 2022], ['Sana Malik', 'CS', 2022],
        ['Bilal Abbas', 'CS', 2022], ['Sana Malik', 'CS', 2021]
     ], '1e36e9e1c7ef2f82f67de6aacc4df0eef8a118e8f9d8ad7cb2888a53d4d2a1f6', False),

    ([
        ['Ayesha Abbas', 'CND', 2020], ['Bilal Khan', 'CS', 2020],
        ['Amir Ali', 'CS', 2021], ['Zoya Ali', 'EE', 2021]
     ], '1b3a8669eff6eb1b1ce4e75feb950863a847fc2b3e819df02a2b9d97f790fcd1', False),

    ([
        ['Zoya Babar', 'SE', 2026], ['Zohaib Khan', 'EE', 2025],
        ['Bilal Noor', 'CS', 2024], ['Ayesha Ali', 'BBA', 2023]
     ], 'b8b6d4d425e43f68c9be08c225362232da13f359e2d23ed1d3174323c7a071d9', False),

    ([
      ['Bilal Khan', 'CS', 2020], ['Bilal Khan', 'EE', 2020],
      ['Bilal Khan', 'CS', 2022], ['Bilal Khan', 'CS', 2021]
     ], '06a7c0555ffb129dcc4d4afe4f8e14f7b63338b3d1e854bb6e3c567493259642', False),

    ([
        ['Muhammad Adeel Ahmed', 'EE', 2099], ['Ayesha Noor Khan', 'CS', 1900],
        ['Sara Fatima Ali', 'CND', 1999], ['Ali Hassan Raza', 'BBA', 2000]
     ], '14bcae68005e185c7819b19f4a0a72711778b54f8bae9543e733764ccb65b2e7', False),

    ([
        ['Ayesha Noor', 'EE', 2018], ['Ayesha Noor', 'EE', 2024], ['Zohaib Raza', 'SE', 2021], 
        ['Nimra Khan', 'CND', 2019], ['Zohaib Raza', 'SE', 2024], ['Sadia Ahmed', 'BBA', 2020],
        ['Nimra Khan', 'CND', 2022], ['Hamza Ali', 'CS', 2022], ['Ayesha Noor', 'EE', 2021],
        ['Hamza Ali', 'CS', 2023], ['Ayesha Noor', 'EE', 2022], ['Hamza Ali', 'CS', 2021],
        ['Hamza Ali', 'CS', 2024], ['Zohaib Raza', 'SE', 2020], ['Zohaib Raza', 'SE', 2018], 
        ['Ayesha Noor', 'EE', 2019], ['Nimra Khan', 'CND', 2018], ['Sadia Ahmed', 'BBA', 2019],
        ['Sadia Ahmed', 'BBA', 2022], ['Hamza Ali', 'CS', 2020], ['Nimra Khan', 'CND', 2023],
        ['Ayesha Noor', 'EE', 2023], ['Sadia Ahmed', 'BBA', 2018], ['Hamza Ali', 'CS', 2019],
        ['Zohaib Raza', 'SE', 2022], ['Nimra Khan', 'CND', 2024], ['Sadia Ahmed', 'BBA', 2021],
        ['Ayesha Noor', 'EE', 2020], ['Nimra Khan', 'CND', 2021], ['Hamza Ali', 'CS', 2018],
        ['Zohaib Raza', 'SE', 2023], ['Sadia Ahmed', 'BBA', 2023], ['Sadia Ahmed', 'BBA', 2024],
        ['Zohaib Raza', 'SE', 2019], ['Nimra Khan', 'CND', 2020]
     ], '8b15cdcdda3bc32961afcaef303441f8b7b752e8b0ccf5490ad80aee50d4a9a7', False),
]


@pytest.mark.parametrize("student_records, expected, visible", q4_testcases)
def test_q4(student_records, expected, visible):
    original_records = deepcopy(student_records)
    result = special_list_sort(student_records)
    assert student_records == original_records, "The original student_records list must not be modified."
    assert isinstance(result, list), "The function must return a list."
    assert result is not student_records, "Return a new list, not the original student_records list."
    if visible:
        assert result == expected, f"{result!r} != {expected!r}"
    else:
        assert hashcode(result) == expected, "Incorrect sort order or records in this hidden test case."
