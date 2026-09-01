## Approach
- **Solution 1**: We utilize a hash table to record the difference between the target and each number. Then we test if each number has corresponding difference in the hash table.
	- The second condition in line 9 is crutial. Otherwise, `nums=[3, 2, 4], target=6` would return `[0, 0]`.
- **Solution 2**: We greedily check each number when we traverse the `num` array and comprass the two for loops in *Solution 1* into one for loop.
  - The solution now has the early stopping property.

---
## Complexity
|Solution|Submission|Time|Space|
|---|---|:---|:---|
|**Solution 1**|submission-0|amortized expected `O(n)`|worst case `O(n)`|
|**Solution 2**|submission-1|amortized expected `O(n)`|worst case `O(n)`|
