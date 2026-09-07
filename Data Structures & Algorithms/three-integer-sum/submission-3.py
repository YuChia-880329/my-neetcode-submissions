class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # sort
        nums.sort()

        # greedy check
        if nums[0] > 0 or nums[n-1] < 0:
            return [] 

        ans = []
        # 2 pointers
        temp_i = None
        for i in range(n-2): # i: from 0 to n-3
            num = nums[i]
            # redundant iterations
            if temp_i == num:
                continue
            if num > 0:
                break
            temp_i = num
            # subproblem : sorted 2-sum, nums[i+1:n-1], target=-num
            p_left, p_right = i+1, n-1
            target = -num
            # greedy check
            if nums[p_left] > target:
                break
            temp_l = None
            while p_left < p_right: # 'while True:' works better, but here for readability
                num_l, num_r = nums[p_left], nums[p_right]
                sum_ = num_l + num_r
                if sum_ < target:
                    p_left += 1
                elif sum_ > target:
                    p_right -= 1
                elif temp_l != num_l : # temp_l == num_l iff temp_r == num_r
                    temp_l = num_l
                    ans.append([num, num_l, num_r])
                    p_left += 1
                    p_right -= 1
                else:
                    p_left += 1
                    p_right -= 1

        return ans
