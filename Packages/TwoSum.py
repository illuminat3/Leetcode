class Solution:
    def twoSum(self, nums, target):
        nums_length = len(nums)
        for index in range(0, nums_length):
            for index2 in range(0, nums_length):
                  if index != index2 and nums[index] + nums[index2] == target:
                      return [index, index2]