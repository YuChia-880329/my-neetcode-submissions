class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        for i in nums:
            if i in seen_nums:
                return True
            else:
                seen_nums.add(i)
        return False
        