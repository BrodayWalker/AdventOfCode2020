# Find the two entries that sum to 2020 in the list contained in input.txt
# Multiply those numbers to find the answer which unlocks day 1's second puzzle

def findSum(nums, target):
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

if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = f.read().split()

        num1, num2 = findSum(numbers, 2020)
        answer = num1 * num2
        print(f'Puzzle 1 answer: {answer}')
            

        

        

                
            

            

        
