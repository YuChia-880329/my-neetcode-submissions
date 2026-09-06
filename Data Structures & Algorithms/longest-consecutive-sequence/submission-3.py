class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = set(nums)

        # max size
        max_size = 0
        for num in record:
            if num-1 not in record:
                size = 1
                k = num + 1
                while k in record:
                    size += 1
                    k += 1
                if max_size < size:
                    max_size = size

        return max_size
