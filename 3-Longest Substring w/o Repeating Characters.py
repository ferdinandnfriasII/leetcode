#leetcode practice question 3
#determine the longest substring of a string without having repeated characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
                              l  
        [a, b, c, a, b, c, b, b]
                              r
         
        res = 0
        charSet = {, b, c}
        Sliding Window:
        
        step 1. initialize charSet, l and r pointer
        step 2. iterate through the string
                if s[r] is in the charSet:  
                    remove the s[l] from set
                    and increment l by 1
                if s[r] is not in the charSet:
                    add to the set
                
                calculate the max
        
        
        """
        charSet = set()
        res = 0
        
        l = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            print(charSet)
            res = max(res, r - l + 1)
        return res