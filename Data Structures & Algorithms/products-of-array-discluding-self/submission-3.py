class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [nums[0]] * n
        suffixes = [nums[n-1]] * n
        for i in range(1, n-1):
            prefixes[i] = prefixes[i-1] * nums[i]
        for i in range(n-2, 0, -1):
            suffixes[i] = suffixes[i+1] * nums[i]

        # answer
        ans = [1] * n
        for i in range(n):
            if i == 0:
                ans[i] = suffixes[1]
            elif i == n-1:
                ans[i] = prefixes[n-2]
            else:
                ans[i] = prefixes[i-1] * suffixes[i+1]

        return ans
