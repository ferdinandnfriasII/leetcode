#leetcode practice question 33
#if a sorted array is pivoted, use binary search to find the target 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Notes:
        [0,1,2,4,5,6,7] rotated at pivot index 3 becomes [4,5,6,7,0,1,2]
        
        regular binary search:
        
        l = 0, r = 6, m = 3
        [0,1,2,4,5,6,7] target = 6
         l     m     r
                 l m r
                 
         target > num[m]: 
         l = m + 1 
         
         target < num[m]:
         r = m - 1
         
         target == num[m]:
         return m
        """
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if target == nums[m]:
                return m
            
            #left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1
            