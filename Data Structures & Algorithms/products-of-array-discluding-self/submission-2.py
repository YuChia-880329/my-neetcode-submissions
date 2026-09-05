class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        # answer
        ans = [0] * len(nums)
        if zero_count == 0:     # There's no *zero*
            for i, num in enumerate(nums):
                ans[i] = product // num
        elif zero_count == 1:   # There's one *zero*
            for i, num in enumerate(nums):
                if num == 0:
                    ans[i] = product
                else:
                    ans[i] = 0

        return ans
