from typing import List
class Solution1:
    def moveZero(self,nums: List[int]) -> None:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range (slow,len(nums)):
            nums[i]=0