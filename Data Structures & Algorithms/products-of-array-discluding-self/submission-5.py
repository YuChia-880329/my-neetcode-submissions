class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # prefixes
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            # update
            left_product *= nums[i]

        # suffixes
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            # update
            right_product *= nums[i]

        return ans
