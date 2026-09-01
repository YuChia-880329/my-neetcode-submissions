## Approach
- **Solution 1**: We utilize a hash table to record the number we have seen and compare the number to the hash table along the way.
  - We do not need values in the has table. We only need keys.
  - A key being hashed is a key we have seen.
- **Solution 2**: This solution turns the array to a whole hash table then compare the number of keys storing in the table with the length of the array.
  - It loses early stopping.
  - It remains the same complexities.

---
## Complexity
|Solution|submission|time|space|
|---|---|:---|:---|
|**Solution 1**|`submission 0`|amortized expected `O(n)`|worst case `O(n)`|
|**Solution 2**|`submission 1`|amortized expected `O(n)`| `O(n)`|
