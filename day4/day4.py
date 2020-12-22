'''
Day 4 - Advent of Code
'''

import re

def readInput(file):
    '''
    Parses the input file for passport entries, returning an array of
    passport entries in key:value pair format
    '''
    with open(file) as f:
        # Passport entries are separated by a blank line (in other words,
        # two newlines)
        lines = f.read().split('\n\n')

        passports = []
        # Pare down the line into an array of passport field key:value pairs
        for line in lines:
            line = line.split()
            passports.append(line)

        return passports

def isValidPassport(passport):
    '''
    Checks a passport entry to see if it is valid (entries missing 'cid' are
    considered valid if all other fields are present)
    '''
    isValid = False

    fieldsInPassport = []
    for field in passport:
        # Split this field key:value pair
        strippedField = field.split(':')
        # Add the field to the array
        fieldsInPassport.append(strippedField[0])

    numFields = len(fieldsInPassport)
    # If all fields except 'cid' are present, passport entry is valid
    # If all fields are present, passport is valid
    if (numFields == 7 and 'cid' not in fieldsInPassport) or (numFields == 8):
        isValid = True
    
    return isValid

def validateData(passport):
    '''
    Validates each field and its respective data format for puzzle 2
    '''
    isValid = True

    passportDict = {}
    for field in passport:
        kv = field.split(':')
        passportDict[kv[0]] = kv[1]

    # One wrong field invalidates the passport
    if 'byr' not in passportDict or not (1920 <= int(passportDict['byr']) <= 2002):
        return False
    
    if 'iyr' not in passportDict or not (2010 <= int(passportDict['iyr']) <= 2020):
        return False

    if 'eyr' not in passportDict or not (2020 <= int(passportDict['eyr']) <= 2030):
        return False
    
    if 'hgt' not in passportDict or not isHeightValid(passportDict['hgt']):
        return False

    if 'hcl' not in passportDict or not isHairColorValid(passportDict['hcl']):
        return False

    if 'ecl' not in passportDict or not isEyeColorValid(passportDict['ecl']):
        return False

    if 'pid' not in passportDict or not isPidValid(passportDict['pid']):
        return False

    return isValid

def isHeightValid(height):
    isValid = False

    # Get unit character
    number = ""
    for num in height[:len(height) - 2]:
        number += num
    number = int(number)
    unit = height[len(height) - 2]

    # Centimeters
    if unit == 'c' and (150 <= number <= 193):
        isValid = True
    # Inches
    elif unit == 'i' and (59 <= number <= 76):
        isValid = True

    return isValid

def isHairColorValid(color):
    '''
    Validates the hair color value in the passport dict.
    Valid hair colors begin with a # followed by exactly six characters 0-9 or a-f
    '''
    prog = re.compile('#([0-9]|[a-f]){6}')

    return prog.match(color)

def isEyeColorValid(color):
    '''
    Validates eye color passport value, which must be one and only one
    of the valid colors in the list.
    '''
    validColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    return color in validColors

def isPidValid(pid):
    '''
    Validates passport ID field, which must be a nine-digit number including
    leading 0s
    '''
    isValid = True

    digits = []
    for digit in pid:
        digits.append(digit)

    # Must be a nine-digit number
    if not len(digits) == 9:
        isValid = False

    return isValid


if __name__ == '__main__':
    lines = readInput('input.txt')

    # Puzzle 1
    countValidPassports = 0
    for line in lines:
        if isValidPassport(line):
            countValidPassports += 1

    # Puzzle 1 answer
    print(f'Puzzle 1 Answer: {countValidPassports}')

    # Puzzle 2
    countValidPassports = 0
    for line in lines:
        if validateData(line):
            countValidPassports += 1

    # Puzzle 2 answer
    print(f'Puzzle 2 Answer: {countValidPassports}')