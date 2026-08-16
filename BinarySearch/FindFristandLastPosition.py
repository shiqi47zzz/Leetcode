'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         first = -1
#         last = -1

#         for i in range(len(nums)):
#             if nums[i] == target:
#                 if first == -1:
#                     first = i
#                 last = i
#         return [first, last]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left = 0
            right = len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                midValue = nums[mid]
                if midValue == target:
                    result = mid
                    right = mid - 1
                elif midValue > target: 
                    right = mid - 1
                else:
                    left = mid + 1
            return result

        def findLast():
            left = 0
            right = len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                midValue = nums[mid]
                if midValue == target:
                    result = mid
                    left =  mid + 1
                elif midValue > target: 
                    right = mid - 1
                else:
                    left = mid + 1
            return result
        
        return [findFirst(), findLast()]