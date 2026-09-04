from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k
        ans = [0]*k
        ans_index = 0
        for num, freq in Counter(nums).most_common(k):
            ans[ans_index] = num
            ans_index += 1

        return ans
