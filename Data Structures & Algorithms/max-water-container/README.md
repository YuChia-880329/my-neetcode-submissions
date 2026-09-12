## Approach
- **Solution 1**: We maintain two pointers and greedily move the one with smaller height inward and compare for the maximum volume.


---
## Complexity
- n : `len(heights)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-2|`O(n)`|`O(1)`|


---
## Note
- **Thinking process**:
  1. Find the exact formula
  2. We move the one really control the volume. `volume = h_min * width`. Therefore we move the one with smaller height.
- Comparison for linear skill
  - The way of *maximum subarray* :
    1. The maximum one can be inherited and passed on since they use the same increment.
      - Therefore we do the one pointer from left to right.
    2. The formula is about the whole subarray and can not be computed by only two side pinters
      - Not suitable for two pointers.
  - The way of *maximum water container* :
    1. The maximum one depends on two heights only.
      - Suitable for two pointers.
    2. The maximum one cannot be inherited and passed on. The old max does not imply the new max.
      - We cannot use one pointer from left to right.
- When we using skills of pointers, we better check if the fast forwarding is possible.
- When do we use `max()` or `min()`?
  - When there is a whole iterable to compare
    - Low level C works faster
  - For readability
  - Do not use it when there is only two arguments and it is inside a loop.
    - The c function call overhead
- Always use the *multiple assighment*.
  - CPython optimization : no tuple constructed in heap
  - Faster CPU instruction
  - Especially when swapping
- Ternary operation:
  - It is better to write `if ans < volume: ans = volume` than `ans = ans if ans>volume else volume`
    - The ternary operation forces python to write.
    - Especially when we are in a loop.
