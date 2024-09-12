from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 

        if len(nums) == 0:
            return 0
        if len(nums) == 1: 
            return 1

        for i in range(len(nums)):
            if nums[i] != nums[k]:
                nums[k+1] = nums[i]
                k = k+1


        return k+1