'''
Day 3 - Advent of Code 2020
'''

def readInput(file):
    with open(file) as f:
        return f.read().split()

def traverse(lines, movesRight, movesDown):
    '''
    Returns the number of trees encountered on the given slope using
    the lines array as the field. Traverses the field from left to right,
    wrapping if necessary until the bottom of the field is reached.
    '''
    # Bottom row number
    bottom = len(lines)

    countTrees = 0
    i = 0
    j = 0

    while (i < bottom):
        # Increment tree counter if there is a tree in the path
        if lines[i][j] == '#':
            countTrees += 1

        # The puzzle states that the field/biome tree pattern repeats in the horizontal,
        # so wrap around using modulo
        j = (j + movesRight) % len(lines[i])
        i += movesDown
        
    return countTrees


if __name__ == '__main__':
    lines = readInput('input.txt')

    # Puzzle 1
    puzzle1TreeCount = traverse(lines, 3, 1)
    # Puzzle 1 answer
    print(f'Puzzle 1 Answer: {puzzle1TreeCount}')


    # Puzzle 2
    puzzle2Answer = traverse(lines, 1, 1)
    puzzle2Answer *= traverse(lines, 3, 1)
    puzzle2Answer *= traverse(lines, 5, 1)
    puzzle2Answer *= traverse(lines, 7, 1)
    puzzle2Answer *= traverse(lines, 1, 2)
    
    # Puzzle 2 answer
    print(f'Puzzle 2 Answer: {puzzle2Answer}')

