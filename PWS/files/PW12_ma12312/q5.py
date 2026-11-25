def update_lughat(lughat, paragraph_id, word, frequency_to_add):
    name = word[0]

    if name not in lughat:
        lughat[name] = {}

    if paragraph_id not in lughat[name]:
        lughat[name][paragraph_id] = []

    v = lughat[name][paragraph_id]

    for i in range(len(v)):
        if v[i][0] == word:
            v[i][1] += frequency_to_add
            return

    for i in range(len(v)):
        if word < v[i][0]:
            v.insert(i, [word, frequency_to_add])
            return

    v.append([word, frequency_to_add])


    


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":
    import pprint

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually compare the output #
    # with the expected output below.                #
    # ----------------------------------------------#

    lughat = {'a': {'p1': [['and', 2], ['as', 1]], 'p2': [['a', 1]]},
     'b': {'p1': [['but', 1], ['by', 1]]},
     'c': {'p1': [['code', 2]]}}

    update_lughat(lughat, 'p1', 'and', 3)
    pprint.pprint(lughat)
    # Should print:
    # {'a': {'p1': [['and', 5], ['as', 1]], 'p2': [['a', 1]]},
    #  'b': {'p1': [['but', 1], ['by', 1]]},
    #  'c': {'p1': [['code', 2]]}}
    print()

    update_lughat(lughat, 'p2', 'also', 1)
    pprint.pprint(lughat)
    # Should print:
    # {'a': {'p1': [['and', 5], ['as', 1]], 'p2': [['a', 1], ['also', 1]]},
    #  'b': {'p1': [['but', 1], ['by', 1]]},
    #  'c': {'p1': [['code', 2]]}}
    print()

    update_lughat(lughat, 'p2', 'because', 2)
    pprint.pprint(lughat)
    # Should print:
    # {'a': {'p1': [['and', 5], ['as', 1]], 'p2': [['a', 1], ['also', 1]]},
    #  'b': {'p1': [['but', 1], ['by', 1]], 'p2': [['because', 2]]},
    #  'c': {'p1': [['code', 2]]}}
    print()

    update_lughat(lughat, 'p3', 'code', 1)
    pprint.pprint(lughat)
    # Should print:
    # {'a': {'p1': [['and', 5], ['as', 1]], 'p2': [['a', 1], ['also', 1]]},
    #  'b': {'p1': [['but', 1], ['by', 1]], 'p2': [['because', 2]]},
    #  'c': {'p1': [['code', 2]], 'p3': [['code', 1]]}}
    print()

    update_lughat(lughat, 'p1', 'data', 2)
    pprint.pprint(lughat)
    # Should print:
    # {'a': {'p1': [['and', 5], ['as', 1]], 'p2': [['a', 1], ['also', 1]]},
    #  'b': {'p1': [['but', 1], ['by', 1]], 'p2': [['because', 2]]},
    #  'c': {'p1': [['code', 2]], 'p3': [['code', 1]]},
    #  'd': {'p1': [['data', 2]]}}
    print()

    print(update_lughat(lughat, 'p1', 'and', 1) is None)
    # Should print: True
    print(lughat['a']['p1'])
    # Should print: [['and', 6], ['as', 1]]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py
