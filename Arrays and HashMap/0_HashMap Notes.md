# HashMap Data Structure
A HashMap (also called a Dictionary in Python) is a key-value data structure that 
allows for fast data retrieval, insertion, and deletion.

# How HashMap Works
A HashMap uses a hash function to map keys to an index in an array. Each index stores a key-value pair. 
If multiple keys hash to the same index (collision), a collision-handling technique such as 
chaining (linked list) or open addressing is used.

# HashMap in Python (Dictionary)

```python

# Creating a HashMap
hashmap = {}

# Inserting Key-Value Pairs
hashmap["name"] = "Pankesh" # O(1) 
hashmap["age"] = 42  # O(1)

# Retrieving a Value - O(1) 
print(hashmap["name"])  # Output: Pankesh

# Checking if a Key Exists - O(1) 
if "age" in hashmap:
    print(hashmap["age"])  # Output: 42

# Removing a Key - O(1) 
del hashmap["age"]

# Iterating Over a HashMap - O(n)
for key, value in hashmap.items():
    print(key, "->", value)

# Getting All Keys and Values - O(1)
keys = hashmap.keys()
values = hashmap.values()
```


# Python HashMap Libraries and APIs

Python has built-in and external libraries for working with HashMaps.

## dict (Built-in)
Python’s built-in dict is a high-performance implementation of HashMap.

##  collections.OrderedDict
Maintains the insertion order of key-value pairs.

```python
from collections import OrderedDict

ordered_map = OrderedDict()
ordered_map["a"] = 1
ordered_map["b"] = 2
ordered_map["c"] = 3
print(ordered_map)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

## collections.defaultdict
Provides a default value for missing keys.

```python
from collections import defaultdict

default_map = defaultdict(int)  # Default value is 0
print(default_map["missing_key"])  # Output: 0
```

## collections.ChainMap

Combines multiple dictionaries into a single view.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_map = ChainMap(dict1, dict2)
print(combined_map['b'])  # Output: 2 (takes from first dictionary)
```

## weakref.WeakValueDictionary
Holds references to objects without preventing them from being garbage collected.

```python
import weakref

class MyClass:
    pass

weak_map = weakref.WeakValueDictionary()
obj = MyClass()
weak_map["obj"] = obj

del obj  # Now, weak_map becomes empty because the object is garbage collected
```