'''
Advent of Code 2020 Day 2 Solutions
'''

def readInData():
    '''
    Opens a text file containing input data, splitting on newline characters.
    Returns an array of string lines of input text
    '''
    with open('input.txt', 'r') as f:
        return f.read().split('\n')

def splitInputLine(line):
    '''
    Processes input string lines for use in password validation methods.
    If the line is empty, an empty dictionary is returned.
    If the line is not empty, a dictionary containing minCount, maxCount,
    reqLetter, and password is returned.
    '''
    tokens = {}
    if not line:
        return tokens

    # Split line into three tokens: min-max, letter, password
    splitLine = line.split()
    # Split min-max string further
    countStr = splitLine[0].split('-')
    tokens['minCount'] = int(countStr[0])
    tokens['maxCount'] = int(countStr[1])
    # The letter that must appear between minCount and maxCount times
    # in the password
    tokens['reqLetter'] = splitLine[1][0] # just grab char, ignore colon
    tokens['password'] = splitLine[2]

    return tokens


def validatePuzzle1Password(line):
    '''
    Returns password validity as a boolean. Puzzle 1 requires a password to have
    between tokens['minCount'] and tokens['maxCount'] occurences of tokens['reqLetter'].
    '''
    isValid = False
    # Don't process empty lines, immediately return False
    if not line:
        return isValid

    tokens = splitInputLine(line)

    # Ready to validate password
    # Count occurences of the required letter in the string password
    letterCount = 0
    for letter in tokens['password']:
        if letter == tokens['reqLetter']:
            letterCount += 1

    if tokens['minCount'] <= letterCount <= tokens['maxCount']:
        isValid = True

    return isValid


def validPuzzle2Password(line):
    '''
    Returns password validity as a boolean. Puzzle 2 requires a password to have
    the character tokens['reqLetter'] in the password string at index tokens['minCount'] - 1
    or tokens['maxCount'] - 1 but not both.
    '''
    isValid = False
    if not line:
        return isValid

    tokens = splitInputLine(line)

    loc1Matches = False
    loc2Matches = False
    # Indices decremented by 1 because problem indexes start at 1
    loc1Idx = int(tokens['minCount']) - 1
    loc2Idx = int(tokens['maxCount']) - 1
    letter = tokens['reqLetter']
    password = tokens['password']


    if password:
        if loc1Idx < len(password) and password[loc1Idx] == letter:
            loc1Matches = True
        if loc2Idx < len(password) and password[loc2Idx] == letter:
            loc2Matches = True
    
    # XOR
    if loc1Matches != loc2Matches:
        isValid = True

    return isValid

if __name__ == '__main__':
    lines = readInData()

    # Puzzle 1
    countValidPasswordsPuzzle1 = 0
    for line in lines:
        if validatePuzzle1Password(line):
            countValidPasswordsPuzzle1 += 1

    # Puzzle 1 answer
    print(f'Puzzle 1 Answer: {countValidPasswordsPuzzle1}')
        
    # Puzzle 2
    puzzle2PassCount = 0
    for line in lines:
        if validPuzzle2Password(line):
            puzzle2PassCount += 1

    # Puzzle 2 answer
    print(f'Puzzle 2 Answer: {puzzle2PassCount}')
    

