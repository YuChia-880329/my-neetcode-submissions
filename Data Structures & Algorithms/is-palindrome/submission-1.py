class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_left, p_right = 0, len(s)-1
        while True:
            # check
            while (p_left<p_right) and (not s[p_left].isalnum()): # first condition: in case there are zero alnum
                p_left += 1
            while (p_left<p_right) and (not s[p_right].isalnum()): # first condition: in case there are zero alnum
                p_right -= 1
            if p_left >= p_right:
                break

            if s[p_left].upper() != s[p_right].upper():
                return False

            # update
            p_left += 1
            p_right -= 1
            # if it finishes, it will break in the next check section

        return True
