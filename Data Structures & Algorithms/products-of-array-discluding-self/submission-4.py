class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # prefixes
        for i in range(1, n):   
            ans[i] = ans[i-1] * nums[i-1]
        # suffixes
        right_product = 1
        for i in range(n-2, -1, -1): 
            right_product *= nums[i+1]
            ans[i] *= right_product

        return ans
