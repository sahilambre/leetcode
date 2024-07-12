def orArray(nums):
        ans = []
        n = len(nums)
        for i in range(n - 1):
            ans.append(nums[i] | nums[i + 1])
        return ans