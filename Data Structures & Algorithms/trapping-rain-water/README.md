## Approach
- **Solution 1**: We calculate the water chunk-by-chunk.
-   - *chunk-by-chunk* solution
    - Remember to move from the shoter wall.
- **Solution 2**: We maintain two arrays to record `left_max_height` and `right_max_height` for each index. And we calculate the water on each column by the math formula `min(left_max_height[i], right_max_height[i])-height[i]` if `height[i]` is smaller.
-   - A standard *bottom-up dp* solution mixed with *two pointers* technique. But it does not do well for the space complexity.
- **Solution 3**: We maintain two pointers and two walls and move forward from the shorter walls.
-   - column-by-column* solution
    - Standard answer for interviewing
    - It caanot fast forward the pointers.
    - It uses more *if-else* branching.
      - Heavily loading on the CPU branch predictor.


---
## Complexity
- n : `len(height)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-3|`O(n)`|`O(1)`|
|**Solution 2**|submission-6|`O(n)`|`O(n)`|
|**Solution 3**|submission-5|`O(n)`|`O(1)`|


---
## Note
- **Thinking process**:
  1. What is the mathmetical formula of the answer?
  2. It seams like the local answer depends on two parameters `left_max_height` and `right_max_height`. But it is actually dictated by the shorter one between them.
    - Starting from the shorter one, we can do it greedily.
- The *array slot pre-allocation* is an optimizatoin for python, but is distroys a lot of readability.
  - Don't do that during the interview.
- The *two pointers* technique really relies on the greedy choice to speed up.
  1. If there is a "container-like" optimal structure for the answer. We can consider the *two pointers* technique.
  2. Then we analyze the mathematical formula of the answer, seeing that if there is certain parameter dictating the formula
     - Maybe we can make some greedy choices.
