def right_justify(s):
    numLetters = len(s)
    spaces = 70 - numLetters
    print(' ' * spaces + s)

right_justify('My Name is my Name')
