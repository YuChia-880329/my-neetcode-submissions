## Approach
- **Solution 1**: We copy a new string removing the none-alphanumeric characters and turn characters to upper cases. Then we check if it's palindrome with two pointers.
  - This solution is more elegant and readable but takes more space.
- **Solution 2**: We directly use two pointers to check the string, skipping the character when it's not alphanumeric.
  - The edge condition has to be carefully treated.
    1. Is the stopping condition `s[p_left].isalnum()` always safe?
    2. No, if `p_right==n-1` and non-alphanumeric, `p_left` might become `n`




---
## Complexity
- n : `len(s)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-0|`O(n)`|worst case `O(n)`|
|**Solution 2**|submission-1|`O(n)`|`O(1)`|


---
## Note
- The outer while loop condition can be checked by the code in the body, so we use `while True:` loop to save the comparison time in each iteration.
  - While for the readability, we can still put the comparison back.
    - The last iteration will stop earlier but the intermediate iterations get slower down by an extra comparison.
