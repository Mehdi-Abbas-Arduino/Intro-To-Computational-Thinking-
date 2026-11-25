def remove_user(user_profiles, username):
    if username not in user_profiles:
        return user_profiles

    del user_profiles[username]

    for values in user_profiles.values():
        following = values[1]

        if username in following:
            following.remove(username)

    return user_profiles

# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":
    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually compare the output #
    # with the expected output below.                #
    # ----------------------------------------------#

    user_profiles = {'Alice': ['123-456-7890', ['Bob', 'Charlie']],
     'Bob': ['987-654-3210', ['Alice', 'David']],
     'Charlie': ['111-222-3333', ['Alice']],
     'David': ['555-666-7777', ['Bob']]}
    print(remove_user(user_profiles, 'Alice'))
    # Should print:
    # {'Bob': ['987-654-3210', ['David']],
    #  'Charlie': ['111-222-3333', []],
    #  'David': ['555-666-7777', ['Bob']]}

    user_profiles = {'Alice': ['123-456-7890', []],
     'Bob': ['987-654-3210', ['Alice']],
     'Charlie': ['111-222-3333', ['Alice']],
     'David': ['555-666-7777', ['Bob']]}
    print(remove_user(user_profiles, 'Alice'))
    # Should print:
    # {'Bob': ['987-654-3210', []],
    #  'Charlie': ['111-222-3333', []],
    #  'David': ['555-666-7777', ['Bob']]}

    user_profiles = {'Alice': ['111', []], 'Bob': ['222', ['Alice']]}
    print(remove_user(user_profiles, 'Alice'))
    # Should print: {'Bob': ['222', []]}

    print(remove_user(user_profiles, 'Eve'))
    # Should print: {'Bob': ['222', []]}

    print(remove_user({}, 'Eve'))
    # Should print: {}

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
