Sliding window Techniques

- Used when solving `subarray or substring` problems (e.g., "smallest subarray with sum ≥ X")
- `One pointer expands/contracts` a "window" dynamically (e.g., left and right adjusting)
- `Fixed-size & variable-size window` problems (subarrays, substrings)
- When we need to maintain a range (window) of elements to satisfy a condition

### When to Use:
- Contiguous Subarrays or Subsequences: Works well when solving problems that involve 
  finding subarrays, substrings, or continuous sequences.

- Fixed/Variable-Length Window:
 - Fixed-Length: When the window size is known in advance.
 - Variable-Length: When expanding and shrinking a window based on conditions is required.

- Optimizing Subarray Problems: Helps in problems like finding the maximum/minimum sum 
  in a subarray or longest substring with unique characters.

### When NOT to Use:

- Non-Contiguous Elements Are Needed: 
  If the problem does not deal with continuous elements, this approach might not work.

- Sorting is Required: 
  If sorting is necessary before solving the problem, a different approach might be needed.


- Multiple Windows Must Be Tracked: 
   If more than one window needs to be tracked simultaneously, dynamic programming 
   or a different approach might be more efficient.