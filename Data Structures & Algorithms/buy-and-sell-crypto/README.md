## Approach
- **Solution 1**: The textbook solution. Get all the differences and calculate the maximum subarray by Kadane's Algorithm.
  - naming mistake : It should be the `right_max` instead of the `left_max`.
- **Solution 2**: We Maintain a window moving from left to right.
  - The left side should be the minimum in the left checked subarray.
  - The right side moves on with the for loop.
  - The property we want to maintain is the maximality of the difference, the rifht side minus the left side.
  - This solution is easy to prove.
  - This solution only takes one array look up instruction instead of two each iteration.



---
## Complexity
- n : `len(prices)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-0|`O(n)`|`O(1)`|
|**Solution 2**|submission-1|`O(n)`|`O(1)`|
