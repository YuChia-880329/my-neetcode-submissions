from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # heap sort
        def heapsort(freqs, k):
            h = []
            for num, freq in freqs.items():
                if len(h) < k:
                    heapq.heappush(h, (freq, num))
                else:
                    heapq.heappushpop(h, (freq, num))

            # top k
            ans = [0]*k
            for index in range(k-1, -1, -1):
                ans[index] = heapq.heappop(h)[1]
            return ans

        dist_count = len(freqs)
        COUNT_METHOD_THRESHOLD = 10**2
        if dist_count == 1:
            return [nums[0]]
        elif dist_count <= COUNT_METHOD_THRESHOLD:
            return [num for num, _ in sorted(freqs.items(), key=(lambda item:item[1]), reverse=True)[:k:]]
        else:
            return heapsort(freqs, k)
