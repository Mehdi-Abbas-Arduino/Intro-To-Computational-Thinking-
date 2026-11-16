# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def contacts():
    # WRITE YOUR CODE HERE
    dict = {}
    name = input()
    while name != 'STOP':
        name, phone = name.split(", ")
        if name not in dict:
            dict[name] = [phone]
        else:
            if phone not in dict[name]:
                dict[name].append(phone)
        name = input()

    for i in dict:
        dict[i].sort()
    return dict


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":
    import pprint

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#
    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # Chandi, 0300-555-2224
    # Chacha Karmoo, 0300-333-7777
    # Chandi, 0300-555-2222
    # Chandi, 0300-555-2224
    # Sona, 0300-555-2222
    # STOP
    # Should print:
    # {'Chacha Karmoo': ['0300-333-7777'],
    #  'Chandi': ['0300-555-2222', '0300-555-2224'],
    #  'Sona': ['0300-555-2222']}

    print()

    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # STOP
    # Should print:
    # {}

    print()

    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # Sona, 0300-555-1111
    # Chandi, 0300-555-2222
    # Chacha Karmoo, 0300-333-7777
    # Maasi Barkatay, 0300-222-9999
    # Nawab Farasat Ali Khan, 0388-888-8888
    # STOP
    # Should print:
    # {'Chacha Karmoo': ['0300-333-7777'],
    #  'Chandi': ['0300-555-2222'],
    #  'Maasi Barkatay': ['0300-222-9999'],
    #  'Nawab Farasat Ali Khan': ['0388-888-8888'],
    #  'Sona': ['0300-555-1111']}

    print()

    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # Sona, 0300-555-1111
    # Sona, 0300-555-1112
    # Chandi, 0300-555-2222
    # Chandi, 0300-555-2223
    # Chandi, 0300-555-2224
    # Chacha Karmoo, 0300-333-7777
    # Chacha Karmoo, 0300-333-7778
    # Maasi Barkatay, 0300-222-9999
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-888-8889
    # Nawab Farasat Ali Khan, 0388-888-8898
    # Nawab Farasat Ali Khan, 0388-888-8899
    # Nawab Farasat Ali Khan, 0388-889-8888
    # Nawab Farasat Ali Khan, 0388-889-8889
    # STOP
    # Should print:
    # {'Chacha Karmoo': ['0300-333-7777', '0300-333-7778'],
    #  'Chandi': ['0300-555-2222', '0300-555-2223', '0300-555-2224'],
    #  'Maasi Barkatay': ['0300-222-9999'],
    #  'Nawab Farasat Ali Khan': ['0388-888-8888',
    #                             '0388-888-8889',
    #                             '0388-888-8898',
    #                             '0388-888-8899',
    #                             '0388-889-8888',
    #                             '0388-889-8889'],
    #  'Sona': ['0300-555-1111', '0300-555-1112']}

    print()

    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # Sona, 0300-555-1112
    # Chandi, 0300-555-2224
    # Chandi, 0300-555-2222
    # Chandi, 0300-555-2223
    # Sona, 0300-555-1111
    # STOP
    # Should print:
    # {'Chandi': ['0300-555-2222', '0300-555-2223', '0300-555-2224'],
    #  'Sona': ['0300-555-1111', '0300-555-1112']}

    print()

    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # Sona, 0300-555-1111
    # Sona, 0300-555-1111
    # Chandi, 0300-555-2222
    # Chandi, 0300-555-2222
    # Chandi, 0300-555-2222
    # Chacha Karmoo, 0300-333-7777
    # Chacha Karmoo, 0300-333-7777
    # Maasi Barkatay, 0300-222-9999
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-888-8888
    # STOP
    # Should print:
    # {'Chacha Karmoo': ['0300-333-7777'],
    #  'Chandi': ['0300-555-2222'],
    #  'Maasi Barkatay': ['0300-222-9999'],
    #  'Nawab Farasat Ali Khan': ['0388-888-8888'],
    #  'Sona': ['0300-555-1111']}

    print()

    pprint.pprint(contacts())
    # Enter these lines when prompted:
    # Chacha Karmoo, 0300-333-7778
    # Chandi, 0300-555-2223
    # Nawab Farasat Ali Khan, 0388-888-8898
    # Nawab Farasat Ali Khan, 0388-888-8899
    # Chandi, 0300-555-2224
    # Sona, 0300-555-1111
    # Chacha Karmoo, 0300-333-7778
    # Chandi, 0300-555-2224
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Chandi, 0300-555-2222
    # Nawab Farasat Ali Khan, 0388-889-8889
    # Sona, 0300-555-1112
    # Chacha Karmoo, 0300-333-7777
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Nawab Farasat Ali Khan, 0388-889-8888
    # Chandi, 0300-555-2222
    # Chandi, 0300-555-2222
    # Nawab Farasat Ali Khan, 0388-888-8889
    # Nawab Farasat Ali Khan, 0388-888-8888
    # Chacha Karmoo, 0300-333-7778
    # Maasi Barkatay, 0300-222-9999
    # Maasi Barkatay, 0300-222-9999
    # STOP
    # Should print:
    # {'Chacha Karmoo': ['0300-333-7777', '0300-333-7778'],
    #  'Chandi': ['0300-555-2222', '0300-555-2223', '0300-555-2224'],
    #  'Maasi Barkatay': ['0300-222-9999'],
    #  'Nawab Farasat Ali Khan': ['0388-888-8888',
    #                             '0388-888-8889',
    #                             '0388-888-8898',
    #                             '0388-888-8899',
    #                             '0388-889-8888',
    #                             '0388-889-8889'],
    #  'Sona': ['0300-555-1111', '0300-555-1112']}

    # ----------------------------------------------#
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW       #
    # ----------------------------------------------#

    # In order to test your function, run:
    # pytest tests/test_q5.py
