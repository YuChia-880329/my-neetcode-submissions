## Approach
- **Solution 1**: We sort the array first. And we iterate the sorted array with `i` as the possible most left index in the triplet. The rest is a subproblem *sorted 2sum*.
  - Why iterating `i`?
    - Remember when solving *2sum*, we rearrange the equality and free one for loop. This technique can also apply here.
      - `nums[j] + nums[k] = 0 - nums[i]`.
  - Why sorting?
    - We couldnot afford a sorting when solving *2sum* since the time complexity was only `O(n)`.
    - Here the time complexity is `O(n^2)`, we can do a sorting first.
    - After sorting we can apply the two pointers technique as in *sorted 2sum*


---
## Complexity
- n : `len(nums)`

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-9|`O(n^2)`|`O(1)`|


---
## Note
- Some *early stopping* techniques are applied. They exist because the special power of `0`.
  - Otherwise, these do not work
  - We can just remember the one outside the for loop. Other ones are tricky and run a risk in making mistakes during the interview.
- *Fast forwarding* techniques are applied in order to avoid duplicate triplets.
  - The way to remember: three pointers all have to do the *fast forwarding*. Do not miss any one of them.
  - Do not use state variables to avoid duplicate triplets. We don't have to do that.
- Remember to avoid reserved key words. For example, `sum`
- Be careful with the boundary condition of loops.
  - `range(n-2)` means from `0` to `n-3`
  - Being used to write down comments after special for loops can effectively decrease the likelihood of making mistakes.
    - `for i in range(n-2) # i from 0 to n-3`
- We write the sorting on our own, but during interview, we better use a line to abstract the sorting
  - If a sorting with `O(n*logn)` time complexity and strict `O(1)` space complexity is asked for, then *heap sort* should be the answer
    - Make the heap in-place.
  - The sorting python use is *Tim sort*.
    - `O(n*logn)` time complexity in the worst case
    - `O(n)` space complexity in the worst case
