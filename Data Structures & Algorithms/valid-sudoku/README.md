## Approach
- **Solution 1**: We allocate a hash table for each row, one for each column, and one for each grid (a total of `3n` hash tables) to check if there are duplicates.




---
## Complexity
- n : `len(board)`
  - We do not view the board to be the fixed `9*9` board. Otherwise the complexity makes no sense. The board can be any n*n board as long as n is a perfect square number.

|Solution|Submission|Time|Auxiliary Space|
|:---:|:---:|:---|:---|
|**Solution 1**|submission-2|amortized expected `O(n^2)`|worst case `O(n^2)`|


---
## Note
- Do not cast the string into the integer. Compare it with string.
  - Always think twice when we cast types.
- Do not use isdigit() to check if the slot is empty. We test if it is the delimiter `.`.
  - Always check if testing with the opposite makes things easier.
- We use `n**0.5` instead of `math.sqrt(n)`.
  - No need to import.
  - When to use `n**0.5`
    1. When we only compute it a few times rather than many times.
      -  `n**0.5` is slower than `math.sqrt(n)`
    2. When we know the type is really save (e.g. result no complex number).
  - When to use `math.sqrt(n)`
    1. In real project, type check is important.
    2. When we use many power computation (e.g. in a loop)
