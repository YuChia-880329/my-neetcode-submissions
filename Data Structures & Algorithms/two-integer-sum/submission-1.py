class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}
        for index, num in enumerate(nums):
            diff = target-num
            if num in diffs:
                return [diffs[num], index]
            else:
                diffs[diff] = index
