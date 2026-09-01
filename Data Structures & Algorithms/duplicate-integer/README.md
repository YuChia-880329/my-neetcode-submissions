## Approach
- **Solution 1**: We utilize a hash table to record the number we have seen and compare the number to the hash table along the way.
  - We do not need values in the has table. We only need keys.
  - A key being hashed is a key we have seen.

---
## Complexity
|Solution|time|space|
|---|:---|:---|
|**Solution 1**|amortized expected `O(n)`|worst case `O(n)`|
