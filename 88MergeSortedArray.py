class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0 and m > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m-1+n] = nums2[n-1]
                n = n-1
            else:
                nums1[m-1+n], nums1[m-1] = nums1[m-1], nums1[m-1+n]
                m = m -1
        if m == 0 and n> 0:
            nums1[:n] = nums2[:n]
        return nums1
