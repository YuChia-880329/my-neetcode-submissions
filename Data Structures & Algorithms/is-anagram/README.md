## Approach
- **Solution 1**: We utilize two hash tables to record the frequency of each character. Then we compare two hash tables.
- **Solution 2**: We utilize one hash table to record the difference of frequency. The appear of character in `s` corresponds to `+1`. The appear of character in `s` corresponds to `-1`.
	- In this way, we only need one hash table

---
## Complexity
|Solution|time|space|
|---|:---|:---|
|**Solution 1**|amortized expected `O(m+n)`|worst case `O(m+n)`|
|**Solution 2**|amortized expected `O(m+n)`|worst case `O(m+n)`|
