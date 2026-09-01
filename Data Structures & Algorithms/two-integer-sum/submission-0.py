class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {}
        for index, num in enumerate(nums):
            diff[target-num] = index

        for index, num in enumerate(nums):
            if num in diff and diff[num]!=index:
                return [diff[num], index] if diff[num] < index else [index, diff[num]]
        