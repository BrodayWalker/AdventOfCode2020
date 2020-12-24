'''
Advent of Code 2020 - Day 10
Adapter Array
'''


def readLines(file):
    intLines = []
    with open(file) as f:
        for line in f.read().splitlines():
            intLine = int(line)
            intLines.append(intLine)
    
    return intLines

def countDiffs(lines):
    '''
    Uses a counting sort to tally the distribution of jolt differences
    counts[0] is unused
    '''
    counts = [0, 0, 0, 0]
    counts[lines[0]] += 1
    # Handle special last case, which always results in a jolt difference of 3
    counts[3] += 1

    i = 1
    while i < len(lines):
        counts[lines[i] - lines[i - 1]] += 1

        i += 1

    return counts





if __name__ == '__main__':
    #inputFile = 'shortInput.txt'
    inputFile = 'input.txt'
    lines = readLines(inputFile)

    # Puzzle 1
    lines.sort()
    counts = countDiffs(lines)
    puzzle1Answer = counts[1] * counts[3]
    # Puzzle 1 answer
    print(f'Puzzle 1 answer: {puzzle1Answer}')
    