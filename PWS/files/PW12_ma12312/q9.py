def count_reported_comments(comment):
    count = 0
    if comment['reported']:
        count += 1
    
    for reply in comment['replies']:
        count += count_reported_comments(reply)
        
    return count
    
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

    discussion = {
        'author': 'Ali',
        'reported': True,
        'replies': [
            {
                'author': 'Sara',
                'reported': False,
                'replies': [
                    {
                        'author': 'Bilal',
                        'reported': True,
                        'replies': []
                    }
                ]
            },
            {
                'author': 'Hania',
                'reported': True,
                'replies': []
            }
        ]
    }

    print(count_reported_comments(discussion))
    # Should print: 3

    print(count_reported_comments(discussion["replies"][0]))
    # Should print: 1

    print(count_reported_comments(discussion["replies"][1]))
    # Should print: 1

    print(count_reported_comments({"author": "Ahmed", "reported": False, "replies": []}))
    # Should print: 0

    print(count_reported_comments({"author": "Ayesha", "reported": True, "replies": []}))
    # Should print: 1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q9.py
# python3 -m pytest tests/test_q9.py
