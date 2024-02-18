class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2
        else:
            return nums[length // 2]