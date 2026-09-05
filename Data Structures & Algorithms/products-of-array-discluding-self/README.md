## Approach
- **Solution 1**: We calculate the product of all the numbers, and utilize division to get the final answers.
  - Be careful with the `0`s in the input: edge cases.
    1. No `0`
    2. One `0`
    3. Multiple `0`s
- **Solution 2**: We calculate all the prefix products and suffix products like we do in the *prefix sum* technique.
  - We can utilize the answer array without construct other auxiliary arrays.
  - The `left_product` and the `right_product` can be computed consecutively.



---
## Complexity
- n : `len(nums)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-2|`O(n)`|`O(1)`|
|**Solution 2**|submission-5|`O(n)`|`O(1)`|


---
## Note
- We should always consider to utilize the output space to save the auxiliary space
- *afterward update* or *beforehand update* (in the loop) can avoid awkward index computation when chosen well.
