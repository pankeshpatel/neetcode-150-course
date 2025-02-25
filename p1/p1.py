# given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


# nums = [1, 4, 3, 5, 4]
# True

# numns = [1,2,3,4,5]
# False

# Approach 1:
# for loop to compare each element in the array
# time complexity : O(n^2)

# Approach 2: time complexity O(nlogn)

# numbers = [1, 4, 5, 5, 5]
# sorted_numbers = sorted(numbers)
# result = False

# for i in range(len(sorted_numbers) - 1):
#     if sorted_numbers[i] == sorted_numbers[i + 1]:
#         result = True
#         break

# print(f"The result is {result}")


# approach 3: Hash Set O(n)

# hash_set = set()

# numbers = [1, 4, 2, 3, 5]
# result = False


# for element in numbers:
#     print(element)
#     if element in hash_set:
#         result = True
#     else:
#         hash_set.add(element)

# print(f"The result is {result}")


# approach 4

# numbers = [1, 4, 5, 3, 5]
# numbers_set = set(numbers)
# result = False


# if len(numbers) == len(numbers_set):
#     result = False
# else:
#     result = True

# print(f"The result is {result}")
