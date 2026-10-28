# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def dostiyaariXI(player_names):
    # WRITE YOUR CODE HERE
    Cat = []
    catA = []
    catB = []
    catC = []
    vowels = ['a','e','i','o','u']
    for i in range(len(player_names)):
        if player_names[i][0].lower() in vowels and player_names[i][-1].lower() in vowels:
            catA.append(player_names[i])
    for j in range(len(player_names)):
        if player_names[j] not in catA:
            if player_names[j][0].lower() in vowels or player_names[j][-1].lower() in vowels:
            
                catB.append(player_names[j])

    for z in range(len(player_names)):
        if player_names[z] not in catA and player_names[z] not in catB:
            catC.append(player_names[z])

    catA.sort(key=str.lower)
    catB.sort(key=str.lower)
    catC.sort(key=str.lower)

    Cat.append(catA)
    Cat.append(catB)
    Cat.append(catC)

    return Cat 






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

    player_names = [
        'quddusi', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde',
        'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo',
        'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura',
        'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta',
        'abdullah', 'hussainshah', 'askarizz', 'basim', 'raphina',
        'usman', 'coldp@lm4r',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['alonso', 'etoo', 'evra', 'iniesta', 'isco'],
    #     ['abdullah', 'amir', 'askarizz', 'mbappe', 'messi',
    #      'mraura', 'quddusi', 'raphina', 'ronaldo', 'saifibhai',
    #      'skibidiali', 'usman', 'valverde'],
    #     ['CEmajorAT', 'baqir', 'basim', 'coldp@lm4r', 'hassan',
    #      'hussainshah', 'mrgreedy', 'mufaddal', 'swifthyderabad'],
    # ]

    player_names = [
        'Ava', 'Amir', 'Bilal', 'O',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['Ava', 'O'],
    #     ['Amir'],
    #     ['Bilal'],
    # ]

    player_names = []
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     [],
    #     [],
    #     [],
    # ]

    player_names = [
        'quddusi', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde',
        'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo',
        'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura',
        'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta',
        'abdullah', 'babarazam', 'hussainshah', 'askarizz', 'basim',
        'raphina', 'usman', 'coldp@lm4r',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['alonso', 'etoo', 'evra', 'iniesta', 'isco'],
    #     ['abdullah', 'amir', 'askarizz', 'mbappe', 'messi',
    #      'mraura', 'quddusi', 'raphina', 'ronaldo', 'saifibhai',
    #      'skibidiali', 'usman', 'valverde'],
    #     ['CEmajorAT', 'babarazam', 'baqir', 'basim', 'coldp@lm4r',
    #      'hassan', 'hussainshah', 'mrgreedy', 'mufaddal', 'swifthyderabad'],
    # ]

    player_names = [
        'amir', 'babarazam', 'otto', 'ali', 'saifibhai',
        'hassan', 'evra', 'mrgreedy', 'mraura', 'etoo',
        'alonso', 'messi', 'ronaldo', 'usman', 'abdullah',
        'mbappe', 'quddusi', 'skibidiali', 'valverde', 'coldp@lm4r',
        'askari', 'babarazam', 'faheem', 'leo', 'nash',
        'tito', 'zio', 'O_o', 'u2u', 'EVE',
        'ae', 'Ai',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['Ai', 'EVE', 'O_o', 'ae', 'ali',
    #      'alonso', 'askari', 'etoo', 'evra', 'otto',
    #      'u2u'],
    #     ['abdullah', 'amir', 'leo', 'mbappe', 'messi',
    #      'mraura', 'quddusi', 'ronaldo', 'saifibhai', 'skibidiali',
    #      'tito', 'usman', 'valverde', 'zio'],
    #     ['babarazam', 'babarazam', 'coldp@lm4r', 'faheem', 'hassan',
    #      'mrgreedy', 'nash'],
    # ]

    player_names = [
        'ae', 'Ai', 'aoa', 'u2u', 'EVE',
        'eve', 'EVA', 'iZZi', 'usman', 'mufaddal',
        'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira',
        'apollo', 'babarazam', 'AAA', 'Ali', 'otto',
        'iso', 'eko', 'e3e', 'O_o', 'babarazam',
        'aeIOU', 'ae', 'ooo', 'uu', 'ii',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['AAA', 'Ai', 'Ali', 'Amira', 'EVA',
    #      'EVE', 'O_o', 'ae', 'ae', 'aeIOU',
    #      'aoa', 'apollo', 'e3e', 'eko', 'eve',
    #      'iZZi', 'ii', 'iso', 'ooo', 'otto',
    #      'u2u', 'uu'],
    #     ['mraura', 'usman'],
    #     ['babarazam', 'babarazam', 'coldp@lm4r', 'faheem', 'mrgreedy',
    #      'mufaddal'],
    # ]

    player_names = [
        'ronaldo', 'Messi', 'Mbappe', 'Neymar', 'Xavi',
        'Iniesta', 'Lewandowski', 'benzema', 'messi', 'Haaland',
        'babarazam', 'abc', 'amir', 'otto', 'ali',
        'EVE', 'saif', 'usman', 'evra', 'hassan',
        'mehmood', 'ramos', 'gavi', 'pedri', 'isco',
        'rafa', 'mrgreedy', 'leo', 'tito', 'O_o',
        'u2u', 'Ae', 'AAA', 'AE', 'EVE',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['AAA', 'AE', 'Ae', 'EVE', 'EVE',
    #      'Iniesta', 'O_o', 'ali', 'evra', 'isco',
    #      'otto', 'u2u'],
    #     ['Lewandowski', 'Mbappe', 'Messi', 'Xavi', 'abc',
    #      'amir', 'benzema', 'gavi', 'leo', 'messi',
    #      'pedri', 'rafa', 'ronaldo', 'tito', 'usman'],
    #     ['Haaland', 'Neymar', 'babarazam', 'hassan', 'mehmood',
    #      'mrgreedy', 'ramos', 'saif'],
    # ]

    player_names = [
        'AE', 'aeiou', 'eve', 'apollo', 'skibidiali',
        'hEllo', 'usman', 'faheem', 'meow', 'baqir',
        'mraura', 'saifibhai', 'coldp@lm4r', 'iniesta', 'abdullah',
        'ronaldo', 'alonso', 'etoo', 'valverde', 'messi',
        'babarazam', 'A2A', 'EVE', 'otto', 'ae',
        'uSU', 'O_o', 'Ai', 'Ali',
    ]
    print(dostiyaariXI(player_names))
    # Should print:
    # [
    #     ['A2A', 'AE', 'Ai', 'Ali', 'EVE',
    #      'O_o', 'ae', 'aeiou', 'alonso', 'apollo',
    #      'etoo', 'eve', 'iniesta', 'otto', 'uSU'],
    #     ['abdullah', 'hEllo', 'messi', 'mraura', 'ronaldo',
    #      'saifibhai', 'skibidiali', 'usman', 'valverde'],
    #     ['babarazam', 'baqir', 'coldp@lm4r', 'faheem', 'meow'],
    # ]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py