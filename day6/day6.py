'''
Advent of Code 2020 - Day 6
Custom Customs
'''


def readInput(file):
    with open(file) as f:
        return f.read().split('\n\n')

def makeCustomsSet(lines):
    '''
    Converts each list of answers into a set of answers
    Returns a list of all the sets
    '''
    customs = []

    for line in lines:
        questionSet = set()
        for entry in line:
            for answer in entry:
                questionSet.add(answer)
        customs.append(questionSet)

    return customs

def intersectSets(lines):
    '''
    Converts each string of answers into a set, intersecting each set to
    find the questions that all parties answered yes to (if there are any)
    '''
    customs = []

    for line in lines:
        intersecting = set()

        if line:
            for char in line[0]:
                intersecting.add(char)

        i = 1
        while i < len(line):
            lineSet = set()
            for char in line[i]:
                lineSet.add(char)
            intersecting = intersecting.intersection(lineSet)
            i += 1
        
        customs.append(intersecting)

    return customs

if __name__ == '__main__':
    inputLines = readInput('input.txt')

    lines = []
    for line in inputLines:
        splitLine = line.split()
        lines.append(splitLine)

    # Puzzle 1
    lineSet = makeCustomsSet(lines)
    sumAnswers = 0
    for line in lineSet:
        sumAnswers += len(line)

    # Puzzle 1 answer
    print(f'Puzzle 1 answer: {sumAnswers}')


    # Puzzle 2
    intersecting = intersectSets(lines)

    sumAnswers = 0
    for line in intersecting:
        sumAnswers += len(line)

    # Puzzle 2 answer
    print(f'Puzzle 2 answer: {sumAnswers}')
    
