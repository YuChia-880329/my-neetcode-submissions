## Approach
- **Solution 1**: We utilize two hash tables to record the frequency of each character. Then we compare two hash tables.
	- Since we do not utilize the number 26 in this solution, we cannot veiw this solution as constant space.
- **Solution 2**: We utilize one hash table to record the difference of frequency. The appear of character in `s` corresponds to `+1`. The appear of character in `s` corresponds to `-1`.
	- In this way, we only need one hash table
- **Solution 3**: We utilize one hash table to record the difference of frequency as `Solution 2`. But we fix the table size to contain 26 lower case alphabets.
- **Solution 4**: We utilize one list instead of one hash table to record the difference of frequency and fix the list size to count 26 lower case alphabets.
	- If we fix the size, we don't need hash table
 	- From hashing to direct addressing

---
## Complexity
|Solution|Submission|Time|Space|
|---|---|:---|:---|
|**Solution 1**|Submission 0|amortized expected `O(m+n)`|worst case `O(m+n)`|
|**Solution 2**|Submission 1|amortized expected `O(m+n)`|worst case `O(m+n)`|
|**Solution 3**|Submission 2|amortized expected `O(m+n)`|`O(1)`|
|**Solution 4**|Submission 3|amortized expected `O(m+n)`|`O(1)`|

---
## Note
- If there is a big gap between the size of `universe` and the size of `the set of keys we use`, then **hash table** performs well. Otherwise, we choose **direct addressing table**.
	- `universe` here is 26 lower case alphabets
 	- `the set of keys we use` depends on the string length. Here it says, `1 <= s.length, t.length <= 5 * 10^4`.
  		- We are likely using all the alphabets. Thus **direct addressing table** works better.
    - **hash table** here needs time overhead to compute hash values, and space overhead for the table.
