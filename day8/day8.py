'''
Advent of Code 2020 - Day 8
Handheld Halting
'''

def readInput(file):
    '''
    Returns a list of lines, where each line is as a tuple of (instruction, signed integer)
    '''
    with open(file) as f:
        lines = f.read().splitlines()

        sepLines = []
        for line in lines:
            lineTuple = line.split(' ')
            sepLines.append((lineTuple[0], lineTuple[1]))

        return sepLines

def run(lines):
    lastState = dict()
    # A set of instructions run
    idxSet = set()

    accumulator = 0
    i = 0
    while i not in idxSet:
        idxSet.add(i)
        
        instruction = lines[i][0]
        signedInt = lines[i][1]

        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            accumulator += int(signedInt)
            i += 1
        elif instruction == 'jmp':
            i += int(signedInt)
        
        # Halt upon encountering an instruction that has already
        # been executed
        if i not in idxSet:
            lastState['acc'] = accumulator
            lastState['op'] = instruction
            lastState['instPointer'] = i

    return lastState


def runSubInst(lines):
    '''
    Runs the program, substituting one jmp or nop until the program
    is able to complete. 
    '''
    lastState = dict()
    
    # A list of all locations of jmp and nop instructions
    # to be used for substituting instructions
    jmpLocs, nopLocs = findJmpsAndNops(lines)
    
    completeRun = False
    nopPtr = 0
    # First try substituting a nop with a jmp
    while nopPtr < len(nopLocs) and not completeRun:
        accumulator = 0
        i = 0
        # A set of instructions run
        idxSet = set()
        while i not in idxSet and not completeRun:
            idxSet.add(i)
            
            if i == nopLocs[nopPtr]:
                instruction = 'jmp'
            else:
                instruction = lines[i][0]
            signedInt = lines[i][1]

            if instruction == 'nop':
                i += 1
            elif instruction == 'acc':
                accumulator += int(signedInt)
                i += 1
            elif instruction == 'jmp':
                i += int(signedInt)
            
            # Halt upon encountering an instruction that has already
            # been executed or the instruction pointer is pointig to 
            # an out of bounds memory location (successful program completion)
            if i not in idxSet or i == len(lines):
                lastState['acc'] = accumulator
                lastState['op'] = instruction
                lastState['instPointer'] = i

                if i == len(lines):
                    completeRun = True

        nopPtr += 1

    jmpPtr = 0
    # If substituting nops didn't work, try subbing jmps with nops
    while jmpPtr < len(jmpLocs) and not completeRun:
        accumulator = 0
        i = 0
        # A set of instructions run
        idxSet = set()
        while i not in idxSet and not completeRun:
            idxSet.add(i)
            
            if i == jmpLocs[jmpPtr]:
                instruction = 'nop'
            else:
                instruction = lines[i][0]
            signedInt = lines[i][1]

            if instruction == 'nop':
                i += 1
            elif instruction == 'acc':
                accumulator += int(signedInt)
                i += 1
            elif instruction == 'jmp':
                i += int(signedInt)
            
            # Halt upon encountering an instruction that has already
            # been executed or the instruction pointer is pointig to 
            # an out of bounds memory location (successful program completion)
            if i not in idxSet or i == len(lines):
                lastState['acc'] = accumulator
                lastState['op'] = instruction
                lastState['instPointer'] = i

                if i == len(lines):
                    completeRun = True

        jmpPtr += 1

    return lastState

def findJmpsAndNops(lines):
    '''
    Finds each jmp and nop location and adds them to their respective list.
    Returns two separate lists: a list of jmp instruction locations and a
    list of nop instuction locations
    '''
    jmps = []
    nops = []

    i = 0
    for line in lines:
        if line[0] == 'jmp':
            jmps.append(i)
        elif line[0] == 'nop':
            nops.append(i)

        i += 1
    
    return jmps, nops


if __name__ == '__main__':
    lines = readInput('input.txt')

    # Puzzle 1
    lastState = run(lines)
    puzzle1Answer = lastState['acc']

    # Puzzle 1 answer
    print(f'Puzzle 1 answer: {puzzle1Answer}')

    # Puzzle 2
    lastState = runSubInst(lines)
    puzzle2Answer = lastState['acc']

    # Puzzle 2 answer
    print(f'Puzzle 2 answer: {puzzle2Answer}')
    