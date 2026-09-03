## Approach
- **Solution 1**: We utilize a size-26 array for each string to compute the frequency of the characters. Then we group these strings by their frequency arrays.
  - Python lists have to be turned into tuple to become dictionary keys.
- **Solution 2**: We use the built-in Counter to compute the frequency and group strings by the Counters.
  - Counters have to be turned into frozenset to become dictionary keys.
    - This data-type-turning takes a lot of costs
- **Solution 3**: We optimize the *Solution 1* from two loops to one loop. And we discard the big array *freqs* which takes a lot of cost and lives longer.
  - Each *freq* only lives inside the for loop


---
## Complexity
- m : len(*strs*)
- n : len(the longest string in *strs*)

|Solution|Submission|Time|Space|
|---|---|:---|:---|
|**Solution 1**|submission-0|amortized expected `O(m*n)`|`O(m)`|
|**Solution 2**|submission-1|amortized expected `O(m*n)`|worst case `O(m*n)`|
|**Solution 3**|submission-2|amortized expected `O(m*n)`|`O(m)`|


---
## Note
- There's another solution which sorts each string (with ascending character order) and group them.
  - This takes `O(m*nlogn)` time
