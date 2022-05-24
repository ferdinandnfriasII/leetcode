#leetcode practice question 1228
#given an array, determine which number is missing from arithmetic sequence

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        """    0     2
        arr = [5, 7, 11, 13, 15, 17]
               l     m           r
               l  m  r 
                     lr
               
                0     2       4   5
               [5, 7, 9, 11, 13, 17]
                l     m           r
                         l   m    r
                                 lr
            
        
        """
        l, r = 0, len(arr) - 1
        res = 0
        
        
        if arr[r] < arr[l]:
            arr.reverse()
            
        diff = (arr[r] - arr[l]) // len(arr)
        
        while l < r:
            m = l + (r - l) // 2
        
            if arr[m] == arr[0] + diff * m:
                l = m + 1
            else:
                r = m
                
        #Calculate missing value when l = r
        res = arr[0] + diff * r
        
        return res

