## Approach
- **Solution 1**: `len(strs)` + `SEP` + `len(metadata)` + metadata(with SEP): end positions of the string data(starting from the data section) + data:`strs`
  - **Header-Payload Architecture**
  - Good for random access.
    - e.g. *MP4*、*pdf*
  - Good for parellel proccessing.
  - Good for hardware cooperation
    - e.g. CPU deals with payload, GPU deals with data
  - This solution has an additional information in the front.
- **Solution 2**: `len(s) + SEP + s` for each s in `strs`
  - **Length-Prefixed Framing**
  - Good for serial input.
    - e.g. Internet streaming



---
## Complexity
- m : sum of lengths of all `s` in `strs`
- n : `len(strs)`

|Solution|Submission|Time|Space|
|---|---|:---|:---|
|**Solution 1**|submission-4|`O(m)`|`O(n)`|
|**Solution 2**|submission-5|`O(m)`|`O(n)`|


---
## Note
- string addition and copying is expensive:
  - Codes like `'a' + 'b'` or `str.split()` copy a lot of strings since strings are immutable (in almost every programming language)
    - It may take more time and space complexity than we expect
  - Instead, we use formatted string, list of strings, lazy evaluation(e.g. generators in python) and index pointer to deal with strings to save time and space.
  - When to use methods like `str.split()`
    1. When the output directly needs us to split strings
    2. When the strings are short and the string operations are not the main point (do not take a lot of time)
  - When **not** to use methods like `str.split()`
    1. When the strings are long and the string operations are really important
    2. When we deal with the low layer infrastructure (e.g. this problem)
