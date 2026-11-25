def find_file(folder, filename):
    if filename in folder['files']:
        return [folder['name'], filename]
    
    for subfolder in folder['subfolders']:
        result = find_file(subfolder, filename)
        if result:
            return [folder['name']] + result
            
    return []
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

    drive = {
        'name': 'HU Drive',
        'files': ['welcome.txt'],
        'subfolders': [
            {
                'name': 'Courses',
                'files': ['schedule.pdf'],
                'subfolders': [
                    {
                        'name': 'CS101',
                        'files': ['lab1.py', 'notes.pdf'],
                        'subfolders': []
                    },
                    {
                        'name': 'CS102',
                        'files': ['quiz.py'],
                        'subfolders': []
                    }
                ]
            },
            {
                'name': 'Events',
                'files': ['poster.png'],
                'subfolders': []
            }
        ]
    }

    print(find_file(drive, "lab1.py"))
    # Should print: ['HU Drive', 'Courses', 'CS101', 'lab1.py']

    print(find_file(drive, "schedule.pdf"))
    # Should print: ['HU Drive', 'Courses', 'schedule.pdf']

    print(find_file(drive, "welcome.txt"))
    # Should print: ['HU Drive', 'welcome.txt']

    print(find_file(drive, "poster.png"))
    # Should print: ['HU Drive', 'Events', 'poster.png']

    print(find_file(drive, "assignment.pdf"))
    # Should print: []

    print(find_file(drive["subfolders"][0], "quiz.py"))
    # Should print: ['Courses', 'CS102', 'quiz.py']

    print(find_file({"name": "Empty Folder", "files": [], "subfolders": []}, "notes.pdf"))
    # Should print: []

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q10.py
# python3 -m pytest tests/test_q10.py
