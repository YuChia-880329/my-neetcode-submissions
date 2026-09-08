class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # sorting : insertion sort
        for i in range(1, n): # i from 1 to n-1
            cur_num = nums[i]
            p = i - 1
            while (p >= 0) and (nums[p] > cur_num):
                nums[p+1] = nums[p]
                p -= 1
            nums[p+1] = cur_num # Here p is either -1 or nums[p] <= cur_num

        # early stopping
        if (nums[0]>0) or (nums[n-1]<0):
            return []

        # 2 pointers
        ans = []
        for i in range(n-2): # i from 0 to n-3
            # fast forwarding
            if (i>0) and (nums[i]==nums[i-1]):
                continue
            num = nums[i]
            # early stopping
            if num > 0:
                break

            # subproblem : sorted 2sum, nums[i+1:n-1], target=-num
            p_left, p_right = i+1, n-1
            target = -num
            # early stopping
            if nums[p_left] > target:
                break
            # sorted 2sum
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
                    while (p_left<p_right) and (nums[p_left]==nums[p_left-1]):
                        p_left += 1
                    while (p_left<p_right) and (nums[p_right]==nums[p_right+1]):
                        p_right -= 1

        return ans
