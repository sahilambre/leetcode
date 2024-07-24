class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num > 0:
            if num % 2 == 0:        # checking for even
                num = num / 2
                steps += 1
            else:                   # checking for odd
                num = num - 1
                steps += 1
        return steps
