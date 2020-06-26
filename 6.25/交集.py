from typing import List
def intersection(self,nums1:List[int],nums2:List[int])->List[int]:
    nums1.sort()
    nums2.sort()
    i,j=0,0
    nums_set=set()
    while i <len(nums1) and j<len(nums2):
        if nums1[i]>nums2[j]:
            j +=1
        elif nums1[i]<nums2[j]:
            i +=1
        elif nums1[i]==nums2[j]:
            nums_set.add(nums1[i])
            i +=1
            j +=1
    return list(nums_set)
