'''
Advent of Code 2020 - Day 7
Handy Haversacks
'''
import re

def readInput(file):
    with open(file) as f:
        lines = f.read().split('\n')
        # Remove empty last line
        lines.pop()
        return lines

def parseLines(lines):
    '''
    Parses the input lines returning a list of lists of parsed rules
    List format: [string bag color description, 1 or more tuples (int number of bags, string bag color description)]

    Example:
        Original: drab purple bags contain 4 muted cyan bags, 3 wavy lavender bags, 2 dotted blue bags.
        Parsed: ['drab purple', ('4', 'muted cyan'), ('3', 'wavy lavender'), ('2', 'dotted blue')]
    '''
    parsedLines = []

    for line in lines:
        # Replace 'bags contain', 'bags', 'bag', ',', and '.' with # for easy
        # splitting
        sepLine = re.sub(r'( bags\s{1}contain\s{1})|bags?|[,.]', '#', line)
        stripLine = sepLine.split('#')

        # Create the 
        lineX = []

        if stripLine:
            lineX.append(stripLine[0].strip())

        for field in stripLine[1:]:
            # Handle special case where there isn't a number then a two-word 
            # bag color description
            if field == 'no other':
                lineX.append((0, field))
            # Skip empty lines
            elif field != '':
                # Strip leading and trailing whitespace
                info = field.strip()
                # Split the number of bags from the bag color description
                info = info.split(' ', 1)
                # Strip whitespace off number and append (number of bags, bag color description)
                # tuple to the line
                #lineX.append((info[0].strip(), info[1]))
                lineX.append((info[0], info[1]))

        parsedLines.append(lineX)

    return parsedLines





if __name__ == '__main__':
    lines = readInput('input.txt')

    parsedLines = parseLines(lines)

    # Temporary parsing logic check
    i = 0
    for line in parsedLines:
        print(i, end=' ')
        print(line)

        i += 1