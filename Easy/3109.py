def minimumOperations(nums):
    steps = 0
    for num in nums:
        if (num % 3 == 0):
            steps += 0
        else:
            if((num + 1)% 3 == 0 or (num - 1)% 3 == 0):
                steps += 1
    
    return steps