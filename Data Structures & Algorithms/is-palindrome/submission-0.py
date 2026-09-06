class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join((c for c in s if c.isalnum())).upper()
        p_left, p_right = 0, len(s)-1
        while p_left < p_right:
            if s[p_left] != s[p_right]:
                return False
            # update
            p_left += 1
            p_right -= 1

        return True