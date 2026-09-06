## Approach
- **Solution 1**: We utilize the *disjoint set union* data structure to maintain different consecutive sequences.
  - Remember to use `find()` to check if these two elements belong to different sets before `union()`
    - Or we better write it in `union()` for safety
- **Solution 2**: We put all the numbers into a hash table for checking the existence in constant time . Then we check if each number is a *head of any consecutive sequence* by checking if that number-1 exists.
  - `Set` initialization can be directly done by giving `Iterable`. Don't use *for loop*
  - Iterate the set instead of the original list to avoid duplicate checks.
  - The thinking process can be:
    1. If we do know if this number-1 exists, then we can be sure if it's a *head of any consecutive sequence*
    2. How do we know if this number-1 exists -> hash table helps in constant time


---
## Complexity
- n : `len(nums)`
- alpha() : the *inverse Ackermann function*

|Solution|Submission|Time|Space|
|---|---|:---|:---|
|**Solution 1**|submission-1|amortized `O(n*alpha(n))`|worst case `O(n)`|
|**Solution 2**|submission-3|amortized expected `O(n)`|worst case `O(n)`|


---
## Note
- If the input `nums` dynamically grows or the input is given one by one(online-algorithm), then **Solution 1** works better than **Solution 2**.
  - We won't want to iterate the set every time the new input number is given.
