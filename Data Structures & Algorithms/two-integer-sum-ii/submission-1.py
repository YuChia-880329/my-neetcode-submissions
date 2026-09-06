class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_left, p_right = 0, len(numbers)-1

        while p_left < p_right: # Actually 'while true:' works better here, since the answer is guaranteed to exist
            sum = numbers[p_left] + numbers[p_right]
            if sum > target:
                p_right -= 1
            elif sum < target:
                p_left += 1
            else:
                break

        return [p_left+1, p_right+1] 
