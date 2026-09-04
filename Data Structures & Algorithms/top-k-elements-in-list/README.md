## Approach
- **Solution 1**: We count the frequency of each number by a hash table and use **bucket sort** to sort the number via their frequencies.
  - Since the frequency cannot exceed `n`, the length of `nums`, we can use length `n` array to represents buckets.
    - in fact we use length `n+1`, because:
      - buckets is not the final answer
      - readability of the code
  - best solution for big O complexity, but it spends a lot of sapce(especially when there are only a few distinct numbers in `nums`)
  - We use array, insted of linkedlist, in each bucket because:
    1. lower cache miss
    2. It spends more time and space constructing that many *deques* than *list*(array) resizing in python
- **Solution 2**: We use the built-in Counter and the method most_common.
  - What it actually does is hybrid. It depends on distinct numbers in `num`:
    1. When there is `1`, just return the number
    2. When there are not many, use simple sorting(sorting with little overhead time or space)
    3. When there are many, maintain a heap with size `k` and sort it.
  - Why **heap**?
    1. *bucket sort* takes too much space when there are only a few distinct numbers in `num`
    2. In practice, sometimes, the order of the output does matter.
  - It's a trade-off between time and space.
- **Solution 3**: We simulate the way Python does.
  - In python, maintaining the length of a list on our own is not encouraging.
    - `+= 1` may take more time then `len()`


---
## Complexity
- n : `len(num)`

|Solution|Submission|Time|Space|
|---|---|:---|:---|
|**Solution 1**|submission-3|amortized expected `O(n)`|`O(n)`|
|**Solution 2**|submission-4|amortized expected `O(n*log(k))`|worst case `O(n)`|
|**Solution 3**|submission-7|amortized expected `O(n*log(k))`|worst case `O(n)`|


---
## Note
- When to use *hash table*:
  1. When we need to check if the element has appeared but there is quite a gap between the *universe* and *the values we use*.
  2. When we need to count the frequency but there is quite a gap between the *universe* and *the values we use*.
  3. When we need to group things by some keys but there is quite a gap between the *key universe* and *the keys we use*.
  4. When we simply want to save the space.
- When to use *bucket sort*:
  1. When we need to group things by some keys and produce some order (between each thing or between each bucket) and **we know exactly the range the keys would be in**.
  2. When the grouping can be uniform of some kind. (We use almost every bucket and the number of things in each bucket are similar)
