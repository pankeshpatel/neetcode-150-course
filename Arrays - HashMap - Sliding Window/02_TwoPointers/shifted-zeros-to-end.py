# Given an array of integers, modify the array in place to
# move all zeros to the end while maintaining the relative order
# of non-zero elements.

# Example:
# Input: nums = [0, 1, 0, 3, 2]
# Output: [1, 3, 2, 0, 0]

from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    non_zero_index = 0

    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    return nums
