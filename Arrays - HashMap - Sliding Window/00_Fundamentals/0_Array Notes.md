Arrays

- Accessing element = O(1)
- Insert = O(1) / O(n) in worst case - (beginning/middle insertion with shifts)
- Delete = O(1) / O(n) in worst case - (shifting)
- Traverse = O(n)
- Search = Linear Search O(n) / Binary Search O(log n)
- Update - O(1)


## Array Insert 

The time complexity of inserting an element into an array data structure depends on where the insertion occurs:

At the end (`append`) → `O(1)` (amortized)

If the array has enough space, `appending` an element is `O(1)`.

If resizing is needed (in dynamic arrays like Python's list), it takes O(n) in worst-case scenarios but is O(1) amortized due to exponential resizing.

At the beginning (shift elements right) → `O(n)`

Every element must shift one position to the right.
At an arbitrary index → `O(n)`

Elements after the insertion index must shift one position to the right.

Summary:
- Best case (end insertion without resizing): O(1)
- Worst case (beginning/middle insertion with shifts): O(n)
- Amortized complexity (dynamic array expansion): O(1) on average


# Array Delete

The time complexity of deleting an element in an array data structure depends on where the deletion occurs:

1. Deleting from the End (Pop) → O(1)

If you remove the last element, it is a simple operation with O(1) complexity.
Example: arr.pop() in Python.

2. Deleting from the Beginning (Shift Left) → O(n)

All elements must shift one position to the left.

```python
arr = [1, 2, 3, 4, 5]
del arr[0]  # Removes 1, shifts [2,3,4,5] left
```

Takes `O(n)` because shifting affects all n elements.


3. Deleting from the Middle → O(n)
Elements to the right of the deleted element must shift left.

```python
arr = [10, 20, 30, 40, 50]
del arr[2]  # Removes 30, shifts [40, 50] left
```


The worst case is when deleting near the beginning, requiring the most shifts.



Summary of Deletion Complexity
Case	Time Complexity
Delete from end	O(1)
Delete from beginning	O(n)
Delete from middle	O(n)


### Python Syntax

1. Insert Operations using Python List

```python
arr = [10, 20, 30, 40]

# Insert at index 2
arr.insert(2, 25)  # O(n)
print(arr)  # [10, 20, 25, 30, 40]

# Append at the end
arr.append(50)  # O(1) amortized
print(arr)  # [10, 20, 25, 30, 40, 50]
```


2. Delete Operations

```python
arr = [10, 20, 30, 40, 50]

# Delete at index 2
del arr[2]  # O(n)
print(arr)  # [10, 20, 40, 50]

# Pop from end
arr.pop()  # O(1)
print(arr)  # [10, 20, 40]

# Remove first occurrence of a value
arr.remove(20)  # O(n)
print(arr)  # [10, 40]
```

3. Update Operations


```python
arr = [10, 20, 30, 40]
arr[2] = 99  # O(1)
print(arr)  # [10, 20, 99, 40]
```

4. Search Operations

```python
arr = [10, 20, 30, 40]

# Find index of a value
index = arr.index(30)  # O(n)
print(index)  # 2
```


5. Traversing an Array

```python
arr = [10, 20, 30, 40]

for num in arr:  # O(n)
    print(num)
```


6. Sorting an Array


```python
arr = [40, 10, 30, 20]
arr.sort()  # O(n log n)
print(arr)  # [10, 20, 30, 40]
```

Sorting in Python can be done using two different approaches:



#### Using sorted(numbers) (Returns a New Sorted List)

```python
sorted_numbers = sorted(numbers)
```

- Time Complexity: O(n log n)
- Why? Python’s built-in sorted() uses Timsort, which is a combination of Merge Sort and Insertion Sort.
- Space Complexity: O(n) (since it creates a new list).

#### Using numbers.sort() (Sorts In-Place)

```python
numbers.sort()
```

- Time Complexity: O(n log n)
- Why? Again, it uses Timsort.
- Space Complexity: O(1) (since it modifies the list in place).