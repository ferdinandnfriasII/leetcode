#leetcode practice question 704
#find target index using binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #create left/right pointer
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + ((right - left) // 2)
            
            #if target is on the left side of the midpoint
            if target < nums[mid]:
                right = mid - 1
             
            #if target is on the right side of the midpoint
            elif target > nums[mid]:
                left = mid + 1
            
            #when target is found
            else:
                return mid
        
        #when target does not exist
        return -1