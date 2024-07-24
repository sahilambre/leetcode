class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        runningMax = 0

        for i in nums:
            if i == 1:
                counter += 1

                if counter > runningMax:
                    runningMax = counter
            else:
                counter = 0
        
        return runningMax