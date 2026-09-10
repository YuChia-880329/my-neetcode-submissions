import heapq
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # sorting : heap sort
        Solution._heapsort(nums)

        # early stopping
        if (nums[0]>0) or (nums[n-1]<0):
            return []

        # two pointers
        ans = []
        for i in range(n-2): # i from 0 to n-3
            # fast forwarding
            if (i>0) and (nums[i-1]==nums[i]):
                continue
            # early stopping
            num = nums[i]
            if num > 0:
                break
            # subproblem : sorted 2sum, nums[i+1:n-1], target = -num
            p_left, p_right = i+1, n-1
            target = -num
            # early stopping
            if nums[p_left] > target:
                break
            while p_left < p_right:
                sum_ = nums[p_left] + nums[p_right]
                if sum_ < target:
                    p_left += 1
                elif sum_ > target:
                    p_right -= 1
                else:
                    ans.append([num, nums[p_left], nums[p_right]])
                    p_left += 1
                    p_right -= 1
                    # fast forwarding
                    while (p_left<p_right) and (nums[p_left-1]==nums[p_left]):
                        p_left += 1
                    while (p_left<p_right) and (nums[p_right+1]==nums[p_right]):
                        p_right -= 1

        return ans

    @staticmethod
    def _heapsort(nums: List[int]):
        # build max heap
        Solution._buildheap_max(nums)
        # sorting
        heapsize = len(nums)
        for i in range(heapsize-1, 0, -1): # i from heapsize-1 to 1
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            Solution._shiftdown_max(nums, heapsize, 0)

    @staticmethod
    def _buildheap_max(nums: List[int]):
        heap_size = len(nums)
        for i in range((heap_size-1)//2, -1, -1): # i from (heap_size-1)//2 to 0
            Solution._shiftdown_max(nums, heap_size, i)

    @staticmethod
    def _shiftdown_max(heap: List[int], heap_size: int, i:int):
        while i < heap_size: # actually, we can use 'while true:' here
            left_child = (i << 1) + 1 # i*2+1
            right_child = left_child + 1 # i*2+2
            max_i = i
            if left_child<heap_size and heap[max_i]<heap[left_child]:
                max_i = left_child
            if right_child<heap_size and heap[max_i]<heap[right_child]:
                max_i = right_child
            if max_i != i:
                heap[max_i], heap[i] = heap[i], heap[max_i]
                i = max_i
            else:
                break
