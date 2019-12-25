class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        address = 0
        
        for i in nums2:
            if m == 0:
                nums1[0] = nums2[0]
                m += 1
                continue
            if i >= nums1[m-1]: 
                nums1[m] = i
                m += 1
                continue
            for j in range(address, m):
                if i < nums1[j] and j == 0: 
                    nums1.insert(0, i)
                    nums1.pop(-1)
                    m += 1
                    break                    
                if i >= nums1[j] and i < nums1[j+1]:
                    nums1.insert(j+1, i)
                    nums1.pop(-1)
                    address = j + 1
                    m += 1
                    break
