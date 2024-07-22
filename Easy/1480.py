class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            sum = total
            runningSum.append(sum)
        
        return runningSum