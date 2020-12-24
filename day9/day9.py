'''
Advent of Code 2020 - Day 9
Encoding Error
'''
import collections

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

def findContiguousSum(lines, target):
    # Ref: https://docs.python.org/3/library/collections.html#collections.deque
    # Put first element in the deque
    contigDeque = collections.deque()
    contigDeque.append(lines[0])
    dequeSum = int(lines[0])
    found = False

    i = 1
    while i < len(lines) and not found:
        # Grow and shrink the deque as necessary
        if dequeSum < target:
            # Add next number in list to the deque
            contigDeque.append(lines[i])
            # Add next number to the sum of all numbers held by the deque
            dequeSum += int(lines[i])
            i += 1
        elif dequeSum > target:
            # Pop the furthest-left number out of the deque
            popped = int(contigDeque.popleft())
            # Subtract the popped amount from the deque sum
            dequeSum -= popped
        else:
            found = True

    return contigDeque



if __name__ == '__main__':
    inputFile = 'input.txt'
    #inputFile = 'shortInput.txt'
    lines = readInput(inputFile)

    lenPreamble = int()
    if inputFile == 'input.txt':
        lenPreamble = 25
    elif inputFile == 'shortInput.txt':
        lenPreamble = 5

    # Puzzle 1
    result = parseXMAS(lines, lenPreamble)
    puzzle1Answer = result[1]

    # Puzzle 1 answer:
    print(f'Puzzle 1 answer: {puzzle1Answer}')

    # Puzzle 2:
    contigDeque = findContiguousSum(lines, puzzle1Answer)
    # Each member of the contigDeque is stored as a string
    # Build a new list of integers from the contigDeque so they
    # may be sorted as integers and used in the final answer
    answerList = [int(x) for x in contigDeque]
    answerList.sort()
    puzzle2Answer = answerList[0] + answerList[len(answerList) - 1]

    # Puzzle 2 answer:
    print(f'Puzzle 2 answer: {puzzle2Answer}')

