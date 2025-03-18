Two Pointers in 7 minutes | LeetCode Pattern
https://www.youtube.com/watch?v=QzZ7nmouLTI




The Two Pointers pattern is a common technique in algorithmic problem-solving, 
and you should consider applying it when a problem involves:


### Finding Pairs or Triplets
 - If the problem asks you to `find pairs`, `triplets`, or a `subarray that satisfies a condition`, 
   two pointers can optimize brute-force approaches.

- Example: `Finding all unique triplets that sum to zero in an array`.

### Sorted or Partially Sorted Data

- If the `input array is sorted` or `can be sorted efficiently`, the two-pointer technique is often useful.
- Example: `Finding a pair of numbers that sum to a target in a sorted array`.

### Palindrome or Reversal Problems
- If you need to check if a `string or array is a palindrome`, two pointers moving inward can optimize the process.
- Example: Checking if a given string is a palindrome.


### Comparing Elements from Two Different Arrays

- When you need to `merge`, `compare`, `or find intersections of two sorted arrays`, 
  two pointers can efficiently iterate through them.

- Example: `Merging two sorted lists`.

### Sliding Window Optimization

- Sometimes, a two-pointer approach is useful in sliding window problems, especially 
 when `dynamically expanding` and `contracting a window`.
- Example: Longest substring with at most k distinct characters.

###  Minimizing/Maximizing a Condition
 - If you need to `minimize/maximize a sum, length, or some other parameter within a subarray`, the two-pointer method helps.
- Example: Finding the smallest subarray whose sum is greater than or equal to a given value.


## When NOT to Use Two Pointers
- If the problem involves unsorted data and sorting it isn't feasible (e.g., time constraints).
- If the problem requires random access (e.g., hashing might be better).
- If the problem involves graphs or trees, where BFS/DFS is more suitable.