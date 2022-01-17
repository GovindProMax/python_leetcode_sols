class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        last=m+n-1      
        for i in range(0,(m+n)-1):
            if nums2:
                if nums1[i] >= nums2[0]:
                    nums1.insert(i,nums2[0])
                    nums2.pop(0)
                    nums1.pop(-1)
                elif (nums1[i] < nums2[0]):
                    j=i
                    while j<n:
                        if nums1[i] > nums2[0]:
                            nums1.insert(i,nums2[0])
                            nums2.pop(0)
                            nums1.pop(-1)
                        else:
                            j+=1     
        for i in range(len(nums1)-len(nums2) ,len(nums1)):
            nums1[i]=nums2[0]
            nums2.pop(0)