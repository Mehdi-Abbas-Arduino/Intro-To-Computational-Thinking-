# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#
import pprint

def are_anagrams(first_phrase, second_phrase):
    # WRITE YOUR CODE HERE
    dictionary = {}
    dict2 = {}
    first_phrase = first_phrase.lower()
    second_phrase = second_phrase.lower()

    lst =[]
    lst2 = []

    # var = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(first_phrase)):
        if first_phrase[i].isalpha():
            lst.append(first_phrase[i])
    for j in range(len(second_phrase)):
        if second_phrase[j].isalpha():
            lst2.append(second_phrase[j])

    lst.sort()
    lst2.sort()
    
    for i in lst:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    for j in lst2:
        if j not in dict2:
            dict2[j] = 1
        else:
            dict2[j] += 1

    pprint.pprint(dictionary)
    pprint.pprint(dict2)

    if dict2 == dictionary:
        print("Anagrams")
    else:
        print("Not anagrams")


    # Sample code for printing dictionaries with the pprint module:
    # import pprint
    # dict_p = {}
    # Populate the dictionary...
    # pprint.pprint(dict_p)


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#
    are_anagrams('Stressed?', 'Desserts!!!!')
    # Should print:
    # {'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}
    # {'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}
    # Anagrams
    print()

    are_anagrams('Stressed?', 'Dessert.')
    # Should print:
    # {'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}
    # {'d': 1, 'e': 2, 'r': 1, 's': 2, 't': 1}
    # Not anagrams
    print()

    are_anagrams('Snooze alarms.', "Alas! No more Z's. =(")
    # Should print:
    # {'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}
    # {'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}
    # Anagrams
    print()

    are_anagrams('Snooze alarm.', "Alas! No more Z's. =(")
    # Should print:
    # {'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 1, 'z': 1}
    # {'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}
    # Not anagrams
    print()

    are_anagrams('The eye...', '... it sees!')
    # Should print:
    # {'e': 3, 'h': 1, 't': 1, 'y': 1}
    # {'e': 2, 'i': 1, 's': 2, 't': 1}
    # Not anagrams
    print()

    are_anagrams('123!', '...')
    # Should print:
    # {}
    # {}
    # Anagrams

    # ----------------------------------------------#
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW       #
    # ----------------------------------------------#

    # In order to test your function, run:
    # pytest tests/test_q4.py
