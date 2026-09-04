from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # count frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # bucket sort
        buckets = [[] for _ in range(n+1)] # 1 more slot for better reading
        for num, freq in freqs.items():
            buckets[freq].append(num)


        # top k
        ans = [0] * k
        ans_index = 0
        for bucket in buckets[::-1]:
            for num in bucket:
                ans[ans_index] = num
                ans_index += 1
            if ans_index >= k:
                break

        return ans
        