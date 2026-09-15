## Approach
- **Solution 1**: We maintain a window from left to right to track a non-duplicate substring. And use a dictionary to indicate the index where it last appeared.
  - We don't need to clean up the indices when we move the `window_left`.
  - *Lazy evaluation*
    - Update the answer only when the window is shrinked. It can avoid many updates when the string is long and few duplicate characters.



---
## Complexity
- n : `len(s)`
- m : number of different characters in `s`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-1|`O(n)`|`O(m)`|


---
## Note
- We can use `.get()` method for dictionary so that we can combine the check "if some key's in" and "the look up for the key".
