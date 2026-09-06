## Approach
- **Solution 1**: We use two pointers to detect the sum.
  - logic:
    1. If sum is too large : the right pointer should decrease, since there can be no answer that is paired with this big number.
    2. If sum is too small : the left pointer should increase, since there can be no answer that is paired with this small number.
    3. If sum equals target : it's the answer.




---
## Complexity
- n : `len(numbers)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-1|`O(n)`|`O(1)`|


---
## Note
- If the numbers are not sorted, we do need a table to look up for what we want.
- But if the numbers are already sorted, some nice properties stand out.
  - Always think twice when the numbers are sorted
- Always check if we make any redundant calculation after writing code.
  - e.g. the `sum` in *Submission-0*
