from collections import Counter
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """

    def create_complement_to_index_mapping():
        complement = {}
        for i, num in enumerate(nums):
            complement[target - num] = i
        return complement

    complement = create_complement_to_index_mapping()

    for i, num in enumerate(nums):
        if num in complement and i != complement[num]:
            return [i, complement[num]]


print(twoSum([2, 7, 11, 15], 9))
