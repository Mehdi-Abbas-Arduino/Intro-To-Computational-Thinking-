# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def remove_excluded_players(player_names):
    # WRITE YOUR CODE HERE
    names = []
    vowels = 'aeiou'
    hasvowel = False
    for player in player_names:
        hasvowel = False
        if player != '':
            if player.lower() != 'babarazam':
                for p in player:
                    if p.lower() in vowels:
                        hasvowel = True
                if hasvowel:
                    names.append(player)

    player_names[:] = names


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

    # Visible Test Case 1
    player_names = ['quddusi', 'MNT', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde', 'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo', 'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura', 'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta', 'abdullah', 'babarazam', 'hussainshah', 'sr4', 'kdb', 'askarizz', 'basim', 'raphina', 'usman', 'coldp@lm4r', '']
    print(remove_excluded_players(player_names))
    # Should print: None
    print(player_names)
    # Should print: ['quddusi', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde', 'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo', 'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura', 'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta', 'abdullah', 'hussainshah', 'askarizz', 'basim', 'raphina', 'usman', 'coldp@lm4r']

    print()

    # Visible Test Case 2
    player_names = ['amir', 'MNT', 'xyz', 'babarazam', 'otto', 'ali', 'saifibhai', 'hassan', 'evra', 'mrgreedy', 'mraura', 'etoo', 'alonso', 'messi', 'ronaldo', 'usman', 'abdullah', 'kdb', 'mbappe', 'quddusi', 'skibidiali', 'valverde', 'coldp@lm4r', '', 'askari', 'babarazam', 'faheem', 'leo', 'nash', 'tito', 'zio', 'O_o', 'u2u', 'EVE', 'ae', 'Ai']
    print(remove_excluded_players(player_names))
    # Should print: None
    print(player_names)
    # Should print: ['amir', 'otto', 'ali', 'saifibhai', 'hassan', 'evra', 'mrgreedy', 'mraura', 'etoo', 'alonso', 'messi', 'ronaldo', 'usman', 'abdullah', 'mbappe', 'quddusi', 'skibidiali', 'valverde', 'coldp@lm4r', 'askari', 'faheem', 'leo', 'nash', 'tito', 'zio', 'O_o', 'u2u', 'EVE', 'ae', 'Ai']

    print()

    # Visible Test Case 3
    player_names = ['ae', 'Ai', 'aoa', 'u2u', 'bcd', 'MNT', 'sr4', 'Xyz', 'EVE', 'eve', 'EVA', 'iZZi', 'usman', 'mufaddal', 'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira', 'apollo', 'babarazam', 'AAA', 'bbb', 'zzz', 'zzzZ', 'Ali', 'otto', 'iso', 'eko', 'e3e', 'O_o', 'babarazam', 'aeIOU', 'ae', 'ooo', 'uu', 'ii']
    print(remove_excluded_players(player_names))
    # Should print: None
    print(player_names)
    # Should print: ['ae', 'Ai', 'aoa', 'u2u', 'EVE', 'eve', 'EVA', 'iZZi', 'usman', 'mufaddal', 'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira', 'apollo', 'AAA', 'Ali', 'otto', 'iso', 'eko', 'e3e', 'O_o', 'aeIOU', 'ae', 'ooo', 'uu', 'ii']

    print()

    # Visible Test Case 4
    player_names = ['ronaldo', 'Messi', 'Mbappe', 'Neymar', 'Xavi', 'Iniesta', 'Lewandowski', 'benzema', 'messi', 'Haaland', 'KDB', 'babarazam', 'MNT', 'sr4', 'xyz', 'abc', 'amir', 'otto', 'ali', 'EVE', 'saif', 'usman', 'evra', 'hassan', 'mehmood', 'ramos', 'gavi', 'pedri', 'isco', 'rafa', 'mrgreedy', 'leo', 'tito', 'O_o', 'u2u', 'Ae', 'AAA', 'AE', 'EVE']
    print(remove_excluded_players(player_names))
    # Should print: None
    print(player_names)
    # Should print: ['ronaldo', 'Messi', 'Mbappe', 'Neymar', 'Xavi', 'Iniesta', 'Lewandowski', 'benzema', 'messi', 'Haaland', 'abc', 'amir', 'otto', 'ali', 'EVE', 'saif', 'usman', 'evra', 'hassan', 'mehmood', 'ramos', 'gavi', 'pedri', 'isco', 'rafa', 'mrgreedy', 'leo', 'tito', 'O_o', 'u2u', 'Ae', 'AAA', 'AE', 'EVE']

    print()

    # Visible Test Case 5
    player_names = ['AE', 'aeiou', 'eve', 'apollo', 'skibidiali', 'sky', 'hEllo', 'usman', 'faheem', 'meow', 'baqir', 'mraura', 'saifibhai', 'coldp@lm4r', 'iniesta', 'abdullah', 'ronaldo', 'alonso', 'etoo', 'valverde', 'messi', 'babarazam', 'kdb', 'MNT', 'xyz', 'zzz', 'zzzZ', 'A2A', 'EVE', 'otto', 'ae', 'uSU', 'O_o', 'Ai', 'Ali']
    print(remove_excluded_players(player_names))
    # Should print: None
    print(player_names)
    # Should print: ['AE', 'aeiou', 'eve', 'apollo', 'skibidiali', 'hEllo', 'usman', 'faheem', 'meow', 'baqir', 'mraura', 'saifibhai', 'coldp@lm4r', 'iniesta', 'abdullah', 'ronaldo', 'alonso', 'etoo', 'valverde', 'messi', 'A2A', 'EVE', 'otto', 'ae', 'uSU', 'O_o', 'Ai', 'Ali']

    print()

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py