# Find the two entries that sum to 2020 in the list contained in input.txt
# Multiply those numbers to find the answer which unlocks day 1's second puzzle
# The second puzzle uses the same target (2020) but searches for three numbers
# that add up to the target, using their product to solve the puzzle.

def findSum(nums, target):
    '''
    Traverses an array searching for two numbers that add up to the target.
    Numbers are added to a dictionary for quick querying.
    '''
    visited = {}

    for x in nums:
            diff = target - int(x)
            # Check map of already discovered numbers
            if diff in visited:
                return int(x), int(diff)

            for y in nums:
                if int(y) == diff:
                    return int(x), int(y)
                else:
                    visited[int(y)] = True

def findThreeNumSum(nums, target):
    '''
    Traverses an array searching for three numbers whose sum is equal to the target.
    Numbers are added to a dictionary for quick querying.
    '''
    visited = {}

    for x in nums:
        for y in nums:
            diff = target - int(x) - int(y)

            if diff in visited:
                return int(x), int(y), diff
            
            for z in nums:
                if z == diff:
                    return int(x), int(y), int(z)
                else:
                    visited[int(z)] = 1



if __name__ == '__main__':
    with open('input.txt') as f:
        # Read the data into an array
        numbers = f.read().split()

        target = 2020
        # Puzzle 1
        num1, num2 = findSum(numbers, target)
        print(f'Puzzle 1 answer: {num1 * num2}')
            
        # Puzzle 2
        x, y, z = findThreeNumSum(numbers, target)
        print(f'Puzzle 2 answer: {x * y * z}')

        

        

                
            

            

        
