# Understanding Python for Loop with Time Complexity

A for loop in Python is used for iterating over a sequence (like lists, tuples, dictionaries, strings, or even a range of numbers). The time complexity of a for loop depends on the operations performed inside the loop and the size of the iterable.

## Basic `for` Loop (`range(0,n)` - excluding `n`)

```python
# Example 1: Iterating over a range
for i in range(5):
    print(i)
```

Time Complexity:
- range(5) generates numbers from 0 to 4 → O(1)
- The loop runs 5 times, executing print(i) each time → O(n)
- Overall Complexity: O(n) (Linear)

## Nested for Loops


```python
# Example 2: Nested loops
n = 3
for i in range(n):
    for j in range(n):
        print(i, j)
```

Time Complexity:
- Outer loop runs n times → O(n)
- Inner loop runs n times for each iteration of the outer loop → O(n)
- Total iterations = n × n = n²
- Overall Complexity: O(n²) (Quadratic)

## Looping Through a List

```python
# Example 3: Iterating over a list
arr = [10, 20, 30, 40]
for num in arr:
    print(num)
```

Time Complexity:
- The loop iterates once per element in arr → O(n)
- Overall Complexity: O(n) (Linear)

## Looping through a list using `enumerate`


The `enumerate()` function in Python is used when you need both the index 
and the value while iterating over a sequence.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Time Complexity:
- enumerate() creates an iterable object → O(1)
- Loop iterates n times (once per element) → O(n)
- Overall Complexity: O(n) (Linear)


## Looping Through a Dictionary


```python
# Example 4: Iterating over a dictionary
data = {"a": 1, "b": 2, "c": 3}
for key, value in data.items():
    print(key, value)
```

Time Complexity:
- `.items()` creates an iterable view of dictionary items → O(1)
- The loop iterates once per key-value pair → `O(n)`
- Overall Complexity: `O(n)` (Linear)