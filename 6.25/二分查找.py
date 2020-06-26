from typing import List
def binarySearch(nums:List,val:int):
    left=0
    right=len(nums)-1
    while left <=right:
        if val not in nums:
            return -1
        if val ==nums[left]:
            return left
        elif val ==nums[right]:
            return right
        else:
            mid =(left+ right)//2
            if val <nums[mid]:
                right =mid
            elif val >nums[mid]:
                left =mid
            else:
                return mid

    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while left <= right:
            if target not in nums:
                return -1
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid

    def search2(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while left <= right:
            if target not in nums:
                return -1
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid