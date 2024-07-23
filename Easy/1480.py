class Solution:
    def runningSum(nums):
        runningSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            sum = total
            runningSum.append(sum)
        
        return runningSum