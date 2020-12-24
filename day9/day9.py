'''
Advent of Code 2020 - Day 9
Encoding Error
'''

def readInput(file):
    with open(file) as f:
        return f.read().splitlines()


def parseXMAS(lines, lenPreamble):
    # Point to indices after the preamble (in other words, the next
    # number to validate)
    i = lenPreamble
    # Use to iterate over the preamble
    preambleStart = 0

    result = tuple()

    validNumber = True
    while i < len(lines) and validNumber:
        # Search for two numbers in the preamble that sum to the
        # target number. Discontinue loop if a pair is found
        target = int(lines[i])
        validSum = findSum(lines[preambleStart:i], target)
        
        if validSum == None:
            validNumber = False
            

        result = (validNumber, target)
        preambleStart += 1
        i += 1

    return result


def findSum(lines, target):
    pairFound = False
    result = None
    
    i = 0
    j = 1

    while i < len(lines) - 1 and not pairFound:
        while j < len(lines) and not pairFound:

            if int(lines[i]) + int(lines[j]) == target:
                pairFound = True
                result = (lines[i], lines[j])

            j += 1

        i += 1
        j = i + 1
        
    return result





if __name__ == '__main__':
    lines = readInput('input.txt')
    lenPreamble = 25

    # Puzzle 1
    result = parseXMAS(lines, lenPreamble)
    puzzle1Answer = result[1]

    # Puzzle 1 answer:
    print(f'Puzzle 1 answer: {puzzle1Answer}')

