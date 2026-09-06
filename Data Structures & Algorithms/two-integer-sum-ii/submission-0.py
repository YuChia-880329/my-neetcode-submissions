class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_left, p_right = 0, len(numbers)-1
        
        while p_left < p_right: # actually 'while true:' works better here, since the answer is guaranteed to exist
            if numbers[p_left] + numbers[p_right] < target:
                p_left += 1
            elif numbers[p_left] + numbers[p_right] > target:
                p_right -= 1
            else:
                break

        return [p_left+1, p_right+1] # 1-indexed
