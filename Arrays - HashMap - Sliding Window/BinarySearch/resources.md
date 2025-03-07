A problem that falls into the Binary Search category typically has the following characteristics:


# Sorted or Monotonic Input
- The input array or data structure must be `sorted` (either in ascending or descending order) 
   or exhibit monotonic behavior (always increasing or always decreasing).

- Example: Searching for a number in a sorted array.

# Search Space Reduction

- The problem should allow you to `reduce the search space by half at every step`.
- Example: Looking for a value in a dictionary, phone book, or sorted database.


# Deterministic Condition to Move Left or Right

- There should be a clear rule that `decides whether to move to the left half` or the `right half of the search space`.
- Example: In a guessing game, where if your guess is too low, you are told to "guess higher".