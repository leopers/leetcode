from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        removed = 0
        it1 = 0
        it2 = n-1

        if nums == []:
            return 0

        while it1 < it2:
            if nums[it1] == val and nums[it2] != val:
                nums[it1], nums[it2] = nums[it2], nums[it1]
                it1 += 1
                it2 -= 1
            elif nums[it1] == val and nums[it2] == val:
                it2 -= 1
            else: 
                it1 += 1
        
        if nums[it1] == val:
            removed = n-it1
        else:
            removed = n-it1-1


        val = n - removed
        return val
        