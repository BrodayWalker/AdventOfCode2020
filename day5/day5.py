'''
Advent of Code 2020 - Day 5
Binary Boarding
'''

import math

def readInput(file):
    with open(file) as f:
        return f.read().split()

def splitLine(line):
    '''
    Splits the string line into the row and seat instructions
    Row: 7 characters (either F or B)
    Seat: 3 characcters (either L or R)
    Returns row, seat 
    '''
    row = ''
    seat = ''

    i = 0
    while i < len(line):
        if i < 7:
            row += line[i]
        else:
            seat += line[i]
        i += 1

    return row, seat

def binarySearch(line, low, high):
    # used to traverse the line string which holds instructions
    i = 0
    while low < high and i < len(line):
        direction = line[i]

        if direction == 'F' or direction == 'L':
            high = ((high - low) // 2) + low
        elif direction == 'B' or direction == 'R':
            low = math.ceil((high + low) / 2)
        i += 1

    return low

def calculateSeatID(row, col):
    return row * 8 + col

def findOpenSeat(seatIDs):
    openSeat = -1

    i = 1
    for id in seatIDs:
        if seatIDs[id] != seatIDs[id - 1] + 1:
            return seatIDs[id] - 1
        i += 1

    return openSeat

if __name__ == '__main__':
    lines = readInput('input.txt')

    # Puzzle 1
    highestSeatID = -1
    seatIDs = [] # Used for puzzle 2
    for line in lines:
        row, seat = splitLine(line)
        rowPosition = binarySearch(row, 0, 127)
        colPosition = binarySearch(seat, 0, 7)
        seatID = calculateSeatID(rowPosition, colPosition)
        seatIDs.append(seatID)

        if seatID > highestSeatID:
            highestSeatID = seatID

    # Puzzle 2
    seatIDs.sort()
    openSeat = findOpenSeat(seatIDs)

    # Puzzle 1 answer:
    print(f'Puzzle 1 answer: {highestSeatID}')

    # Puzzle 2 answer
    print(f'Puzzle 2 answer: {openSeat}')

